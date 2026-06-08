"""Advocu API client with rate limiting and error handling."""

import logging
from typing import Any, Dict, List, Optional

import httpx

from ..config import ProgramType, settings
from ..utils.rate_limiter import RateLimiter

logger = logging.getLogger(__name__)


class AdvocuAPIError(Exception):
    """Base exception for Advocu API errors."""
    pass


class AdvocuAuthError(AdvocuAPIError):
    """Authentication error."""
    pass


class AdvocuRateLimitError(AdvocuAPIError):
    """Rate limit exceeded error."""
    pass


class AdvocuClient:
    """Client for interacting with Advocu API."""

    def __init__(self, program: ProgramType):
        """
        Initialize Advocu client for a specific program.

        Args:
            program: The program type (GDE or Docker Captains)

        Raises:
            ValueError: If program is not configured
        """
        self.program = program
        self.base_url = f"{settings.advocu_base_url}/{program.value}"

        self.token = settings.get_token(program)
        if not self.token:
            raise ValueError(f"No access token configured for {program.value}")

        self.rate_limiter = RateLimiter(
            max_requests=settings.rate_limit_requests,
            period_seconds=settings.rate_limit_period,
        )

        self.client = httpx.Client(
            timeout=30.0,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}",
            },
        )

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make an API request with rate limiting and error handling.

        Args:
            method: HTTP method (GET, POST, PATCH, etc.)
            endpoint: API endpoint path
            data: Request payload for POST/PATCH requests

        Returns:
            Response data as dictionary

        Raises:
            AdvocuAuthError: Authentication failed
            AdvocuRateLimitError: Rate limit exceeded
            AdvocuAPIError: Other API errors
        """
        # Apply rate limiting
        self.rate_limiter.acquire()

        url = f"{self.base_url}{endpoint}"
        logger.debug(f"Making {method} request to {url}")

        try:
            response = self.client.request(method, url, json=data)

            # Handle different status codes
            if response.status_code == 401:
                raise AdvocuAuthError(
                    "Authentication failed. Please check your access token."
                )
            elif response.status_code == 429:
                raise AdvocuRateLimitError(
                    "Rate limit exceeded. Please wait before making more requests."
                )
            elif response.status_code >= 400:
                error_msg = f"API request failed with status {response.status_code}"
                try:
                    error_data = response.json()
                    if "message" in error_data:
                        error_msg += f": {error_data['message']}"
                except Exception:
                    error_msg += f": {response.text}"
                raise AdvocuAPIError(error_msg)

            # Return response data
            if response.status_code == 204:  # No content
                return {}

            return response.json()

        except httpx.RequestError as e:
            raise AdvocuAPIError(f"Network error: {str(e)}")

    def create_activity_draft(
        self,
        activity_type: str,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Create a new activity draft.

        Note: This creates a DRAFT that needs to be published manually
        or via update_activity() with publish=True.

        Args:
            activity_type: Type of activity (e.g., 'public-speaking', 'content-creation')
            data: Activity data

        Returns:
            Created activity draft data (contains 'id' field)
        """
        endpoint = f"/activity-drafts/{activity_type}"
        return self._make_request("POST", endpoint, data)

    def get_activities(self) -> List[Dict[str, Any]]:
        """
        Get all activities for the user.

        Returns:
            List of activities
        """
        response = self._make_request("GET", "/activities")

        # API returns {"content": [...]} instead of array directly
        if isinstance(response, dict) and "content" in response:
            return response["content"]

        # Fallback for direct array response
        return response if isinstance(response, list) else []

    def update_activity(
        self,
        activity_id: str,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Update an existing activity.

        Args:
            activity_id: ID of the activity to update
            data: Updated activity data

        Returns:
            Updated activity data
        """
        endpoint = f"/activities/{activity_id}"
        return self._make_request("PATCH", endpoint, data)

    def publish_draft(
        self,
        draft_id: str,
    ) -> Dict[str, Any]:
        """
        Publish a draft activity.

        This is a convenience method that updates the activity to publish it.
        The exact payload needed may vary - this is a best-effort implementation.

        Args:
            draft_id: ID of the draft to publish (returned from create_activity_draft)

        Returns:
            Updated activity data
        """
        # Attempt to publish by updating with minimal data
        # The API might require specific fields or just accept an empty PATCH
        return self.update_activity(draft_id, {})

    def close(self):
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

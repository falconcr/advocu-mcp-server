"""Docker Captain tools for Advocu MCP Server."""

import logging
from typing import Any, Dict, List, Optional

from .clients.advocu import AdvocuAPIError, AdvocuAuthError, AdvocuClient
from .config import ProgramType
from .models import (
    Dates,
    DockerAmplificationActivity,
    DockerEventActivity,
    DockerFeedbackSessionActivity,
    DockerPublicSpeakingActivity,
    DockerResourceActivity,
    Metrics,
)

logger = logging.getLogger(__name__)


def submit_docker_public_speaking(
    title: str,
    description: str = "",
    activity_date: str = "",
    activity_url: str = "",
    format_type: str = "",
    duration_minutes: int = 0,
    attendees: int = 0,
    tags: str = "",
    additional_info: str = "",
    private: bool = False,
) -> Dict[str, Any]:
    """
    Submit a Docker Captain public speaking activity.

    Args:
        title: Title of your talk (required, 3-200 chars)
        description: What was it about?
        activity_date: Date of your talk (YYYY-MM-DD format)
        activity_url: URL to slides, recording, or event page
        format_type: Format (In-person, Virtual, Hybrid, Recorded)
        duration_minutes: How long did your talk take (in minutes)?
        attendees: Approximate number of attendees
        tags: Comma-separated tags (e.g., "Docker, Kubernetes, DevOps")
        additional_info: Additional information
        private: Make this activity private? (default: False)

    Returns:
        Created activity draft information

    Example:
        "I gave a talk titled 'Advanced Docker Networking' at DockerCon 2026 on 2026-06-05.
        It was in-person, lasted 45 minutes, and had about 500 attendees"
    """
    try:
        # Build metrics if attendees provided
        metrics = None
        if attendees > 0:
            metrics = Metrics(attendees=attendees)

        # Parse tags
        tag_list = [t.strip() for t in tags.split(",")] if tags else None

        activity = DockerPublicSpeakingActivity(
            title=title,
            description=description or None,
            activityDate=activity_date or None,
            activityUrl=activity_url or None,
            format=format_type or None,
            duration=duration_minutes if duration_minutes > 0 else None,
            metrics=metrics,
            tags=tag_list,
            additionalInfo=additional_info or None,
            private=private,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "public-speaking",
                activity.model_dump(exclude_none=True, by_alias=True),
            )

        return {
            "success": True,
            "message": "Public speaking activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the Docker Captains portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://hub.docker.com/",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker speaking activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


def submit_docker_resource(
    title: str,
    description: str = "",
    activity_date: str = "",
    activity_url: str = "",
    content_type: str = "",
    views: int = 0,
    likes: int = 0,
    comments: int = 0,
    shares: int = 0,
    tags: str = "",
    additional_info: str = "",
    private: bool = False,
) -> Dict[str, Any]:
    """
    Submit a Docker Captain resource (article, video, tutorial, documentation).

    Args:
        title: Name of your project/resource (required, 3-200 chars)
        description: What is this resource about?
        activity_date: Date published (YYYY-MM-DD format)
        activity_url: Link to the resource
        content_type: Type (Blog post, Video, Tutorial, Documentation, Repository, etc.)
        views: Number of views/reads
        likes: Number of likes
        comments: Number of comments
        shares: Number of shares
        tags: Comma-separated tags
        additional_info: Additional information
        private: Make this activity private? (default: False)

    Returns:
        Created activity draft information

    Example:
        "I published a blog post titled 'Docker Compose Best Practices' on 2026-06-01.
        It's on my blog at example.com/docker-compose and has 5000 views so far"
    """
    try:
        # Build metrics if any metrics provided
        metrics = None
        if any([views, likes, comments, shares]):
            metrics = Metrics(
                views=views if views > 0 else None,
                likes=likes if likes > 0 else None,
                comments=comments if comments > 0 else None,
                shares=shares if shares > 0 else None,
            )

        # Parse tags
        tag_list = [t.strip() for t in tags.split(",")] if tags else None

        activity = DockerResourceActivity(
            title=title,
            description=description or None,
            activityDate=activity_date or None,
            activityUrl=activity_url or None,
            contentType=content_type or None,
            metrics=metrics,
            tags=tag_list,
            additionalInfo=additional_info or None,
            private=private,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "resources",
                activity.model_dump(exclude_none=True, by_alias=True),
            )

        return {
            "success": True,
            "message": "Resource activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the Docker Captains portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://hub.docker.com/",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker resource activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


def submit_docker_event(
    title: str,
    description: str = "",
    activity_url: str = "",
    start_date: str = "",
    end_date: str = "",
    event_type: str = "",
    format_type: str = "",
    duration: str = "",
    attendees: int = 0,
    tags: str = "",
    additional_info: str = "",
    private: bool = False,
) -> Dict[str, Any]:
    """
    Submit a Docker Captain organized event (workshop, meetup, hackathon).

    Args:
        title: Event title (required, 3-200 chars)
        description: Event description
        activity_url: Event URL
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD) - optional for single-day events
        event_type: Type (Workshop, Meetup, Hackathon, Conference, Training, etc.)
        format_type: Format (In-person, Virtual, Hybrid)
        duration: Duration (1-2 hours, 2-4 hours, 4-8 hours, Full day, Multi-day)
        attendees: Number of participants
        tags: Comma-separated tags
        additional_info: Additional information
        private: Make this activity private? (default: False)

    Returns:
        Created activity draft information

    Example:
        "I organized a Docker workshop titled 'Container Security' on 2026-06-03.
        It was in-person, lasted 4 hours (2-4 hours), and had 30 attendees"
    """
    try:
        # Build dates if provided
        dates = None
        if start_date:
            dates = Dates(
                startDate=start_date,
                endDate=end_date if end_date else None,
            )

        # Build metrics if attendees provided
        metrics = None
        if attendees > 0:
            metrics = Metrics(attendees=attendees)

        # Parse tags
        tag_list = [t.strip() for t in tags.split(",")] if tags else None

        activity = DockerEventActivity(
            title=title,
            description=description or None,
            activityUrl=activity_url or None,
            dates=dates,
            type=event_type or None,
            format=format_type or None,
            duration=duration or None,
            metrics=metrics,
            tags=tag_list,
            additionalInfo=additional_info or None,
            private=private,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "event",
                activity.model_dump(exclude_none=True, by_alias=True),
            )

        return {
            "success": True,
            "message": "Event activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the Docker Captains portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://hub.docker.com/",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker event activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


def submit_docker_feedback(
    title: str,
    description: str = "",
    activity_date: str = "",
    docker_representative: str = "",
    mode_of_communication: str = "",
    time_spent_minutes: int = 0,
    private: bool = False,
) -> Dict[str, Any]:
    """
    Submit a Docker Captain feedback session activity.

    Args:
        title: Docker feature discussed (required, 3-200 chars)
        description: Key feedback points discussed
        activity_date: Date of the feedback session (YYYY-MM-DD)
        docker_representative: Docker representative name
        mode_of_communication: Mode (Direct call, Email, Slack, Meeting)
        time_spent_minutes: Time spent in minutes
        private: Make this activity private? (default: False)

    Returns:
        Created activity draft information

    Example:
        "I participated in a feedback session about 'Docker Desktop Networking' on 2026-06-04
        with Varun Kapoor via Direct call. We discussed UX improvements for 45 minutes"
    """
    try:
        # Build metrics if time_spent provided
        metrics = None
        if time_spent_minutes > 0:
            metrics = Metrics(timeSpent=time_spent_minutes)

        activity = DockerFeedbackSessionActivity(
            title=title,
            description=description or None,
            activityDate=activity_date or None,
            dockerRepresentative=docker_representative or None,
            modeOfCommunication=mode_of_communication or None,
            metrics=metrics,
            private=private,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "feedbackSession",
                activity.model_dump(exclude_none=True, by_alias=True),
            )

        return {
            "success": True,
            "message": "Feedback session DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the Docker Captains portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://hub.docker.com/",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker feedback activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


def submit_docker_amplification(
    title: str,
    description: str = "",
    activity_date: str = "",
    url: str = "",
    amplification_type: str = "",
    channels: str = "",
    reach: int = 0,
    impressions: int = 0,
    likes: int = 0,
    shares: int = 0,
    comments: int = 0,
    private: bool = False,
) -> Dict[str, Any]:
    """
    Submit a Docker Captain amplification activity (social media, community engagement).

    Args:
        title: Activity title (required, 3-200 chars)
        description: What you amplified and how
        activity_date: Date of the amplification (YYYY-MM-DD)
        url: URL to post or content (max 100 chars)
        amplification_type: Comma-separated types (Social media post, Blog post, Newsletter)
        channels: Comma-separated channels (Twitter, LinkedIn, Facebook, Blog)
        reach: Estimated reach
        impressions: Impressions count
        likes: Number of likes
        shares: Number of shares/retweets
        comments: Number of comments
        private: Make this activity private? (default: False)

    Returns:
        Created activity draft information

    Example:
        "I shared Docker's new features announcement on Twitter and LinkedIn on 2026-06-06.
        Got 10000 impressions with 200 likes and 50 retweets"
    """
    try:
        # Build metrics if any metrics provided
        metrics = None
        if any([reach, impressions, likes, shares, comments]):
            metrics = Metrics(
                reach=reach if reach > 0 else None,
                impressions=impressions if impressions > 0 else None,
                likes=likes if likes > 0 else None,
                shares=shares if shares > 0 else None,
                comments=comments if comments > 0 else None,
            )

        # Parse type and channels
        type_list = [t.strip() for t in amplification_type.split(",")] if amplification_type else None
        channel_list = [c.strip() for c in channels.split(",")] if channels else None

        activity = DockerAmplificationActivity(
            title=title,
            description=description or None,
            activityDate=activity_date or None,
            url=url or None,
            type=type_list,
            channel=channel_list,
            metrics=metrics,
            private=private,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "amplification",
                activity.model_dump(exclude_none=True, by_alias=True),
            )

        return {
            "success": True,
            "message": "Amplification activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the Docker Captains portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://hub.docker.com/",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker amplification activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}

"""Rate limiter for API requests."""

import time
from collections import deque
from typing import Deque


class RateLimiter:
    """Token bucket rate limiter for API requests."""

    def __init__(self, max_requests: int, period_seconds: int):
        """
        Initialize rate limiter.

        Args:
            max_requests: Maximum number of requests allowed in the period
            period_seconds: Time period in seconds
        """
        self.max_requests = max_requests
        self.period = period_seconds
        self.requests: Deque[float] = deque()

    def acquire(self) -> None:
        """
        Wait if necessary to respect rate limits.

        Blocks until a request can be made within rate limits.
        """
        now = time.time()

        # Remove requests outside the current window
        while self.requests and self.requests[0] <= now - self.period:
            self.requests.popleft()

        # If at limit, wait until oldest request expires
        if len(self.requests) >= self.max_requests:
            sleep_time = self.period - (now - self.requests[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
            self.requests.popleft()

        # Record this request
        self.requests.append(time.time())

    def can_proceed(self) -> bool:
        """Check if a request can proceed without waiting."""
        now = time.time()

        # Remove old requests
        while self.requests and self.requests[0] <= now - self.period:
            self.requests.popleft()

        return len(self.requests) < self.max_requests

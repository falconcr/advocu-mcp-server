"""Base models for activities."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class BaseActivity(BaseModel):
    """Base model for all activities."""

    title: str = Field(..., min_length=1, max_length=500, description="Activity title")
    description: Optional[str] = Field(None, description="Detailed description")
    date: datetime = Field(..., description="Activity date (ISO format)")
    url: Optional[str] = Field(None, description="URL related to the activity")

    @field_validator("date", mode="before")
    @classmethod
    def parse_date(cls, v):
        """Parse date from various formats."""
        if isinstance(v, str):
            # Try to parse common date formats
            try:
                return datetime.fromisoformat(v.replace("Z", "+00:00"))
            except ValueError:
                pass
        return v

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "title": "Example Activity",
                "description": "A sample activity description",
                "date": "2026-06-08T10:00:00Z",
                "url": "https://example.com/activity",
            }
        }

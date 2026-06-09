"""Base models for activities."""

from datetime import date as date_type, datetime
from typing import Optional

from pydantic import BaseModel, Field, field_serializer, field_validator


class BaseActivity(BaseModel):
    """Base model for all activities."""

    title: str = Field(..., min_length=1, max_length=500, description="Activity title")
    description: Optional[str] = Field(None, description="Detailed description")
    date: date_type = Field(..., description="Activity date (ISO format)", serialization_alias="activityDate")
    url: Optional[str] = Field(None, description="URL related to the activity", serialization_alias="activityUrl")

    @field_validator("date", mode="before")
    @classmethod
    def parse_date(cls, v):
        """Parse date from various formats."""
        if isinstance(v, str):
            # Try to parse common date formats
            try:
                # Parse as datetime first
                dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
                # Return just the date part
                return dt.date()
            except ValueError:
                pass
        if isinstance(v, datetime):
            return v.date()
        return v

    @field_serializer("date")
    def serialize_date(self, value: date_type) -> str:
        """Serialize date as YYYY-MM-DD string."""
        return value.isoformat()

    class Config:
        """Pydantic config."""
        populate_by_name = True  # Allow using both field name and alias
        json_schema_extra = {
            "example": {
                "title": "Example Activity",
                "description": "A sample activity description",
                "activityDate": "2026-06-08",
                "activityUrl": "https://example.com/activity",
            }
        }

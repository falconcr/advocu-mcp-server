"""Pydantic models for GDE activities."""

from typing import Optional

from pydantic import Field

from .base import BaseActivity


class GDEPublicSpeakingActivity(BaseActivity):
    """Model for GDE public speaking activities."""

    event_name: str = Field(..., description="Name of the event")
    location: Optional[str] = Field(None, description="Event location (city, country)")
    attendees: Optional[int] = Field(None, ge=1, description="Number of attendees")
    topics: Optional[str] = Field(None, description="Topics covered")


class GDEContentCreationActivity(BaseActivity):
    """Model for GDE content creation (articles, videos, tutorials)."""

    content_type: str = Field(
        ...,
        description="Type of content (article, video, tutorial, documentation, etc.)",
    )
    views: Optional[int] = Field(None, ge=0, description="Number of views/reads")
    engagement: Optional[str] = Field(
        None,
        description="Engagement metrics (likes, comments, shares)",
    )


class GDEWorkshopActivity(BaseActivity):
    """Model for GDE workshops and training sessions."""

    attendees: Optional[int] = Field(None, ge=1, description="Number of attendees")
    duration_hours: Optional[float] = Field(None, ge=0, description="Workshop duration in hours")
    topics: Optional[str] = Field(None, description="Topics covered")


class GDEMentoringActivity(BaseActivity):
    """Model for GDE mentoring activities."""

    mentees: Optional[int] = Field(None, ge=1, description="Number of mentees")
    duration_hours: Optional[float] = Field(None, ge=0, description="Total mentoring hours")
    topics: Optional[str] = Field(None, description="Topics covered in mentoring")


class GDEProductFeedbackActivity(BaseActivity):
    """Model for GDE product feedback."""

    product_name: str = Field(..., description="Google product name")
    feedback_type: Optional[str] = Field(
        None,
        description="Type of feedback (bug report, feature request, usability, etc.)",
    )
    impact: Optional[str] = Field(None, description="Potential impact of the feedback")


class GDEInteractionActivity(BaseActivity):
    """Model for GDE interactions with Googlers."""

    googler_team: Optional[str] = Field(None, description="Google team involved")
    interaction_type: Optional[str] = Field(
        None,
        description="Type of interaction (meeting, email, collaboration, etc.)",
    )
    topics: Optional[str] = Field(None, description="Topics discussed")


class GDEStoryActivity(BaseActivity):
    """Model for GDE success stories."""

    story_type: Optional[str] = Field(
        None,
        description="Type of story (case study, testimonial, impact story, etc.)",
    )
    impact: Optional[str] = Field(None, description="Impact of the story")

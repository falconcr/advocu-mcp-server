"""Pydantic models for GDE activities - based on official API spec."""

from typing import List, Optional

from pydantic import BaseModel, Field


class GDEMetrics(BaseModel):
    """Metrics object for GDE activities."""

    readers: Optional[int] = Field(None, ge=1, description="How many people read your content?")
    # Note: Different activity types may have different metrics fields


class GDEContentCreationActivity(BaseModel):
    """Model for GDE content creation (articles, videos, tutorials)."""

    contentType: Optional[str] = Field(
        None,
        description="Content type - enum with 7 values from API"
    )
    title: Optional[str] = Field(None, min_length=3, max_length=200, description="What was the title?")
    description: Optional[str] = Field(None, max_length=2000, description="What was it about?")
    tags: Optional[List[str]] = Field(None, description="Tags (86 possible values)")
    metrics: Optional[GDEMetrics] = Field(None, description="Metrics")
    activityDate: Optional[str] = Field(
        None,
        description="Date published (YYYY-MM-DD)",
        pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
    activityUrl: Optional[str] = Field(
        None,
        max_length=500,
        description="Link to Content",
        pattern=r"https?:\/\/(www\.)?.*"
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    private: Optional[bool] = Field(None, description="Do you want to make this activity private?")


class GDEPublicSpeakingActivity(BaseModel):
    """Model for GDE public speaking activities."""

    title: Optional[str] = Field(None, min_length=3, max_length=200, description="What was the title of your talk?")
    description: Optional[str] = Field(None, max_length=2000, description="What was it about?")
    tags: Optional[List[str]] = Field(None, description="Tags")
    metrics: Optional[dict] = Field(None, description="Metrics")
    eventFormat: Optional[str] = Field(None, description="Select event format (enum with 3 values)")
    country: Optional[str] = Field(None, description="Country (enum with 251 values)")
    inPersonAttendees: Optional[int] = Field(
        None,
        ge=0,
        description="Out of all, how many people attended your session in-person?"
    )
    activityDate: Optional[str] = Field(
        None,
        description="Date of your talk",
        pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
    activityUrl: Optional[str] = Field(
        None,
        max_length=500,
        description="Share the event link",
        pattern=r"https?:\/\/(www\.)?.*"
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    private: Optional[bool] = Field(None, description="Do you want to make this activity private?")


class GDEWorkshopActivity(BaseModel):
    """Model for GDE workshops and training sessions."""

    title: Optional[str] = Field(None, min_length=3, max_length=200, description="What was the name of your workshop session?")
    description: Optional[str] = Field(None, max_length=2000, description="What was it about?")
    tags: Optional[List[str]] = Field(None, description="Tags")
    metrics: Optional[dict] = Field(None, description="Metrics")
    eventFormat: Optional[str] = Field(None, description="Select event format (enum with 3 values)")
    country: Optional[str] = Field(None, description="Country (enum with 251 values)")
    inPersonAttendees: Optional[int] = Field(
        None,
        ge=0,
        description="Out of all, how many people attended your session in-person?"
    )
    activityDate: Optional[str] = Field(
        None,
        description="Date of your workshop",
        pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
    activityUrl: Optional[str] = Field(
        None,
        max_length=500,
        description="Share the event link",
        pattern=r"https?:\/\/(www\.)?.*"
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    private: Optional[bool] = Field(None, description="Do you want to make this activity private?")


class GDEMentoringActivity(BaseModel):
    """Model for GDE mentoring activities."""

    title: Optional[str] = Field(None, min_length=3, max_length=200, description="What was the name of your mentoring session?")
    description: Optional[str] = Field(None, max_length=2000, description="What was it about?")
    tags: Optional[List[str]] = Field(None, description="Tags")
    metrics: Optional[dict] = Field(None, description="Metrics")
    eventFormat: Optional[str] = Field(None, description="Select event format (enum with 3 values)")
    country: Optional[str] = Field(None, description="Country (enum with 251 values)")
    inPersonAttendees: Optional[int] = Field(
        None,
        ge=0,
        description="Out of all, how many people attended your session in-person?"
    )
    activityDate: Optional[str] = Field(
        None,
        description="Date of your mentoring session",
        pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
    activityUrl: Optional[str] = Field(
        None,
        max_length=500,
        description="Share the event link",
        pattern=r"https?:\/\/(www\.)?.*"
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    private: Optional[bool] = Field(None, description="Do you want to make this activity private?")


class GDEProductFeedbackActivity(BaseModel):
    """Model for GDE product feedback."""

    title: Optional[str] = Field(None, min_length=3, max_length=200, description="Title")
    description: Optional[str] = Field(None, max_length=2000, description="Description")
    contentType: Optional[str] = Field(None, description="Content type (enum with 2 values)")
    productDescription: Optional[str] = Field(None, max_length=500, description="What product was it about?")
    tags: Optional[List[str]] = Field(None, description="Tags")
    metrics: Optional[dict] = Field(None, description="Metrics")
    activityDate: Optional[str] = Field(
        None,
        description="Participation Date",
        pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    private: Optional[bool] = Field(None, description="Do you want to make this activity private?")


class GDEInteractionActivity(BaseModel):
    """Model for GDE interactions with Googlers."""

    title: Optional[str] = Field(None, min_length=3, max_length=200, description="Title")
    description: Optional[str] = Field(None, max_length=2000, description="Description")
    format: Optional[str] = Field(None, description="Format (enum with 8 values)")
    interactionType: Optional[str] = Field(None, description="Interaction Type (enum with 6 values)")
    tags: Optional[List[str]] = Field(None, description="Tags")
    metrics: Optional[dict] = Field(None, description="Metrics")
    activityDate: Optional[str] = Field(
        None,
        description="Interaction Date",
        pattern=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    additionalLinks: Optional[str] = Field(None, max_length=2000, description="Additional links")
    private: Optional[bool] = Field(None, description="Do you want to make this activity private?")


class GDEStoryActivity(BaseModel):
    """Model for GDE success stories."""

    title: Optional[str] = Field(None, min_length=3, max_length=200, description="Title of the story")
    description: Optional[str] = Field(None, max_length=2000, description="Description")
    whyIsSignificant: Optional[str] = Field(None, max_length=2000, description="Tell us more about it and why it is significant")
    significanceType: Optional[str] = Field(None, description="Significance type (enum with 6 values)")
    activityUrl: Optional[str] = Field(
        None,
        max_length=500,
        description="Link",
        pattern=r"https?:\/\/(www\.)?.*"
    )
    tags: Optional[List[str]] = Field(None, description="Tags")
    metrics: Optional[dict] = Field(None, description="Metrics")
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    private: Optional[bool] = Field(None, description="Do you want to make this activity private?")

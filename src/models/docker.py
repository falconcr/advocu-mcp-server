"""Pydantic models for Docker Captains activities matching Advocu API schema."""

from typing import List, Optional

from pydantic import BaseModel, Field


class Metrics(BaseModel):
    """Metrics for various activity types."""

    # Common metrics
    views: Optional[int] = Field(None, ge=0, description="Number of views")
    likes: Optional[int] = Field(None, ge=0, description="Number of likes")
    comments: Optional[int] = Field(None, ge=0, description="Number of comments")
    shares: Optional[int] = Field(None, ge=0, description="Number of shares")

    # Speaking/Event metrics
    attendees: Optional[int] = Field(None, ge=1, description="Number of attendees")

    # Feedback session metrics
    timeSpent: Optional[int] = Field(None, ge=1, description="Time spent in minutes")

    # Amplification metrics
    reach: Optional[int] = Field(None, ge=0, description="Estimated reach")
    impressions: Optional[int] = Field(None, ge=0, description="Impressions")


class Dates(BaseModel):
    """Date range for events."""

    startDate: Optional[str] = Field(None, description="Start date (YYYY-MM-DD)")
    endDate: Optional[str] = Field(None, description="End date (YYYY-MM-DD)")


class DockerPublicSpeakingActivity(BaseModel):
    """Model for Docker Captain public speaking activities."""

    title: str = Field(..., min_length=3, max_length=200, description="Title of your talk")
    description: Optional[str] = Field(None, max_length=2000, description="What was it about?")
    tags: Optional[List[str]] = Field(None, description="Tags")
    activityUrl: Optional[str] = Field(None, max_length=500, description="Share any relevant link")
    activityDate: Optional[str] = Field(None, description="Date of your talk (YYYY-MM-DD)")
    format: Optional[str] = Field(
        None,
        description="Talk format: In-person, Virtual, Hybrid, Recorded"
    )
    duration: Optional[int] = Field(None, ge=1, description="How long did your talk take (in minutes)?")
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    metrics: Optional[Metrics] = Field(None, description="Metrics")
    private: Optional[bool] = Field(False, description="Make this activity private?")


class DockerResourceActivity(BaseModel):
    """Model for Docker Captain resources (articles, videos, tutorials)."""

    title: str = Field(..., min_length=3, max_length=200, description="Name of your project")
    description: Optional[str] = Field(None, max_length=2000, description="What is this resource about?")
    tags: Optional[List[str]] = Field(None, description="Tags")
    activityUrl: Optional[str] = Field(None, max_length=500, description="Link to the resource")
    activityDate: Optional[str] = Field(None, description="Date published (YYYY-MM-DD)")
    metrics: Optional[Metrics] = Field(None, description="Metrics (views, likes, etc.)")
    contentType: Optional[str] = Field(
        None,
        description="Content type: Blog post, Video, Tutorial, Documentation, Repository, etc."
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    private: Optional[bool] = Field(False, description="Make this activity private?")


class DockerEventActivity(BaseModel):
    """Model for Docker Captain organized events."""

    title: str = Field(..., min_length=3, max_length=200, description="What is your event title?")
    description: Optional[str] = Field(None, max_length=2000, description="Description")
    tags: Optional[List[str]] = Field(None, description="Tags")
    activityUrl: Optional[str] = Field(None, max_length=500, description="Event URL")
    dates: Optional[Dates] = Field(None, description="Event dates")
    type: Optional[str] = Field(
        None,
        description="Event type: Workshop, Meetup, Hackathon, Conference, Training, etc."
    )
    format: Optional[str] = Field(
        None,
        description="Format: In-person, Virtual, Hybrid, etc."
    )
    duration: Optional[str] = Field(
        None,
        description="Event duration: 1-2 hours, 2-4 hours, 4-8 hours, Full day, Multi-day"
    )
    additionalInfo: Optional[str] = Field(None, max_length=2000, description="Additional information")
    metrics: Optional[Metrics] = Field(None, description="Metrics (attendees, etc.)")
    private: Optional[bool] = Field(False, description="Make this activity private?")


class DockerFeedbackSessionActivity(BaseModel):
    """Model for Docker Captain feedback sessions."""

    title: str = Field(..., min_length=3, max_length=200, description="Docker feature discussed")
    description: Optional[str] = Field(None, max_length=2000, description="Key feedback points discussed")
    activityDate: Optional[str] = Field(None, description="Date of the feedback session (YYYY-MM-DD)")
    dockerRepresentative: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100,
        description="Docker representative"
    )
    modeOfCommunication: Optional[str] = Field(
        None,
        description="Mode: Direct call, Email, Slack, Meeting"
    )
    metrics: Optional[Metrics] = Field(None, description="Metrics (timeSpent in minutes)")
    private: Optional[bool] = Field(False, description="Make this activity private?")


class DockerAmplificationActivity(BaseModel):
    """Model for Docker Captain amplification activities (social media, community)."""

    title: str = Field(..., min_length=3, max_length=200, description="Activity title")
    description: Optional[str] = Field(None, max_length=2000, description="Description")
    activityDate: Optional[str] = Field(None, description="Date of the amplification (YYYY-MM-DD)")
    type: Optional[List[str]] = Field(
        None,
        min_items=1,
        max_items=3,
        description="Type: Social media post, Blog post, Newsletter"
    )
    channel: Optional[List[str]] = Field(
        None,
        min_items=1,
        max_items=4,
        description="Channel: Twitter, LinkedIn, Facebook, Blog"
    )
    url: Optional[str] = Field(None, max_length=100, description="URL Link")
    metrics: Optional[Metrics] = Field(None, description="Metrics (reach, impressions, etc.)")
    private: Optional[bool] = Field(False, description="Make this activity private?")

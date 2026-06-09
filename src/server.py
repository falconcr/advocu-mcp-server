"""Advocu MCP Server - Unified server for GDE and Docker Captains."""

import logging
from typing import Any, Dict

from fastmcp import FastMCP

from .clients.advocu import AdvocuAPIError, AdvocuAuthError, AdvocuClient
from .config import ProgramType, settings
from . import server_docker

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("advocu-mcp-server")


# ==================== Docker Captains Tools ====================


@mcp.tool()
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
    """
    return server_docker.submit_docker_public_speaking(
        title=title,
        description=description,
        activity_date=activity_date,
        activity_url=activity_url,
        format_type=format_type,
        duration_minutes=duration_minutes,
        attendees=attendees,
        tags=tags,
        additional_info=additional_info,
        private=private,
    )


@mcp.tool()
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
    """
    return server_docker.submit_docker_resource(
        title=title,
        description=description,
        activity_date=activity_date,
        activity_url=activity_url,
        content_type=content_type,
        views=views,
        likes=likes,
        comments=comments,
        shares=shares,
        tags=tags,
        additional_info=additional_info,
        private=private,
    )


@mcp.tool()
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
    """
    return server_docker.submit_docker_event(
        title=title,
        description=description,
        activity_url=activity_url,
        start_date=start_date,
        end_date=end_date,
        event_type=event_type,
        format_type=format_type,
        duration=duration,
        attendees=attendees,
        tags=tags,
        additional_info=additional_info,
        private=private,
    )


@mcp.tool()
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
    """
    return server_docker.submit_docker_feedback(
        title=title,
        description=description,
        activity_date=activity_date,
        docker_representative=docker_representative,
        mode_of_communication=mode_of_communication,
        time_spent_minutes=time_spent_minutes,
        private=private,
    )


@mcp.tool()
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
    """
    return server_docker.submit_docker_amplification(
        title=title,
        description=description,
        activity_date=activity_date,
        url=url,
        amplification_type=amplification_type,
        channels=channels,
        reach=reach,
        impressions=impressions,
        likes=likes,
        shares=shares,
        comments=comments,
        private=private,
    )


# ==================== GDE Tools ====================


@mcp.tool()
def submit_gde_public_speaking(
    title: str,
    date: str,
    event_name: str,
    description: str = "",
    url: str = "",
    location: str = "",
    attendees: int = 0,
    topics: str = "",
) -> Dict[str, Any]:
    """
    Submit a GDE public speaking activity (conference, meetup, presentation).

    Args:
        title: Title of your presentation
        date: Date of the event (ISO format: YYYY-MM-DD)
        event_name: Name of the event/conference (will be added to description)
        description: Detailed description of the talk
        url: URL to slides, recording, or event page
        location: Location of the event (will be mapped to country field)
        attendees: Approximate number of attendees (in-person)
        topics: Google technologies covered (will be added to description)

    Returns:
        Created activity draft information
    """
    from .models.gde import GDEPublicSpeakingActivity

    try:
        # Build description with event name and topics
        full_description = description or ""
        if event_name:
            full_description = f"Event: {event_name}. {full_description}".strip()
        if topics:
            full_description = f"{full_description} Topics: {topics}".strip()

        # Create activity with correct field names
        activity = GDEPublicSpeakingActivity(
            title=title,
            description=full_description or None,
            activityDate=date,
            activityUrl=url or None,
            inPersonAttendees=attendees if attendees > 0 else None,
            country=location or None,  # Map location to country
            eventFormat=None,  # Could be added as parameter
            tags=None,
            metrics=None,
            additionalInfo=None,
            private=False,
        )

        payload = activity.model_dump(exclude_none=True)

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "public-speaking",
                payload,
            )

        return {
            "success": True,
            "message": "GDE public speaking activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the GDE portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://developers.google.com/community/experts",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting GDE speaking activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_gde_content(
    title: str,
    date: str,
    content_type: str,
    description: str = "",
    url: str = "",
    views: int = 0,
    engagement: str = "",
) -> Dict[str, Any]:
    """
    Submit a GDE content creation activity (article, video, tutorial).

    Args:
        title: Title of the content
        date: Publication date (ISO format: YYYY-MM-DD)
        content_type: Type (article, video, tutorial, documentation)
        description: Content description
        url: URL to the content
        views: Number of views/reads (stored as "readers" in API)
        engagement: Engagement metrics (not currently used by API)

    Returns:
        Created activity draft information
    """
    from .models.gde import GDEContentCreationActivity, GDEMetrics

    try:
        # Map common content type values to valid enum values
        # Valid values: Articles, Books, Code contribution, Demos, Newsletters, Podcasts, Videos
        content_type_mapping = {
            "video": "Videos",
            "videos": "Videos",
            "youtube": "Videos",
            "article": "Articles",
            "articles": "Articles",
            "blog": "Articles",
            "blog post": "Articles",
            "book": "Books",
            "books": "Books",
            "code": "Code contribution",
            "code contribution": "Code contribution",
            "demo": "Demos",
            "demos": "Demos",
            "newsletter": "Newsletters",
            "newsletters": "Newsletters",
            "podcast": "Podcasts",
            "podcasts": "Podcasts",
        }

        # Normalize and map content type
        mapped_type = None
        if content_type:
            normalized = content_type.lower().strip()
            mapped_type = content_type_mapping.get(normalized, content_type)

        # Build metrics object if views provided
        metrics = None
        if views > 0:
            metrics = GDEMetrics(readers=views)

        # Create activity with correct field names
        activity = GDEContentCreationActivity(
            title=title,
            description=description or None,
            contentType=mapped_type,
            activityDate=date,
            activityUrl=url or None,
            metrics=metrics,
            tags=None,  # Could be added as a parameter later
            additionalInfo=None,
            private=False,
        )

        # Convert to dict, excluding None values
        payload = activity.model_dump(exclude_none=True)

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "content-creation",
                payload,
            )

        return {
            "success": True,
            "message": "GDE content creation activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the GDE portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://developers.google.com/community/experts",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting GDE content activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_gde_workshop(
    title: str,
    date: str,
    description: str = "",
    url: str = "",
    attendees: int = 0,
    duration_hours: float = 0.0,
    topics: str = "",
) -> Dict[str, Any]:
    """
    Submit a GDE workshop or training activity.

    Args:
        title: Workshop title
        date: Workshop date (ISO format: YYYY-MM-DD)
        description: Workshop description
        url: URL to materials
        attendees: Number of participants (in-person)
        duration_hours: Duration in hours (not stored separately by API)
        topics: Google technologies covered (added to description)

    Returns:
        Created activity draft information
    """
    from .models.gde import GDEWorkshopActivity

    try:
        # Add topics to description
        full_description = description or ""
        if topics:
            full_description = f"{full_description} Topics: {topics}".strip()

        activity = GDEWorkshopActivity(
            title=title,
            description=full_description or None,
            activityDate=date,
            activityUrl=url or None,
            inPersonAttendees=attendees if attendees > 0 else None,
            eventFormat=None,
            country=None,
            tags=None,
            metrics=None,
            additionalInfo=None,
            private=False,
        )

        payload = activity.model_dump(exclude_none=True)

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "workshop",
                payload,
            )

        return {
            "success": True,
            "message": "GDE workshop activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the GDE portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://developers.google.com/community/experts",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting GDE workshop activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_gde_mentoring(
    title: str,
    date: str,
    description: str = "",
    url: str = "",
    mentees: int = 0,
    duration_hours: float = 0.0,
    topics: str = "",
) -> Dict[str, Any]:
    """
    Submit a GDE mentoring activity.

    Args:
        title: Mentoring session title
        date: Session date (ISO format)
        description: What was covered
        url: URL to resources shared
        mentees: Number of mentees
        duration_hours: Total hours spent
        topics: Topics covered

    Returns:
        Created activity draft information
    """
    from .models.gde import GDEMentoringActivity

    try:
        # Add topics to description
        full_description = description or ""
        if topics:
            full_description = f"{full_description} Topics: {topics}".strip()

        activity = GDEMentoringActivity(
            title=title,
            description=full_description or None,
            activityDate=date,
            activityUrl=url or None,
            inPersonAttendees=mentees if mentees > 0 else None,
            eventFormat=None,
            country=None,
            tags=None,
            metrics=None,
            additionalInfo=None,
            private=False,
        )

        payload = activity.model_dump(exclude_none=True)

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "mentoring",
                payload,
            )

        return {
            "success": True,
            "message": "GDE mentoring activity DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the GDE portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://developers.google.com/community/experts",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting GDE mentoring activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_gde_product_feedback(
    title: str,
    date: str,
    product_name: str,
    description: str = "",
    url: str = "",
    feedback_type: str = "",
    impact: str = "",
) -> Dict[str, Any]:
    """
    Submit GDE product feedback activity.

    Args:
        title: Feedback title
        date: Feedback date (ISO format)
        product_name: Google product name (e.g., "Cloud Run", "Firebase")
        description: Detailed feedback
        url: URL to issue/discussion
        feedback_type: Type (bug, feature request, usability)
        impact: Potential impact description

    Returns:
        Created activity draft information
    """
    from .models.gde import GDEProductFeedbackActivity

    try:
        activity = GDEProductFeedbackActivity(
            title=title,
            description=description or None,
            contentType=feedback_type or None,
            productDescription=product_name or None,
            activityDate=date,
            tags=None,
            metrics=None,
            additionalInfo=None,
            private=False,
        )

        payload = activity.model_dump(exclude_none=True)

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "product-feedback-given",
                payload,
            )

        return {
            "success": True,
            "message": "GDE product feedback DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the GDE portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://developers.google.com/community/experts",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting GDE feedback activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_gde_googler_interaction(
    title: str,
    date: str,
    description: str = "",
    url: str = "",
    googler_team: str = "",
    interaction_type: str = "",
    topics: str = "",
) -> Dict[str, Any]:
    """
    Submit GDE interaction with Googlers activity.

    Args:
        title: Interaction title
        date: Interaction date (ISO format)
        description: What was discussed
        url: URL to notes/recording
        googler_team: Google team name
        interaction_type: Type (meeting, email, collaboration)
        topics: Topics discussed

    Returns:
        Created activity draft information
    """
    from .models.gde import GDEInteractionActivity

    try:
        # Add topics to description
        full_description = description or ""
        if topics:
            full_description = f"{full_description} Topics: {topics}".strip()

        activity = GDEInteractionActivity(
            title=title,
            description=full_description or None,
            format=None,
            interactionType=interaction_type or None,
            activityDate=date,
            additionalInfo=googler_team or None,
            additionalLinks=url or None,
            tags=None,
            metrics=None,
            private=False,
        )

        payload = activity.model_dump(exclude_none=True)

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "interaction-with-googlers",
                payload,
            )

        return {
            "success": True,
            "message": "GDE Googler interaction DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the GDE portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://developers.google.com/community/experts",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting GDE interaction activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_gde_story(
    title: str,
    date: str,
    description: str = "",
    url: str = "",
    story_type: str = "",
    impact: str = "",
) -> Dict[str, Any]:
    """
    Submit GDE success story activity.

    Args:
        title: Story title
        date: Story date (ISO format)
        description: Story details
        url: URL to the story
        story_type: Type (case study, testimonial, impact story)
        impact: Impact description

    Returns:
        Created activity draft information
    """
    from .models.gde import GDEStoryActivity

    try:
        activity = GDEStoryActivity(
            title=title,
            description=description or None,
            whyIsSignificant=impact or None,
            significanceType=story_type or None,
            activityUrl=url or None,
            tags=None,
            metrics=None,
            additionalInfo=None,
            private=False,
        )

        payload = activity.model_dump(exclude_none=True)

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "stories",
                payload,
            )

        return {
            "success": True,
            "message": "GDE story DRAFT created successfully",
            "draft_id": result.get("id"),
            "info": "⚠️ The Advocu API only allows creating DRAFTS. You need to go to the GDE portal to review and manually click 'Submit' to publish it.",
            "portal_url": "https://developers.google.com/community/experts",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting GDE story activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


# ==================== Utility Tools ====================


@mcp.tool()
def list_recent_activities(program: str = "docker", limit: int = 10) -> Dict[str, Any]:
    """
    List recent activities for a program.

    Args:
        program: Program type ("gde" or "docker", default: "docker")
        limit: Maximum number of activities to return (default: 10)

    Returns:
        List of recent activities with details
    """
    try:
        program_type = ProgramType.GDE if program.lower() == "gde" else ProgramType.DOCKER

        with AdvocuClient(program_type) as client:
            activities = client.get_activities()

        # Limit results
        activities = activities[:limit] if activities else []

        # Format activities for better readability
        formatted_activities = []
        for activity in activities:
            data = activity.get("data", {})
            formatted = {
                "type": activity.get("type", "unknown"),
                "title": data.get("title", "No title"),
                "date": data.get(
                    "activityDate",
                    activity.get("submissionDate", activity.get("date", "No date")),
                ),
                "url": data.get("activityUrl", activity.get("url", "")),
                "activityId": activity.get("activityId", ""),
            }

            # Add type-specific fields
            if "contentType" in data:
                formatted["contentType"] = data["contentType"]

            if "metrics" in data:
                formatted["metrics"] = data["metrics"]

            formatted_activities.append(formatted)

        return {
            "success": True,
            "program": program,
            "count": len(formatted_activities),
            "activities": formatted_activities,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error listing activities")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()

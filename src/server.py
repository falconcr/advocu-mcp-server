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
        date: Date of the event (ISO format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)
        event_name: Name of the event/conference
        description: Detailed description of the talk
        url: URL to slides, recording, or event page
        location: Location of the event
        attendees: Approximate number of attendees
        topics: Google technologies covered (e.g., "Firebase, Cloud Run")

    Returns:
        Created activity draft information
    """
    from .models import GDEPublicSpeakingActivity

    try:
        activity = GDEPublicSpeakingActivity(
            title=title,
            date=date,
            event_name=event_name,
            description=description or None,
            url=url or None,
            location=location or None,
            attendees=attendees if attendees > 0 else None,
            topics=topics or None,
        )

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "public-speaking",
                activity.model_dump(exclude_none=True),
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
        views: Number of views/reads
        engagement: Engagement metrics (likes, comments, shares)

    Returns:
        Created activity draft information
    """
    from .models import GDEContentCreationActivity

    try:
        activity = GDEContentCreationActivity(
            title=title,
            date=date,
            content_type=content_type,
            description=description or None,
            url=url or None,
            views=views if views > 0 else None,
            engagement=engagement or None,
        )

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "content-creation",
                activity.model_dump(exclude_none=True),
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
        date: Workshop date (ISO format)
        description: Workshop description
        url: URL to materials
        attendees: Number of participants
        duration_hours: Duration in hours
        topics: Google technologies covered

    Returns:
        Created activity draft information
    """
    from .models import GDEWorkshopActivity

    try:
        activity = GDEWorkshopActivity(
            title=title,
            date=date,
            description=description or None,
            url=url or None,
            attendees=attendees if attendees > 0 else None,
            duration_hours=duration_hours if duration_hours > 0 else None,
            topics=topics or None,
        )

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "workshop",
                activity.model_dump(exclude_none=True),
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
    from .models import GDEMentoringActivity

    try:
        activity = GDEMentoringActivity(
            title=title,
            date=date,
            description=description or None,
            url=url or None,
            mentees=mentees if mentees > 0 else None,
            duration_hours=duration_hours if duration_hours > 0 else None,
            topics=topics or None,
        )

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "mentoring",
                activity.model_dump(exclude_none=True),
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
    from .models import GDEProductFeedbackActivity

    try:
        activity = GDEProductFeedbackActivity(
            title=title,
            date=date,
            product_name=product_name,
            description=description or None,
            url=url or None,
            feedback_type=feedback_type or None,
            impact=impact or None,
        )

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "product-feedback-given",
                activity.model_dump(exclude_none=True),
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
    from .models import GDEInteractionActivity

    try:
        activity = GDEInteractionActivity(
            title=title,
            date=date,
            description=description or None,
            url=url or None,
            googler_team=googler_team or None,
            interaction_type=interaction_type or None,
            topics=topics or None,
        )

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "interaction-with-googlers",
                activity.model_dump(exclude_none=True),
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
    from .models import GDEStoryActivity

    try:
        activity = GDEStoryActivity(
            title=title,
            date=date,
            description=description or None,
            url=url or None,
            story_type=story_type or None,
            impact=impact or None,
        )

        with AdvocuClient(ProgramType.GDE) as client:
            result = client.create_activity_draft(
                "stories",
                activity.model_dump(exclude_none=True),
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

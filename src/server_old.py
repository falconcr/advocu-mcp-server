"""Advocu MCP Server - Unified server for GDE and Docker Captains."""

import logging
from typing import Any, Dict

from fastmcp import FastMCP

from .clients.advocu import AdvocuAPIError, AdvocuAuthError, AdvocuClient
from .config import ProgramType, settings
from .models import (
    DockerAmplificationActivity,
    DockerEventActivity,
    DockerFeedbackSessionActivity,
    DockerPublicSpeakingActivity,
    DockerResourceActivity,
    GDEContentCreationActivity,
    GDEInteractionActivity,
    GDEMentoringActivity,
    GDEProductFeedbackActivity,
    GDEPublicSpeakingActivity,
    GDEStoryActivity,
    GDEWorkshopActivity,
)

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
    date: str,
    event_name: str,
    description: str = "",
    url: str = "",
    location: str = "",
    attendees: int = 0,
    topics: str = "",
) -> Dict[str, Any]:
    """
    Submit a Docker Captain public speaking activity (conference, meetup, presentation).

    Args:
        title: Title of your presentation
        date: Date of the event (ISO format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)
        event_name: Name of the event/conference
        description: Detailed description of the talk
        url: URL to slides, recording, or event page
        location: Location of the event (e.g., "San Francisco, CA")
        attendees: Approximate number of attendees
        topics: Topics covered (e.g., "Docker, Kubernetes, DevOps")

    Returns:
        Created activity draft information

    Example:
        "I gave a talk called 'Advanced Docker Networking' at DockerCon 2026 on June 5th,
        2026 in San Francisco with about 500 attendees"
    """
    try:
        activity = DockerPublicSpeakingActivity(
            title=title,
            date=date,
            event_name=event_name,
            description=description or None,
            url=url or None,
            location=location or None,
            attendees=attendees if attendees > 0 else None,
            topics=topics or None,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "public-speaking",
                activity.model_dump(exclude_none=True),
            )

        return {
            "success": True,
            "message": "Public speaking activity submitted successfully",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker speaking activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_docker_resource(
    title: str,
    date: str,
    resource_type: str,
    description: str = "",
    url: str = "",
    views: int = 0,
    engagement: str = "",
) -> Dict[str, Any]:
    """
    Submit a Docker Captain resource (article, video, tutorial, documentation).

    Args:
        title: Title of the resource
        date: Publication date (ISO format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)
        resource_type: Type (article, video, tutorial, documentation, repository)
        description: Description of the content
        url: URL to the resource
        views: Number of views/reads (if available)
        engagement: Engagement metrics (e.g., "150 likes, 20 comments, 50 shares")

    Returns:
        Created activity draft information

    Example:
        "I published an article about Docker Compose best practices on my blog
        on June 1st, 2026. It got 5000 views"
    """
    try:
        activity = DockerResourceActivity(
            title=title,
            date=date,
            resource_type=resource_type,
            description=description or None,
            url=url or None,
            views=views if views > 0 else None,
            engagement=engagement or None,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "resources",
                activity.model_dump(exclude_none=True),
            )

        return {
            "success": True,
            "message": "Resource activity submitted successfully",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker resource activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_docker_event(
    title: str,
    date: str,
    event_type: str,
    description: str = "",
    url: str = "",
    attendees: int = 0,
    duration_hours: float = 0.0,
) -> Dict[str, Any]:
    """
    Submit a Docker Captain organized event (workshop, meetup, hackathon).

    Args:
        title: Title of the event
        date: Event date (ISO format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)
        event_type: Type of event (workshop, meetup, hackathon, training)
        description: Event description
        url: URL to event page or materials
        attendees: Number of participants
        duration_hours: Duration in hours

    Returns:
        Created activity draft information

    Example:
        "I organized a Docker workshop on June 3rd, 2026 with 30 attendees.
        It lasted 4 hours and covered containerization basics"
    """
    try:
        activity = DockerEventActivity(
            title=title,
            date=date,
            event_type=event_type,
            description=description or None,
            url=url or None,
            attendees=attendees if attendees > 0 else None,
            duration_hours=duration_hours if duration_hours > 0 else None,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "event",
                activity.model_dump(exclude_none=True),
            )

        return {
            "success": True,
            "message": "Event activity submitted successfully",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker event activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_docker_feedback(
    title: str,
    date: str,
    description: str = "",
    url: str = "",
    participants: int = 0,
    topics_discussed: str = "",
    feedback_provided: str = "",
) -> Dict[str, Any]:
    """
    Submit a Docker Captain feedback session activity.

    Args:
        title: Title of the feedback session
        date: Session date (ISO format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)
        description: Session description
        url: URL to notes or recording
        participants: Number of participants
        topics_discussed: Topics that were discussed
        feedback_provided: Summary of feedback provided

    Returns:
        Created activity draft information

    Example:
        "I participated in a Docker Desktop feedback session on June 4th
        with 5 other Captains. We discussed new features and UX improvements"
    """
    try:
        activity = DockerFeedbackSessionActivity(
            title=title,
            date=date,
            description=description or None,
            url=url or None,
            participants=participants if participants > 0 else None,
            topics_discussed=topics_discussed or None,
            feedback_provided=feedback_provided or None,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "feedbackSession",
                activity.model_dump(exclude_none=True),
            )

        return {
            "success": True,
            "message": "Feedback session submitted successfully",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker feedback activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


@mcp.tool()
def submit_docker_amplification(
    title: str,
    date: str,
    description: str = "",
    url: str = "",
    platform: str = "",
    reach: int = 0,
    engagement: str = "",
) -> Dict[str, Any]:
    """
    Submit a Docker Captain amplification activity (social media, community engagement).

    Args:
        title: Title of the amplification activity
        date: Activity date (ISO format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)
        description: What you amplified and how
        url: URL to post or content
        platform: Platform used (Twitter, LinkedIn, Blog, YouTube, etc.)
        reach: Estimated reach/impressions
        engagement: Engagement metrics (likes, retweets, comments, etc.)

    Returns:
        Created activity draft information

    Example:
        "I shared Docker's new features announcement on Twitter on June 6th,
        2026. Got 10000 impressions with 200 likes and 50 retweets"
    """
    try:
        activity = DockerAmplificationActivity(
            title=title,
            date=date,
            description=description or None,
            url=url or None,
            platform=platform or None,
            reach=reach if reach > 0 else None,
            engagement=engagement or None,
        )

        with AdvocuClient(ProgramType.DOCKER) as client:
            result = client.create_activity_draft(
                "amplification",
                activity.model_dump(exclude_none=True),
            )

        return {
            "success": True,
            "message": "Amplification activity submitted successfully",
            "data": result,
        }

    except AdvocuAuthError as e:
        return {"success": False, "error": "Authentication failed", "details": str(e)}
    except AdvocuAPIError as e:
        return {"success": False, "error": "API error", "details": str(e)}
    except Exception as e:
        logger.exception("Unexpected error submitting Docker amplification activity")
        return {"success": False, "error": "Unexpected error", "details": str(e)}


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
            "message": "GDE public speaking activity submitted successfully",
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
            "message": "GDE content creation activity submitted successfully",
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
            "message": "GDE workshop activity submitted successfully",
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
            "message": "GDE mentoring activity submitted successfully",
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
            "message": "GDE product feedback submitted successfully",
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
            "message": "GDE Googler interaction submitted successfully",
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
            "message": "GDE story submitted successfully",
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
def list_recent_activities(program: str = "gde", limit: int = 10) -> Dict[str, Any]:
    """
    List recent activities for a program.

    Args:
        program: Program type ("gde" or "docker")
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

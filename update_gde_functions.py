"""Script to update remaining GDE functions."""

# Read the server.py file
with open("src/server.py", "r") as f:
    content = f.read()

# Define replacements for mentoring
old_mentoring = '''    from .models import GDEMentoringActivity

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
                activity.model_dump(mode='json', exclude_none=True),
            )'''

new_mentoring = '''    from .models.gde import GDEMentoringActivity

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
            )'''

# Define replacements for product_feedback
old_product = '''    from .models import GDEProductFeedbackActivity

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
                activity.model_dump(mode='json', exclude_none=True),
            )'''

new_product = '''    from .models.gde import GDEProductFeedbackActivity

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
            )'''

# Define replacements for googler_interaction
old_interaction = '''    from .models import GDEInteractionActivity

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
                activity.model_dump(mode='json', exclude_none=True),
            )'''

new_interaction = '''    from .models.gde import GDEInteractionActivity

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
            )'''

# Define replacements for story
old_story = '''    from .models import GDEStoryActivity

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
                activity.model_dump(mode='json', exclude_none=True),
            )'''

new_story = '''    from .models.gde import GDEStoryActivity

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
            )'''

# Apply replacements
content = content.replace(old_mentoring, new_mentoring)
content = content.replace(old_product, new_product)
content = content.replace(old_interaction, new_interaction)
content = content.replace(old_story, new_story)

# Write back
with open("src/server.py", "w") as f:
    f.write(content)

print("✅ All GDE functions updated successfully!")

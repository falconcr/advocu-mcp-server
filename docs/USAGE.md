# Usage Guide

Learn how to use the Advocu MCP Server with conversational AI.

## Overview

The Advocu MCP Server enables you to submit activities naturally through conversation. Instead of filling out forms, just describe what you did, and the AI agent will structure and submit it for you.

## Basic Workflow

1. **Describe your activity** in natural language
2. **AI agent** identifies the activity type
3. **Server validates** and formats the data
4. **Activity is submitted** to Advocu
5. **Confirmation** is returned

## Conversational Examples

### Docker Captains Activities

#### Public Speaking

> **You:** I gave a talk at DockerCon 2026 in San Francisco on June 5th about "Advanced Docker Networking". There were about 500 people and it went really well!

> **Claude:** I'll submit that Docker Captain speaking activity for you.
>
> ✅ Public speaking activity submitted successfully!
> - Title: Advanced Docker Networking
> - Event: DockerCon 2026
> - Date: 2026-06-05
> - Location: San Francisco
> - Attendees: ~500

#### Resources (Articles/Videos)

> **You:** I published a blog post yesterday about Docker Compose best practices. It's on my blog at example.com/docker-compose and already has 2000 views.

> **Claude:** I'll submit that as a Docker Captain resource.
>
> ✅ Resource activity submitted!
> - Title: Docker Compose Best Practices
> - Type: Article
> - Views: 2000

#### Events (Workshops)

> **You:** I organized a 4-hour Docker workshop last week on June 3rd. We had 30 participants and covered containerization basics.

> **Claude:** Let me submit that workshop for you.
>
> ✅ Event activity submitted!
> - Date: 2026-06-03
> - Duration: 4 hours
> - Attendees: 30

#### Feedback Sessions

> **You:** I participated in a Docker Desktop feedback session today with 5 other Captains. We discussed new features and provided UX improvement suggestions.

> **Claude:** I'll record that feedback session.
>
> ✅ Feedback session submitted!

#### Amplification (Social Media)

> **You:** I shared Docker's new features announcement on Twitter yesterday. It got 10,000 impressions with 200 likes and 50 retweets.

> **Claude:** I'll submit that amplification activity.
>
> ✅ Amplification activity submitted!
> - Platform: Twitter
> - Reach: 10,000
> - Engagement: 200 likes, 50 retweets

### GDE Activities

#### Public Speaking

> **You:** I spoke at Google I/O Extended Madrid on May 15th about Firebase and Cloud Run. Around 200 developers attended.

> **Claude:** I'll submit that GDE speaking activity.
>
> ✅ GDE public speaking submitted!
> - Event: Google I/O Extended Madrid
> - Topics: Firebase, Cloud Run

#### Content Creation

> **You:** I published a video tutorial on YouTube about Cloud Functions yesterday. It's at youtube.com/watch?v=xyz and has 5,000 views so far.

> **Claude:** I'll submit that content creation activity.
>
> ✅ GDE content submitted!
> - Type: Video
> - Platform: YouTube
> - Views: 5,000

#### Workshops

> **You:** I ran a 3-hour Firebase workshop last Saturday for 25 developers. We built a real-time chat app.

> **Claude:** Let me record that workshop.
>
> ✅ GDE workshop submitted!
> - Duration: 3 hours
> - Attendees: 25
> - Topic: Firebase real-time chat

#### Mentoring

> **You:** I had two mentoring sessions this week, 2 hours each, helping new developers with Cloud Run deployment issues.

> **Claude:** I'll submit those mentoring sessions.
>
> ✅ GDE mentoring submitted!
> - Total hours: 4
> - Topic: Cloud Run deployment

#### Product Feedback

> **You:** I reported a bug in Cloud Run's autoscaling yesterday. It's causing issues with cold starts. Issue tracker: github.com/...

> **Claude:** I'll submit that product feedback.
>
> ✅ GDE product feedback submitted!
> - Product: Cloud Run
> - Type: Bug report
> - Focus: Autoscaling cold starts

#### Googler Interactions

> **You:** I had a meeting with the Firebase team yesterday to discuss new features for 2026. We covered real-time database improvements.

> **Claude:** I'll record that interaction.
>
> ✅ GDE Googler interaction submitted!
> - Team: Firebase
> - Topics: Real-time database improvements

#### Success Stories

> **You:** I published a case study about how a startup used Firebase to scale to 1M users. It's on the Google Cloud blog.

> **Claude:** I'll submit that success story.
>
> ✅ GDE story submitted!
> - Type: Case study
> - Impact: Startup scaling story

## Advanced Usage

### Listing Activities

> **You:** Show me my last 5 Docker Captain activities

> **Claude:** *Uses `list_recent_activities` tool*
>
> Here are your recent Docker Captain activities:
> 1. Public Speaking - DockerCon 2026 (June 5)
> 2. Blog Post - Docker Compose Guide (June 1)
> 3. Workshop - Containerization Basics (May 28)
> ...

### Batch Submission

> **You:** I need to submit multiple activities:
> 1. Talk at KubeCon on May 20th about K8s and Docker
> 2. Blog post published May 22nd about Docker security
> 3. Workshop on May 25th, 3 hours, 20 people

> **Claude:** I'll submit all three activities for you.
>
> ✅ Submitted 3 activities successfully!

### Editing/Corrections

> **You:** Actually, that talk had 600 attendees, not 500

> **Claude:** I'll update that activity with the correct number.

*(Note: Update functionality coming soon)*

## Tips for Best Results

### Be Specific About Dates

✅ **Good:**
- "yesterday" (if it's clearly yesterday)
- "June 5th, 2026"
- "last Tuesday"
- "May 15th"

❌ **Avoid:**
- "a while ago"
- "sometime last month"

### Include Key Metrics

For **speaking events**, mention:
- Attendees count
- Event name
- Location

For **content** (articles/videos), mention:
- Views/reads
- Platform
- Engagement (likes, comments)

For **workshops/events**, mention:
- Duration
- Number of participants
- Topics covered

### Provide URLs When Possible

Always helpful:
- Blog post URLs
- YouTube video links
- Slide deck URLs
- Event pages

### Use Natural Language

You don't need to format responses. Just talk naturally:

✅ "I gave a great talk yesterday about Docker to 100 people"

❌ "Activity type: speaking, date: 2026-06-07, attendees: 100"

## Common Questions

### Q: Can I submit activities from the past?

**A:** Yes! Just specify the date. "I spoke at a conference three months ago on March 15th..."

### Q: What if I don't remember exact numbers?

**A:** Use estimates. "around 50 people" or "approximately 1000 views" is fine.

### Q: Can I submit the same activity to both programs?

**A:** Yes, if you're both a GDE and Docker Captain and the activity is relevant to both. Submit separately to each program.

### Q: How do I know if submission succeeded?

**A:** Claude will confirm with a ✅ message and show you the submitted data.

### Q: Can I delete or edit submitted activities?

**A:** Currently, you can only create new activities through the MCP server. For edits/deletions, use the Advocu web portal directly.

## Error Handling

### Authentication Errors

If you see authentication errors:
1. Check your token in `.env`
2. Regenerate if expired
3. Restart the MCP server

### Rate Limit Errors

If you hit rate limits:
- Wait 1 minute
- The server automatically rate-limits (30 req/min)
- Batch submissions might hit limits with many activities

### Validation Errors

If data validation fails:
- AI will ask for clarification
- Provide the missing information
- Common issues: missing date, invalid URL format

## Integration with Other Tools

### With Calendar Apps

> "Check my calendar for last week and submit all the speaking events as activities"

*(Requires calendar integration - coming soon)*

### With Social Media

> "Scan my Twitter for Docker-related posts this month and submit amplification activities"

*(Requires social media integration - coming soon)*

## Next Steps

- [Setup Guide](SETUP.md) - Initial configuration
- [API Reference](API.md) - Technical details
- [Examples](EXAMPLES.md) - More example conversations

## Support

For questions or issues:
- GitHub Issues: [Report a problem](https://github.com/yourusername/advocu-mcp-server/issues)
- Documentation: [Full docs](https://github.com/yourusername/advocu-mcp-server/wiki)

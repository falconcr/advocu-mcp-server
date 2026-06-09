# Advocu MCP Server

A unified Model Context Protocol (MCP) server that enables **Google Developer Experts (GDEs)**, **Docker Captains**, and **Microsoft MVPs** to report their professional activities through conversational AI interfaces.

Built with [FastMCP](https://gofastmcp.com/) for seamless integration with Claude, Gemini, and other AI agents.

## Features

- 🎯 **Multi-Program Support**: Single server for GDE, Docker Captains, and MVP programs
- 🚀 **FastMCP-Powered**: Simple, Pythonic MCP server with automatic schema generation
- 🔒 **Rate Limiting**: Built-in rate limiting (30 req/min) to respect API limits
- ✅ **Type-Safe**: Pydantic models for robust data validation
- 🤖 **Conversational**: Natural language activity submission via AI agents
- 📊 **Activity Management**: Submit, list, and track activities across programs

## ⚠️ Important: Draft-Only Workflow

**The Advocu API only allows creating DRAFTS via API.** After creating an activity through the MCP server, you need to:

1. ✅ **Create draft** via MCP/Claude (automated)
2. 🌐 **Go to the portal** (manual step)
   - Docker Captains: https://hub.docker.com/
   - GDE: https://developers.google.com/community/experts
3. 📝 **Review the draft** (verify data is correct)
4. ✅ **Click "Submit"** to publish (manual step)

This is a limitation of the Advocu API, not the MCP server. All activities will be created as drafts that require manual publishing.

## Supported Activities

### Docker Captains
- 🎤 Public speaking (conferences, meetups)
- 📝 Resources (articles, videos, tutorials)
- 🎓 Events (workshops, hackathons)
- 💬 Feedback sessions
- 📢 Amplification (social media, community)

### Google Developer Experts (GDE)
- 🎤 Public speaking
- 📝 Content creation
- 🎓 Workshops
- 👨‍🏫 Mentoring
- 🔍 Product feedback
- 🤝 Googler interactions
- 📖 Success stories

### Microsoft MVPs
*(Coming soon - different API endpoint)*

## Quick Start

### 1. Prerequisites

- Python 3.10 or higher
- Access token from your program (GDE and/or Docker Captains)

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/advocu-mcp-server.git
cd advocu-mcp-server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

### 3. Configuration

Create a `.env` file with your tokens:

```bash
cp .env.example .env
```

Edit `.env` and add your tokens:

```env
# For GDEs
GDE_ACCESS_TOKEN=your_gde_token_here

# For Docker Captains
DOCKER_ACCESS_TOKEN=your_docker_token_here
```

#### How to Get Your Token

**For Google Developer Experts:**
1. Visit https://devlibrary.advocu.com/
2. Go to Settings → Integrations → API
3. Click "Generate your token"
4. Copy the token

**For Docker Captains:**
1. Visit the Docker Captains portal
2. Go to Settings → Integrations → API
3. Click "Generate your token"
4. Copy the token

### 4a. Configure Claude Desktop (Optional)

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on Mac):

```json
{
  "mcpServers": {
    "advocu": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "/path/to/advocu-mcp-server",
      "env": {
        "PYTHONPATH": "/path/to/advocu-mcp-server"
      }
    }
  }
}
```

### 4b. Configure Claude Code CLI (Recommended)

The project already includes a `.mcp.json` file for Claude Code CLI. Just verify it's configured:

```bash
# Check server status
claude mcp list

# You should see:
# advocu: .../venv/bin/python -m src.server - ✓ Connected
```

If you need to reconfigure, edit `.mcp.json`:

```json
{
  "mcpServers": {
    "advocu": {
      "type": "stdio",
      "command": "/home/falcon/advocu-mcp-server/venv/bin/python",
      "args": ["-m", "src.server"],
      "cwd": "/home/falcon/advocu-mcp-server",
      "env": {
        "PYTHONPATH": "/home/falcon/advocu-mcp-server"
      }
    }
  }
}
```

**Note:** Update the paths to match your installation directory.

### 5. Usage

Start chatting naturally with Claude (Desktop or CLI):

**Examples:**

> "I gave a talk about Docker networking at KubeCon on June 5th, 2026 with 500 attendees"

> "I published a tutorial on Cloud Run yesterday with 3000 views"

> "I organized a workshop on Kubernetes last week with 30 people for 4 hours"

Claude will automatically use the appropriate MCP tools to submit your activities.

## Available Tools

### Docker Captains Tools

- `submit_docker_public_speaking` - Submit speaking engagements
- `submit_docker_resource` - Submit articles, videos, tutorials
- `submit_docker_event` - Submit organized events
- `submit_docker_feedback` - Submit feedback sessions
- `submit_docker_amplification` - Submit social media amplification

### GDE Tools

- `submit_gde_public_speaking` - Submit speaking engagements
- `submit_gde_content` - Submit content creation
- `submit_gde_workshop` - Submit workshops
- `submit_gde_mentoring` - Submit mentoring sessions
- `submit_gde_product_feedback` - Submit product feedback
- `submit_gde_googler_interaction` - Submit Googler interactions
- `submit_gde_story` - Submit success stories

### Utility Tools

- `list_recent_activities` - List recent activities

## Usage Examples

### Docker Captains Examples

#### Example 1: Submit a Video Tutorial

**You say:**
> "I just published a video tutorial on YouTube about Docker Multi-Stage Builds. It was posted on June 1st, 2026, and already has 2500 views, 150 likes, and 45 comments. Here's the link: https://youtube.com/watch?v=example"

**Claude will:**
- Use `submit_docker_resource` tool
- Extract: title, date, URL, metrics (views, likes, comments)
- Content type: "Video"
- Create draft in Advocu

**Result:**
```
✅ Resource activity DRAFT created successfully
Draft ID: abc123...
⚠️ Go to https://hub.docker.com/ to review and click 'Submit' to publish
```

#### Example 2: Submit a Blog Post

**You say:**
> "I wrote a blog post titled 'Docker Security Best Practices 2026' yesterday. It's published at https://myblog.com/docker-security and currently has 5000 views and 200 shares"

**Claude creates:**
- Title: "Docker Security Best Practices 2026"
- Content type: "Blog post"
- Metrics: 5000 views, 200 shares
- Date: 2026-06-07 (yesterday)

#### Example 3: Submit a Conference Talk

**You say:**
> "I gave a presentation at DockerCon 2026 titled 'The Future of Container Orchestration' on June 5th. It was in-person, lasted 45 minutes, and had approximately 500 attendees. Slides are at https://slides.com/my-talk"

**Claude creates:**
- Tool: `submit_docker_public_speaking`
- Format: "In-person"
- Duration: 45 minutes
- Attendees: 500

#### Example 4: Submit a Workshop

**You say:**
> "I organized a Docker workshop for beginners last week on June 3rd. It was a virtual event that lasted 4 hours (2-4 hours duration) with 30 participants. We covered Docker basics and best practices"

**Claude creates:**
- Tool: `submit_docker_event`
- Event type: "Workshop"
- Format: "Virtual"
- Duration: "2-4 hours"
- Attendees: 30
- Tags: Docker, workshop, beginners

#### Example 5: Submit Social Media Amplification

**You say:**
> "I shared Docker's new release announcement on Twitter and LinkedIn yesterday. The post got 15,000 impressions, 250 likes, and 80 retweets"

**Claude creates:**
- Tool: `submit_docker_amplification`
- Type: "Social media post"
- Channels: Twitter, LinkedIn
- Metrics: 15000 impressions, 250 likes, 80 shares

#### Example 6: Submit Feedback Session

**You say:**
> "I had a feedback call with Sarah from the Docker team on June 4th about Docker Desktop's new networking features. We discussed UX improvements for about 45 minutes via Zoom"

**Claude creates:**
- Tool: `submit_docker_feedback`
- Docker representative: "Sarah"
- Mode: "Direct call"
- Time spent: 45 minutes

### GDE Examples

#### Example 1: Submit a Blog Post/Article

**You say:**
> "I published an article about Cloud Run optimization on Medium yesterday. It's at https://medium.com/@me/cloud-run-optimization and has 3500 views, 180 claps, and 25 comments"

**Claude creates:**
- Tool: `submit_gde_content`
- Content type: "Blog post"
- Google technology: "Cloud Run"
- Metrics: 3500 views, 180 likes, 25 comments

#### Example 2: Submit a Conference Presentation

**You say:**
> "I presented at Google I/O Extended 2026 on June 8th. My talk was about 'Building Scalable Apps with Firebase' and was in-person with around 300 attendees. It lasted 50 minutes"

**Claude creates:**
- Tool: `submit_gde_public_speaking`
- Event name: "Google I/O Extended 2026"
- Google technology: "Firebase"
- Format: "In-person"
- Duration: 50 minutes
- Attendees: 300

#### Example 3: Submit a Workshop/Training

**You say:**
> "I conducted a hands-on workshop on Flutter development last Saturday, June 6th. It was a full-day workshop (8 hours) with 25 developers, and we built 3 complete apps together"

**Claude creates:**
- Tool: `submit_gde_workshop`
- Topic: "Flutter development"
- Duration: "Full day"
- Attendees: 25
- Format: "In-person" or "Virtual" (based on context)

#### Example 4: Submit Mentoring Activity

**You say:**
> "I mentored 5 junior developers this week on Google Cloud architecture best practices. We had 3 sessions totaling about 6 hours"

**Claude creates:**
- Tool: `submit_gde_mentoring`
- Topic: "Google Cloud architecture"
- Number of people: 5
- Time spent: 6 hours (360 minutes)

#### Example 5: Submit Product Feedback

**You say:**
> "I provided feedback to the Google Cloud team on June 7th about Cloud Functions cold start performance. I shared detailed metrics and suggestions during a 1-hour call with the product manager"

**Claude creates:**
- Tool: `submit_gde_product_feedback`
- Product: "Cloud Functions"
- Feedback: "Cold start performance improvements"
- Mode: "Direct call"
- Time spent: 60 minutes

#### Example 6: Submit Googler Interaction

**You say:**
> "I collaborated with a Google engineer named Alex on improving the TensorFlow documentation on June 5th. We had a 2-hour video call to review my proposed changes"

**Claude creates:**
- Tool: `submit_gde_googler_interaction`
- Googler name: "Alex"
- Topic: "TensorFlow documentation"
- Type: "Collaboration"
- Duration: 2 hours

#### Example 7: Submit a Success Story

**You say:**
> "One of my mentees just got hired at a major tech company after following my Google Cloud training program. They went from zero cloud experience to GCP certified in 6 months"

**Claude creates:**
- Tool: `submit_gde_story`
- Story: Mentee's success with Google Cloud
- Impact: Career transformation, certification
- Technology: Google Cloud Platform

### Listing Your Activities

**You say:**
> "Show me my last 10 Docker Captain activities"

**Claude will:**
- Use `list_recent_activities` tool
- Display your recent submissions with titles, dates, and types

### Tips for Better Results

1. **Be specific**: Include dates, numbers, and URLs when available
2. **Mention the platform**: "on YouTube", "on Medium", "at KubeCon"
3. **Include metrics**: Views, attendees, duration, impressions
4. **Specify format**: "in-person", "virtual", "hybrid"
5. **Natural language**: Just talk normally, Claude will extract the data

### What Happens After Submission

1. ✅ Claude creates the draft via API
2. 📧 You receive the draft ID
3. 🌐 You go to the portal:
   - Docker: https://hub.docker.com/
   - GDE: https://developers.google.com/community/experts
4. 📝 Review the draft (verify all data is correct)
5. ✅ Click "Submit" to publish

**Important:** The API only creates drafts. The final "Submit" must be done manually in the portal.

## Development

### Project Structure

```
advocu-mcp-server/
├── src/
│   ├── __init__.py
│   ├── server.py              # Main FastMCP server
│   ├── config.py              # Configuration management
│   ├── clients/
│   │   ├── __init__.py
│   │   └── advocu.py          # Advocu API client
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py            # Base models
│   │   ├── docker.py          # Docker Captains models
│   │   └── gde.py             # GDE models
│   └── utils/
│       ├── __init__.py
│       └── rate_limiter.py    # Rate limiting
├── tests/                      # Tests (coming soon)
├── pyproject.toml             # Project metadata
├── .env.example               # Environment template
└── README.md                  # This file
```

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .
```

## API Reference

### Advocu API

**Base URLs:**
- GDE: `https://api.advocu.com/personal-api/v1/gde`
- Docker Captains: `https://api.advocu.com/personal-api/v1/dockercaptains`

**Authentication:**
```
Authorization: Bearer {access-token}
Content-Type: application/json
```

**Rate Limits:**
- 30 requests per minute per user
- Returns HTTP 429 if exceeded

## Troubleshooting

### Authentication Failed

**Error:** `Authentication failed. Please check your access token.`

**Solution:**
1. Verify your token in `.env` is correct
2. Check if the token has expired
3. Generate a new token from the program portal

### Rate Limit Exceeded

**Error:** `Rate limit exceeded. Please wait before making more requests.`

**Solution:**
- The server has built-in rate limiting
- Wait ~1 minute before making more requests
- The rate limiter automatically handles this

### Program Not Configured

**Error:** `No access token configured for {program}`

**Solution:**
1. Add the appropriate token to `.env`
2. Restart the MCP server
3. Verify the token variable name matches

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

- Issues: https://github.com/yourusername/advocu-mcp-server/issues
- Documentation: https://github.com/yourusername/advocu-mcp-server/wiki

## Acknowledgments

- Built with [FastMCP](https://gofastmcp.com/) by Prefect
- Powered by [Advocu API](https://www.advocu.com/)

## Roadmap

- [ ] Microsoft MVP API integration
- [ ] Activity templates and suggestions
- [ ] Batch activity submission
- [ ] Activity analytics and insights
- [ ] Multi-user support
- [ ] Web dashboard
- [ ] Docker container for easy deployment

---

Made with ❤️ for the developer community

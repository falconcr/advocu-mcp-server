# Claude Code CLI Setup Guide

Quick guide to get the Advocu MCP Server running with Claude Code (CLI).

## Prerequisites

- Claude Code CLI installed
- Python 3.10 or higher
- Docker Captain and/or GDE API token

## Setup (5 minutes)

### 1. Clone and Install

```bash
cd /home/falcon/advocu-mcp-server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### 2. Configure Your Token

```bash
cp .env.example .env
nano .env  # or use your preferred editor
```

Add your token(s):
```env
DOCKER_ACCESS_TOKEN=your_docker_token_here
GDE_ACCESS_TOKEN=your_gde_token_here
```

**How to get your token:**
- **Docker Captains**: https://hub.docker.com/ → Settings → Integrations → API
- **GDE**: https://devlibrary.advocu.com/ → Settings → Integrations → API

### 3. Verify MCP Server Connection

```bash
claude mcp list
```

You should see:
```
advocu: .../venv/bin/python -m src.server - ✓ Connected
```

## Usage

Now you can use Claude Code naturally! Just start a conversation:

### Example 1: Submit a Talk

```
I gave a talk titled "Docker Networking Deep Dive" at KubeCon 2026
on June 5th, 2026. It was in-person, lasted 45 minutes, and had
about 500 attendees.
```

Claude will automatically:
1. Extract the information
2. Call `submit_docker_public_speaking`
3. Create the draft in Advocu
4. Tell you to go to the portal to publish

### Example 2: Submit a Blog Post

```
I published a blog post about Kubernetes security yesterday.
It's at https://myblog.com/k8s-security and has 3000 views.
```

### Example 3: List Recent Activities

```
Show me my recent Docker Captain activities
```

## Important: Draft-Only Workflow

⚠️ **The Advocu API only creates DRAFTS**. After Claude creates the draft, you need to:

1. ✅ Draft created by Claude (automatic)
2. 🌐 Go to the portal:
   - Docker Captains: https://hub.docker.com/
   - GDE: https://developers.google.com/community/experts
3. 📝 Review the draft
4. ✅ Click "Submit" to publish (manual)

This is an API limitation, not an MCP server limitation.

## Available Tools

### Docker Captains (5 tools)
- `submit_docker_public_speaking` - Talks, conferences, meetups
- `submit_docker_resource` - Articles, videos, tutorials
- `submit_docker_event` - Workshops, hackathons, trainings
- `submit_docker_feedback` - Feedback sessions with Docker team
- `submit_docker_amplification` - Social media amplification

### GDE (7 tools)
- `submit_gde_public_speaking` - Presentations
- `submit_gde_content` - Content creation
- `submit_gde_workshop` - Workshops
- `submit_gde_mentoring` - Mentoring sessions
- `submit_gde_product_feedback` - Product feedback
- `submit_gde_googler_interaction` - Googler interactions
- `submit_gde_story` - Success stories

### Utility (1 tool)
- `list_recent_activities` - View recent submissions

## Troubleshooting

### Server Not Connected

```bash
# Check if .mcp.json exists
cat .mcp.json

# Restart Claude Code
# (exit and restart your terminal/Claude Code session)

# Check connection again
claude mcp list
```

### Authentication Failed

1. Verify your token in `.env` is correct
2. Check if token expired (generate new one from portal)
3. Make sure token is for the correct program (Docker vs GDE)

### Rate Limit Exceeded

Wait ~60 seconds. The server has built-in rate limiting (30 req/min).

## Configuration Files

- `.mcp.json` - MCP server configuration (committed to git)
- `.env` - Your API tokens (NOT committed, keep secret)
- `src/server.py` - Main FastMCP server with all tools

## Need Help?

- Check `README.md` for full documentation
- Review `FINAL_SUMMARY.md` for project details
- Open an issue on GitHub

---

**Time to first activity**: ~5 minutes
**Time saved per activity**: ~60-80% (vs manual web form)

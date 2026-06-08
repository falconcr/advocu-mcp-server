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

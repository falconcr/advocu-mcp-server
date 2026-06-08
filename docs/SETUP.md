# Setup Guide

Complete setup guide for the Advocu MCP Server.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation](#installation)
3. [Getting Your API Tokens](#getting-your-api-tokens)
4. [Configuration](#configuration)
5. [Client Integration](#client-integration)
6. [Verification](#verification)

## System Requirements

- **Python**: 3.10 or higher
- **Operating System**: macOS, Linux, or Windows
- **Memory**: 256MB minimum
- **Network**: Internet connection for API calls

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/advocu-mcp-server.git
cd advocu-mcp-server
```

### Step 2: Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -e .
```

Or for development:
```bash
pip install -e ".[dev]"
```

## Getting Your API Tokens

### For Google Developer Experts (GDE)

1. **Login to Advocu**
   - Visit: https://devlibrary.advocu.com/
   - Sign in with your Google account

2. **Navigate to Settings**
   - Click on your profile (top right)
   - Select "Settings"

3. **Go to Integrations**
   - In the left sidebar, click "Integrations"
   - Select "API"

4. **Generate Token**
   - Click "Generate your token" button
   - Copy the token immediately (you won't see it again)

5. **Save the Token**
   - Store it securely (password manager recommended)
   - You'll need it for the `.env` file

### For Docker Captains

1. **Login to Docker Captains Portal**
   - Visit the Docker Captains dashboard
   - Sign in with your Docker credentials

2. **Navigate to Settings**
   - Click on "Settings" in the navigation menu

3. **Access Integrations**
   - Select "Integrations" → "API"

4. **Generate Token**
   - Click "Generate your token"
   - Copy the token

5. **Save the Token**
   - Store securely for use in configuration

### For Microsoft MVPs

*(Coming soon - different API endpoint)*

## Configuration

### Step 1: Create Environment File

```bash
cp .env.example .env
```

### Step 2: Edit Configuration

Open `.env` in your text editor and add your tokens:

```env
# ===== Google Developer Experts =====
# Get from: https://devlibrary.advocu.com/ → Settings → Integrations → API
GDE_ACCESS_TOKEN=your_actual_gde_token_here

# ===== Docker Captains =====
# Get from: Docker Captains portal → Settings → Integrations → API
DOCKER_ACCESS_TOKEN=your_actual_docker_token_here

# ===== Optional Settings =====
LOG_LEVEL=INFO  # Options: DEBUG, INFO, WARNING, ERROR
```

**Important Notes:**
- Replace `your_actual_*_token_here` with your real tokens
- Don't share your `.env` file (it's in `.gitignore`)
- Tokens don't expire automatically but can be revoked
- You only need tokens for programs you're part of

### Step 3: Verify Configuration

Test your configuration:

```bash
python -c "from src.config import settings; print('✅ Config loaded:', settings.has_program_configured('gde'))"
```

## Client Integration

### Claude Desktop

#### Location of Config File

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

#### Configuration

Edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "advocu": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "/absolute/path/to/advocu-mcp-server",
      "env": {
        "PYTHONPATH": "/absolute/path/to/advocu-mcp-server"
      }
    }
  }
}
```

**Replace `/absolute/path/to/` with your actual path!**

**To get your absolute path:**

```bash
# In the advocu-mcp-server directory
pwd
```

#### Restart Claude Desktop

After editing the config:
1. Quit Claude Desktop completely
2. Relaunch Claude Desktop
3. The MCP server will auto-start

### Other MCP Clients

#### Gemini (Google AI Studio)

*(Coming soon)*

#### Custom Integration

For custom clients using the MCP protocol:

```python
from mcp import ClientSession
from mcp.client.stdio import stdio_client

# Connect to the server
async with stdio_client(
    command="python",
    args=["-m", "src.server"],
    cwd="/path/to/advocu-mcp-server"
) as (read, write):
    async with ClientSession(read, write) as session:
        # Initialize
        await session.initialize()

        # List available tools
        tools = await session.list_tools()
        print(tools)
```

## Verification

### Test the Server Directly

Run the server in standalone mode:

```bash
python -m src.server
```

You should see:
```
INFO - Starting Advocu MCP Server
INFO - Loaded tools: 13
```

Press `Ctrl+C` to stop.

### Test with Claude Desktop

1. Open Claude Desktop
2. Start a new conversation
3. Type: "List my recent Docker Captain activities"
4. Claude should recognize and use the MCP tools

### Verify Tools are Available

In Claude Desktop, you can ask:
> "What tools do you have available for submitting activities?"

Claude should list all the Advocu tools.

### Test Submission

Try a simple submission:
> "I want to test the system. Create a test speaking activity for Docker Captains on June 1st, 2026 titled 'Test Talk'"

Claude will use the tool and you'll see the result.

## Troubleshooting

### Problem: "Module not found" error

**Solution:**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall
pip install -e .
```

### Problem: "No access token configured"

**Solution:**
1. Check your `.env` file exists
2. Verify token variable names match exactly
3. Ensure no extra spaces or quotes around tokens
4. Try regenerating the token

### Problem: Claude Desktop doesn't see the tools

**Solution:**
1. Verify the path in `claude_desktop_config.json` is absolute
2. Check the config file has valid JSON syntax
3. Restart Claude Desktop completely
4. Check Claude Desktop logs for errors

### Problem: "Authentication failed"

**Solution:**
1. Token might be invalid or expired
2. Regenerate token from the portal
3. Update `.env` with new token
4. Restart the MCP server

## Next Steps

- [Usage Guide](USAGE.md) - Learn how to use the server
- [API Reference](API.md) - Detailed API documentation
- [Examples](EXAMPLES.md) - Example conversations and workflows

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the logs (set `LOG_LEVEL=DEBUG` in `.env`)
3. Open an issue on GitHub with details

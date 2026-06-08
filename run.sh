#!/bin/bash
# Quick start script for Advocu MCP Server

set -e

echo "🚀 Starting Advocu MCP Server..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
if [ ! -f "venv/.installed" ]; then
    echo "📥 Installing dependencies..."
    pip install -e .
    touch venv/.installed
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "📝 Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "❗ Please edit .env and add your API tokens before running again."
    echo "   Then run: ./run.sh"
    exit 1
fi

# Run the server
echo "✅ Starting MCP server..."
python -m src.server

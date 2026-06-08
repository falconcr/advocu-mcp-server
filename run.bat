@echo off
REM Quick start script for Advocu MCP Server (Windows)

echo Starting Advocu MCP Server...

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
if not exist "venv\.installed" (
    echo Installing dependencies...
    pip install -e .
    echo. > venv\.installed
)

REM Check if .env exists
if not exist ".env" (
    echo Warning: .env file not found!
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo Please edit .env and add your API tokens before running again.
    echo Then run: run.bat
    pause
    exit /b 1
)

REM Run the server
echo Starting MCP server...
python -m src.server

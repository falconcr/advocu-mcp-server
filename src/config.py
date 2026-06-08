"""Configuration management for Advocu MCP Server."""

import os
from enum import Enum
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class ProgramType(str, Enum):
    """Supported Advocu programs."""
    GDE = "gde"
    DOCKER = "dockercaptains"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # API Tokens
    gde_access_token: Optional[str] = None
    docker_access_token: Optional[str] = None
    mvp_access_token: Optional[str] = None
    mvp_user_profile_id: Optional[str] = None

    # API Configuration
    advocu_base_url: str = "https://api.advocu.com/personal-api/v1"
    rate_limit_requests: int = 30
    rate_limit_period: int = 60  # seconds

    # Logging
    log_level: str = "INFO"

    def get_token(self, program: ProgramType) -> Optional[str]:
        """Get access token for a specific program."""
        if program == ProgramType.GDE:
            return self.gde_access_token
        elif program == ProgramType.DOCKER:
            return self.docker_access_token
        return None

    def has_program_configured(self, program: ProgramType) -> bool:
        """Check if a program is configured with a valid token."""
        token = self.get_token(program)
        return token is not None and len(token) > 0


# Global settings instance
settings = Settings()

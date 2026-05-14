"""Centralised settings loaded from environment / .env file."""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "/app/.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Google Calendar auth — provide either JSON content or a file path
    google_token_json: str | None = None
    google_token_path: str | None = None
    google_credentials_json: str | None = None
    google_credentials_path: str | None = None

    # Target calendars
    mfc_calendar_url: str = "https://share.myfreecams.com/RinCity/calendar"
    google_calendar_id: str = "primary"

    # Sync window
    sync_start_date: str | None = None
    sync_months: int = 2
    sleep_interval: str | None = None  # e.g. "30m", "12h", "1d"

    # SMTP / email notifications
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_from: str | None = None
    smtp_to: str | None = None
    smtp_use_starttls: bool = True
    smtp_subject_prefix: str = "RinCity Calendar Sync"

    # Notification triggers
    notify_on_success: bool = False
    notify_on_changes: bool = True
    notify_on_error: bool = True

    # Misc
    dry_run: bool = False
    preview_email_html_path: str | None = None


settings = Settings()

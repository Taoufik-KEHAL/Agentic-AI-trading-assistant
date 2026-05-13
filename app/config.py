"""Centralized application configuration."""

from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-driven settings."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = "development"
    log_level: str = "INFO"

    groq_api_key: str = Field(default="", alias="GROQ_API_KEY")
    groq_model: str = Field(default="llama-3.1-70b-versatile", alias="GROQ_MODEL")

    binance_api_key: str = Field(default="", alias="BINANCE_API_KEY")
    binance_api_secret: str = Field(default="", alias="BINANCE_API_SECRET")
    binance_base_url: str = Field(default="https://api.binance.com", alias="BINANCE_BASE_URL")

    database_url: str = Field(default="duckdb:///./trading_assistant.duckdb", alias="DATABASE_URL")

    symbols: str = Field(default="BTCUSDT,ETHUSDT,SOLUSDT", alias="SYMBOLS")
    timeframe: str = Field(default="1m", alias="TIMEFRAME")

    max_risk_per_trade: float = Field(default=0.01, alias="MAX_RISK_PER_TRADE")
    max_daily_loss: float = Field(default=0.03, alias="MAX_DAILY_LOSS")
    max_exposure: float = Field(default=0.2, alias="MAX_EXPOSURE")

    @property
    def tracked_symbols(self) -> List[str]:
        return [symbol.strip().upper() for symbol in self.symbols.split(",") if symbol.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()

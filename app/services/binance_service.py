"""Binance REST and websocket adapters."""

from __future__ import annotations

from typing import Any, Dict, List

import httpx

from app.config import Settings


class BinanceService:
    """Lightweight service to ingest market data from Binance Spot API."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.base_url = settings.binance_base_url.rstrip("/")

    async def get_klines(self, symbol: str, interval: str, limit: int = 200) -> List[List[Any]]:
        """Fetch historical OHLCV candle data."""
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{self.base_url}/api/v3/klines", params=params)
            response.raise_for_status()
            return response.json()

    async def get_order_book(self, symbol: str, limit: int = 100) -> Dict[str, Any]:
        """Fetch order book snapshot."""
        params = {"symbol": symbol, "limit": limit}
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{self.base_url}/api/v3/depth", params=params)
            response.raise_for_status()
            return response.json()

    def websocket_stream_name(self, symbol: str, interval: str) -> str:
        """Build websocket stream name for kline updates."""
        return f"{symbol.lower()}@kline_{interval}"

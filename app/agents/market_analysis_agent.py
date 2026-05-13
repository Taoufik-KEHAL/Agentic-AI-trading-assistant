"""Market analysis agent implementation."""

from __future__ import annotations

from typing import Any, Dict

import pandas as pd
import pandas_ta as ta


class MarketAnalysisAgent:
    """Analyzes trend, volatility, and market regime from OHLCV data."""

    def analyze(self, ohlcv: pd.DataFrame) -> Dict[str, Any]:
        frame = ohlcv.copy()

        frame["rsi"] = ta.rsi(frame["close"], length=14)
        macd = ta.macd(frame["close"], fast=12, slow=26, signal=9)
        frame["macd"] = macd["MACD_12_26_9"]
        frame["macd_signal"] = macd["MACDs_12_26_9"]
        frame["ema_20"] = ta.ema(frame["close"], length=20)
        frame["sma_20"] = ta.sma(frame["close"], length=20)
        frame["atr"] = ta.atr(frame["high"], frame["low"], frame["close"], length=14)
        bbands = ta.bbands(frame["close"], length=20, std=2)
        frame["bb_low"] = bbands["BBL_20_2.0"]
        frame["bb_high"] = bbands["BBU_20_2.0"]
        frame["vol_sma_20"] = ta.sma(frame["volume"], length=20)

        latest = frame.dropna().iloc[-1]
        trend = "bullish" if latest["ema_20"] > latest["sma_20"] else "bearish"
        volatility = "high" if latest["atr"] / latest["close"] > 0.02 else "normal"
        regime = self._detect_regime(latest)

        return {
            "trend": trend,
            "volatility": volatility,
            "market_regime": regime,
            "indicators": {
                "rsi": float(latest["rsi"]),
                "macd": float(latest["macd"]),
                "macd_signal": float(latest["macd_signal"]),
                "ema_20": float(latest["ema_20"]),
                "sma_20": float(latest["sma_20"]),
                "atr": float(latest["atr"]),
            },
        }

    def _detect_regime(self, latest: pd.Series) -> str:
        if latest["rsi"] > 60 and latest["macd"] > latest["macd_signal"]:
            return "trend"
        if latest["rsi"] < 40 and latest["macd"] < latest["macd_signal"]:
            return "trend"
        if latest["atr"] > 0 and (latest["bb_high"] - latest["bb_low"]) / latest["atr"] > 6:
            return "volatile"
        return "range"

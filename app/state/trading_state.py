"""Shared typed state for LangGraph orchestration."""

from typing import Any, Dict, List, Literal, TypedDict


class AgentDecision(TypedDict, total=False):
    agent: str
    decision: str
    confidence: float
    details: Dict[str, Any]


class TradingState(TypedDict, total=False):
    symbol: str
    timeframe: str
    market_data: Dict[str, Any]
    indicators: Dict[str, float]
    market_regime: Literal["trend", "range", "volatile", "unknown"]
    decisions: List[AgentDecision]
    risk_approved: bool
    errors: List[str]

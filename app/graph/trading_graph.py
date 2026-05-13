"""LangGraph workflow skeleton for multi-agent orchestration."""

from __future__ import annotations

from langgraph.graph import END, StateGraph

from app.state.trading_state import TradingState


def market_analysis_node(state: TradingState) -> TradingState:
    return state


def risk_management_node(state: TradingState) -> TradingState:
    return state


def strategy_node(state: TradingState) -> TradingState:
    return state


def execution_node(state: TradingState) -> TradingState:
    return state


def route_after_risk(state: TradingState) -> str:
    return "strategy" if state.get("risk_approved") else "end"


def build_trading_graph():
    workflow = StateGraph(TradingState)

    workflow.add_node("market_analysis", market_analysis_node)
    workflow.add_node("risk", risk_management_node)
    workflow.add_node("strategy", strategy_node)
    workflow.add_node("execution", execution_node)

    workflow.set_entry_point("market_analysis")
    workflow.add_edge("market_analysis", "risk")
    workflow.add_conditional_edges("risk", route_after_risk, {"strategy": "strategy", "end": END})
    workflow.add_edge("strategy", "execution")
    workflow.add_edge("execution", END)

    return workflow.compile()

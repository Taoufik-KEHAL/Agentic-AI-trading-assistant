# Remaining Steps / Open Issues

This file tracks the remaining implementation work after the initial scaffold.

## EPIC-1: Core Multi-Agent Workflow Completion

### Issue 1 — Implement RiskManagementAgent (deterministic gate)
**Priority:** P0
**Why:** No trade should progress unless deterministic risk checks pass.

**Acceptance Criteria**
- Validate max risk per trade, max daily loss, max exposure, and symbol whitelist.
- Reject malformed or LLM-derived direct execution payloads.
- Return structured risk report and `risk_approved: bool`.
- Unit tests for pass/fail scenarios.

---

### Issue 2 — Implement StrategyAgent
**Priority:** P0

**Acceptance Criteria**
- Select strategy by market regime (`trend`, `range`, `volatile`).
- Emit deterministic action proposal schema (`side`, `entry`, `stop_loss`, `take_profit`, `size`).
- No direct broker action in this agent.
- Unit tests for each regime.

---

### Issue 3 — Implement ExecutionAgent (paper trading only)
**Priority:** P0

**Acceptance Criteria**
- Execute only if `risk_approved` and schema-valid order intent exists.
- Persist simulated fills and slippage assumptions.
- Support symbols: BTC/USDT, ETH/USDT, SOL/USDT.
- Unit + integration tests.

---

### Issue 4 — Implement PortfolioAgent
**Priority:** P1

**Acceptance Criteria**
- Track open positions, realized/unrealized PnL, exposure by symbol.
- Expose daily loss and drawdown metrics consumed by risk agent.
- Persist state to DB.

---

### Issue 5 — Implement SupervisorAgent + full LangGraph routing
**Priority:** P1

**Acceptance Criteria**
- Add retries/fallback edges on transient failures.
- Add memory persistence/checkpointing.
- Add graph visualization artifact export.
- Integration tests for end-to-end state transitions.

---

## EPIC-2: Market Data (Realtime + Historical)

### Issue 6 — WebSocket stream consumer
**Priority:** P0

**Acceptance Criteria**
- Subscribe to klines and book-ticker/order-book deltas.
- Reconnect with exponential backoff.
- Store normalized events in DB.

### Issue 7 — Historical OHLCV ingestion pipeline
**Priority:** P1

**Acceptance Criteria**
- Scheduled backfill by symbol/timeframe.
- Idempotent upsert semantics.
- Data quality checks and gap detection.

---

## EPIC-3: Persistence Layer

### Issue 8 — DuckDB/Postgres repository layer
**Priority:** P0

**Acceptance Criteria**
- Create models/tables: candles, signals, decisions, trades, logs, backtest_results.
- Add migrations/init scripts.
- Repository interfaces + tests.

---

## EPIC-4: Backtesting Engine

### Issue 9 — Historical simulation engine
**Priority:** P1

**Acceptance Criteria**
- Run strategy on historical candles.
- Compute Sharpe, max drawdown, win rate, trade logs.
- API endpoint for run + result retrieval.

---

## EPIC-5: API + UI

### Issue 10 — FastAPI endpoints
**Priority:** P0

**Acceptance Criteria**
- `/analysis`, `/decisions`, `/portfolio`, `/risk`, `/backtests` endpoints.
- Pydantic request/response schemas.
- Error handling and structured logging middleware.

### Issue 11 — Streamlit dashboard
**Priority:** P1

**Acceptance Criteria**
- Live prices, indicators, active signals, portfolio, risk metrics, agent logs.
- Polling/subscription model with graceful failure states.

---

## EPIC-6: LLM Integration (Groq only)

### Issue 12 — Groq service adapter
**Priority:** P0

**Acceptance Criteria**
- Support configured models: `llama-3`, `deepseek-r1-distill`, `qwen`.
- Timeout/retry policy and response validation.
- Ensure no direct execution can be triggered by generated text.

---

## EPIC-7: Quality / DevOps

### Issue 13 — CI checks
**Priority:** P1

**Acceptance Criteria**
- Run `ruff`, `black --check`, and `pytest` in CI.
- Failing tests block merges.

### Issue 14 — Observability
**Priority:** P1

**Acceptance Criteria**
- Structured logs across agents/services.
- Basic metrics and health probes.

---

## Notes
- Inline review comments were not available in the provided context. If you share exact comment text, each can be mapped to the issue list above or fixed directly in code.

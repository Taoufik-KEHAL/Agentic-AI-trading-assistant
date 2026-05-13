# Agentic AI Trading Assistant

Production-oriented, modular multi-agent crypto trading analysis platform.

## Current Increment (Phase 1)
- Project scaffolding with layered architecture
- Environment-based configuration
- Binance REST ingestion service
- LangGraph orchestration skeleton
- First `MarketAnalysisAgent` with technical indicators

## Run
```bash
pip install -r requirements.txt
uvicorn app.api.main:app --reload
pytest
```

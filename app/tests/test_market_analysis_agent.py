import pandas as pd

from app.agents.market_analysis_agent import MarketAnalysisAgent


def test_market_analysis_outputs_expected_keys() -> None:
    rows = 120
    df = pd.DataFrame(
        {
            "open": [100 + i * 0.1 for i in range(rows)],
            "high": [101 + i * 0.1 for i in range(rows)],
            "low": [99 + i * 0.1 for i in range(rows)],
            "close": [100 + i * 0.12 for i in range(rows)],
            "volume": [1000 + i * 5 for i in range(rows)],
        }
    )

    result = MarketAnalysisAgent().analyze(df)

    assert set(result.keys()) == {"trend", "volatility", "market_regime", "indicators"}
    assert "rsi" in result["indicators"]

"""Data transformation helpers for market ingestion."""

from __future__ import annotations

import pandas as pd


KLINE_COLUMNS = [
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "quote_asset_volume",
    "number_of_trades",
    "taker_buy_base_asset_volume",
    "taker_buy_quote_asset_volume",
    "ignore",
]


def klines_to_dataframe(klines: list[list]) -> pd.DataFrame:
    frame = pd.DataFrame(klines, columns=KLINE_COLUMNS)
    numeric_columns = ["open", "high", "low", "close", "volume"]
    frame[numeric_columns] = frame[numeric_columns].astype(float)
    frame["open_time"] = pd.to_datetime(frame["open_time"], unit="ms", utc=True)
    return frame

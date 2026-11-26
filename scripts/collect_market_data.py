import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import date, timedelta

# Project directory
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

# Sector ETFs and market benchmark
tickers = [
    "XLK", "XLF", "XLE", "XLV",
    "XLY", "XLP", "XLI", "XLB",
    "XLU", "XLRE", "XLC", "SPY"
]

# Historical data range
start_date = "2014-01-01"
end_date = (date.today() + timedelta(days=1)).isoformat()

# Download historical adjusted prices
market_data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=True
)

# Extract adjusted closing prices
prices = market_data["Close"].copy()
prices = prices.reindex(columns=tickers)
prices.index.name = "date"

# Save historical prices
output_path = RAW_DIR / "etf_prices.csv"
prices.to_csv(output_path)

# Display dataset information
print("\nMarket data download complete!")
print(f"Saved to: {output_path}")
print(f"Trading days: {len(prices)}")
print(f"Number of ETFs: {len(prices.columns)}")

print("\nDate range:")
print(f"Start: {prices.index.min()}")
print(f"End: {prices.index.max()}")

print("\nAvailable observations:")
print(prices.count())

print("\nMissing values by ticker:")
print(prices.isnull().sum())

print("\nFirst five records:")
print(prices.head())

print("\nLast five records:")
print(prices.tail())
import pandas as pd
from pandas_datareader import data as web
from pathlib import Path
from datetime import date

# Project directory
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

# FRED economic series
series = {
    "DGS2": "treasury_2y",
    "DGS10": "treasury_10y",
    "DFEDTARU": "fed_upper",
    "DFEDTARL": "fed_lower",
    "VIXCLS": "vix"
}

# Historical date range
start_date = "2014-01-01"
end_date = date.today().isoformat()

# Download economic data
fred_data = web.DataReader(
    list(series.keys()),
    "fred",
    start=start_date,
    end=end_date
)

# Rename columns for readability
fred_data = fred_data.rename(columns=series)
fred_data.index.name = "date"

# Save economic data
output_path = RAW_DIR / "fred_data.csv"
fred_data.to_csv(output_path)

# Display dataset information
print("FRED data downloaded successfully!")
print(f"Saved to: {output_path}")
print(f"Total records: {len(fred_data)}")
print(f"Number of variables: {len(fred_data.columns)}")

print("\nDate range:")
print(f"Start: {fred_data.index.min()}")
print(f"End: {fred_data.index.max()}")

print("\nAvailable observations:")
print(fred_data.count())

print("\nMissing values:")
print(fred_data.isnull().sum())

print("\nSummary statistics:")
print(fred_data.describe())

print("\nFirst five records:")
print(fred_data.head())

print("\nLast five records:")
print(fred_data.tail())
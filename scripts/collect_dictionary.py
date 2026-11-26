import pandas as pd
from pathlib import Path

# Project directory
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

# Load financial sentiment dictionary
file_path = RAW_DIR / "lm_dictionary.csv"

if not file_path.exists():
    raise FileNotFoundError(
        "Download the Loughran-McDonald dictionary "
        "and save it as data/raw/lm_dictionary.csv"
    )

df = pd.read_csv(file_path)

# Display dataset information
print("Financial sentiment dictionary loaded!")
print(f"Total words: {len(df)}")

print("\nAvailable columns:")
print(df.columns.tolist())

# Sentiment categories
categories = [
    "Positive",
    "Negative",
    "Uncertainty",
    "Litigious",
    "Strong_Modal",
    "Weak_Modal",
    "Constraining"
]

print("\nWords in each category:")

for category in categories:
    if category in df.columns:
        count = (df[category] > 0).sum()
        print(f"{category}: {count}")

print("\nMissing values:")
print(df.isnull().sum())

print("\nSample dictionary entries:")
print(df.head())
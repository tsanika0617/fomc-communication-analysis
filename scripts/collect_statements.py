import pandas as pd
from pathlib import Path

# Define project directory
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

# FOMC communications data source
URL = (
    "https://raw.githubusercontent.com/"
    "vtasca/fed-statement-scraping/"
    "master/communications.csv"
)

# Download and save the dataset
df = pd.read_csv(URL)

output_path = RAW_DIR / "communications.csv"
df.to_csv(output_path, index=False)

# Display dataset information
print("FOMC dataset downloaded successfully!")
print(f"Saved to: {output_path}")
print(f"Total records: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

print("\nCommunication types:")
print(df["Type"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())

print("\nFirst five records:")
print(df[["Date", "Release Date", "Type"]].head())
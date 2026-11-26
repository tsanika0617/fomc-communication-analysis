import pandas as pd
from pathlib import Path

# Project directory
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

# Load USMPD workbook
file_path = RAW_DIR / "USMPD.xlsx"
workbook = pd.ExcelFile(file_path)

print("USMPD workbook loaded successfully!")

# Inspect available worksheets
print("\nAvailable worksheets:")
for sheet in workbook.sheet_names:
    print(sheet)

# Inspect each worksheet
for sheet in workbook.sheet_names:
    df = pd.read_excel(workbook, sheet_name=sheet)

    print(f"\nWorksheet: {sheet}")
    print(f"Dimensions: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")

    print("\nFirst three records:")
    print(df.head(3).to_string(index=False))

# Inspect monetary policy surprise files
surprise_dir = RAW_DIR / "monetary-policy-surprises"

print("\nMonetary policy surprise files:")

if surprise_dir.exists():
    for file in sorted(surprise_dir.rglob("*")):
        if file.is_file():
            print(file.relative_to(RAW_DIR))
else:
    print("Folder not found.")
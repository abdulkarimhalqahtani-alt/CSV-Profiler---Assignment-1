from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

raw_path = ROOT / "data" / "raw" / "sample.csv"
processed_path = ROOT / "data" / "processed" / "sample.parquet"

# Load
df = pd.read_csv(raw_path)

# Simple transform: IDs as string
for col in df.columns:
    if "id" in col.lower():
        df[col] = df[col].astype("string")

# Write processed (idempotent)
processed_path.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(processed_path, index=False)

print("✅ Processed file written to:")
print(processed_path)
print(df.dtypes)


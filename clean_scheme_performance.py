import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Read CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert expense ratio to numeric
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

# Flag expense ratio anomalies
df["expense_ratio_flag"] = (
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
)

print("\nExpense Ratio Anomalies:")
print(df["expense_ratio_flag"].sum())

# Save cleaned CSV
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned scheme performance saved successfully!")
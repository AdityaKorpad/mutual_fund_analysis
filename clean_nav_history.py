import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Read the CSV file
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort by AMFI code and date
df = df.sort_values(by=["amfi_code", "date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Forward fill missing NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Keep only valid NAV values
df = df[df["nav"] > 0]

print("\nCleaned Shape:", df.shape)

# Save cleaned file
df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("\nCleaned file saved successfully!")
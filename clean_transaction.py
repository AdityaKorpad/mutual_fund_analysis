import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Convert date column to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.upper()
)

valid_kyc = ["YES", "NO", "PENDING"]
df = df[df["kyc_status"].isin(valid_kyc)]

print("\nCleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaned transactions saved successfully!")
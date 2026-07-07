"""
Retail Store Sales — Data Cleaning Script
Author: Dmytro Lysov
Tool: Claude AI (diagnostic & cleaning plan) + Python (pandas)

Data Quality Issues Identified by Claude AI:
- Discount Applied: 4,199 missing (33.4%)
- Item:            1,213 missing (9.6%)
- Price Per Unit:    609 missing (4.8%)
- Quantity:          604 missing (4.8%)
- Total Spent:       604 missing (4.8%)
"""

import pandas as pd

# ── 1. Load raw data ──────────────────────────────────────────────
df = pd.read_csv("retail_store_sales.csv")
rows_before = len(df)
print(f"Rows before cleaning: {rows_before}")

# ── 2. Fix: Discount Applied ─────────────────────────────────────
# No record = discount was not applied
df["Discount Applied"] = df["Discount Applied"].fillna(False)

# ── 3. Fix: Price Per Unit ───────────────────────────────────────
# Recover from Total Spent / Quantity where both exist
mask_price = df["Price Per Unit"].isna() & df["Total Spent"].notna() & df["Quantity"].notna()
df.loc[mask_price, "Price Per Unit"] = (
    df.loc[mask_price, "Total Spent"] / df.loc[mask_price, "Quantity"]
).round(2)
print(f"Price Per Unit recovered: {mask_price.sum()} rows")

# ── 4. Drop: rows where Quantity AND Total Spent are both missing ─
mask_drop = df["Quantity"].isna() & df["Total Spent"].isna()
df = df[~mask_drop]
print(f"Rows dropped (no Quantity + Total Spent): {mask_drop.sum()}")

# ── 5. Item: keep rows with missing Item if Category exists ───────
# Category is sufficient for category-level analysis
missing_item_kept = df["Item"].isna().sum()
print(f"Item still missing (kept, Category available): {missing_item_kept}")

# ── 6. Parse date ─────────────────────────────────────────────────
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

# ── 7. Summary ───────────────────────────────────────────────────
rows_after = len(df)
print(f"\nRows after cleaning: {rows_after}")
print(f"Rows removed: {rows_before - rows_after} ({(rows_before - rows_after)/rows_before*100:.1f}%)")
print(f"\nRemaining missing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# ── 8. Save clean file ────────────────────────────────────────────
df.to_csv("retail_store_sales_clean.csv", index=False)
print("\nSaved: retail_store_sales_clean.csv")

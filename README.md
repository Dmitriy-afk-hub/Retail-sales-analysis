# Retail-sales-analysis
# Retail Store Sales — AI-Assisted Data Analysis

## Project Overview

End-to-end data analysis project on a dirty retail sales dataset (12,575 rows).  
The goal was to demonstrate a realistic analyst workflow: AI-assisted diagnostics → data cleaning → exploratory analysis → interactive dashboard.

---

## Tools & Workflow

| Stage | Tool | Purpose |
|---|---|---|
| Data Diagnostics | **Claude AI** | Identified data quality issues, created cleaning plan |
| Exploratory Analysis | **Julius AI** | Automated EDA — distributions, revenue by category, time trends |
| Data Cleaning | **Python (pandas)** | Implemented cleaning plan, recovered missing values |
| Dashboard | **Power BI** | Interactive KPI dashboard on clean data |

---

## Data Quality Issues Found (Claude AI Diagnostic)

Raw dataset: **12,575 rows · 11 columns**

| Column | Missing Values | % | Action Taken |
|---|---|---|---|
| `Discount Applied` | 4,199 | 33.4% | Filled with `False` (no record = no discount) |
| `Item` | 1,213 | 9.6% | Kept — Category sufficient for analysis |
| `Price Per Unit` | 609 | 4.8% | Recovered via `Total Spent / Quantity` |
| `Quantity` | 604 | 4.8% | Rows dropped (no Quantity + Total Spent) |
| `Total Spent` | 604 | 4.8% | Rows dropped (no Quantity + Total Spent) |

**Result after cleaning: 11,971 rows (604 rows removed, 4.8%)**

No duplicate transactions. No calculation errors (`Total Spent = Price × Quantity` verified across all rows).

---

## Exploratory Analysis (Julius AI)

Julius AI was used on the **raw dataset** to visualise initial data shape before cleaning:

- Spending distribution skewed by missing values in `Discount Applied` (33.4%)
- Revenue relatively balanced across 8 categories — no dominant category
- Transaction volume stable over time with moderate variance
- Practical mid-range transaction sizes (avg ~$130)

This EDA confirmed the need for structured cleaning before building a reliable dashboard.

---

## Key Findings (Power BI Dashboard)

| KPI | Value |
|---|---|
| Total Revenue | $1.55M |
| Total Transactions | 11,971 |
| Avg Order Value | $129.65 |

- **Top categories by revenue:** Butchers, Electric Household Essentials, Beverages
- **Payment methods:** evenly split — Cash (34.3%), Credit Card (32.9%), Digital Wallet (32.8%)
- **Transaction volume:** stable month-over-month with no strong seasonal pattern

---

## Files

| File | Description |
|---|---|
| `retail_store_sales.csv` | Original raw dataset (Kaggle) |
| `retail_store_sales_clean.csv` | Cleaned dataset (11,971 rows) |
| `cleaning.py` | Python cleaning script with comments |
| `dashboard_screenshot.png` | Power BI dashboard |

---

## Skills Demonstrated

- AI-assisted data diagnostics (Claude AI, Julius AI)
- Data cleaning & validation (Python, pandas)
- Exploratory data analysis
- Dashboard design (Power BI)
- Data storytelling & documentation

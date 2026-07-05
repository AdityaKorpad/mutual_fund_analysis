# Mutual Fund Analysis - Data Dictionary

## 1. Fund Master (01_fund_master.csv)

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| scheme_name | Text | Name of the mutual fund scheme |
| fund_house | Text | Asset Management Company (AMC) |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct or Regular Plan |
| risk_grade | Text | Risk level of the scheme |

---

## 2. NAV History (02_nav_history_cleaned.csv)

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | AMFI Scheme Code |
| date | Date | NAV Date |
| nav | Decimal | Net Asset Value |

---

## 3. AUM by Fund House

| Column | Data Type | Description |
|--------|-----------|-------------|
| fund_house | Text | AMC Name |
| aum_crore | Decimal | Assets Under Management |
| num_schemes | Integer | Number of Schemes |

---

## 4. Monthly SIP Inflows

| Column | Data Type | Description |
|--------|-----------|-------------|
| month | Date | Month |
| sip_inflow_crore | Decimal | SIP Inflow |
| active_sip_accounts | Integer | Active SIP Accounts |

---

## 5. Category Inflows

| Column | Data Type | Description |
|--------|-----------|-------------|
| category | Text | Mutual Fund Category |
| inflow_crore | Decimal | Net Inflow |

---

## 6. Industry Folio Count

| Column | Data Type | Description |
|--------|-----------|-------------|
| month | Date | Reporting Month |
| total_folios | Integer | Total Folios |

---

## 7. Scheme Performance

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Scheme Code |
| return_1yr_pct | Decimal | 1 Year Return |
| return_3yr_pct | Decimal | 3 Year Return |
| return_5yr_pct | Decimal | 5 Year Return |
| expense_ratio_pct | Decimal | Expense Ratio |
| aum_crore | Decimal | Assets Under Management |

---

## 8. Investor Transactions

| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | Integer | Investor ID |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Decimal | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| age_group | Text | Age Group |
| kyc_status | Text | KYC Verification Status |

---

## 9. Portfolio Holdings

Contains stock holdings of each mutual fund scheme.

---

## 10. Benchmark Indices

Contains benchmark index performance data used for comparison.
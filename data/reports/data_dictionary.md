# Mutual Fund Data Dictionary

## 01_fund_master
- amfi_code : Unique AMFI Scheme Code
- scheme_name : Mutual Fund Scheme Name
- fund_house : Asset Management Company
- category : Fund Category
- plan : Direct/Regular Plan

## 02_nav_history
- amfi_code : Scheme Code
- date : NAV Date
- nav : Net Asset Value

## 07_scheme_performance
- return_1yr_pct : 1 Year Return
- return_3yr_pct : 3 Year Return
- return_5yr_pct : 5 Year Return
- expense_ratio_pct : Expense Ratio
- aum_crore : Assets Under Management

## 08_investor_transactions
- investor_id : Investor ID
- transaction_date : Transaction Date
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction Amount
- state : Investor State
- city : Investor City
- city_tier : Tier Classification
- age_group : Investor Age Group
- gender : Investor Gender
- annual_income_lakh : Annual Income
- payment_mode : Payment Method
- kyc_status : KYC Status
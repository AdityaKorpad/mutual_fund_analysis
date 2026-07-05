-- 1 Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3 Monthly Average NAV
SELECT substr(date,1,7) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- 4 Transactions by State
SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state;

-- 5 SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Sip';

-- 6 Redemption Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Redemption';

-- 7 Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- 8 Funds with Expense Ratio <1%
SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct<1;

-- 9 Highest 5-Year Return
SELECT scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 10 Total Transaction Amount
SELECT SUM(amount_inr)
FROM fact_transactions;
-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT substr(date,1,7) AS month,
AVG(nav) AS average_nav
FROM nav_history
GROUP BY month;

-- 3. SIP Transactions Count
SELECT COUNT(*) AS sip_transactions
FROM investor_transactions
WHERE transaction_type='Sip';

-- 4. Total Transaction Amount by State
SELECT state,
SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with Expense Ratio less than 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 5 Funds by 5-Year Return
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Average Expense Ratio
SELECT AVG(expense_ratio_pct) AS avg_expense_ratio
FROM scheme_performance;

-- 8. Total AUM
SELECT SUM(aum_crore) AS total_aum
FROM scheme_performance;

-- 9. Number of Funds by Category
SELECT category,
COUNT(*) AS total_funds
FROM fund_master
GROUP BY category;

-- 10. Average NAV
SELECT AVG(nav) AS average_nav
FROM nav_history;
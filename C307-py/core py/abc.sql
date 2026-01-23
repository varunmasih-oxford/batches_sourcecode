SELECT 
    tsm AS shift,
    COUNT(*) AS total_orders
FROM hourly_sale
GROUP BY tsm;

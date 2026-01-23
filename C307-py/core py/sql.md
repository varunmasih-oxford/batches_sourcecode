

## Retail Sales Analysis SQL Project



# CREATE DATABASE p1_retail_db;

CREATE TABLE retail_sales
(
    transactions_id INT PRIMARY KEY,
    sale_date DATE,	
    sale_time TIME,
    customer_id INT,	
    gender VARCHAR(10),
    age INT,
    category VARCHAR(35),
    quantity INT,
    price_per_unit FLOAT,	
    cogs FLOAT,
    total_sale FLOAT
);



# copy data from csv file

LOAD DATA INFILE 'C:/Users/Admin/Downloads/bike_buyers.csv'
INTO TABLE dd
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;







# Data Exploration & Cleaning

-Record Count: Determine the total number of records in the dataset.
-Customer Count: Find out how many unique customers are in the dataset.
-Category Count: Identify all unique product categories in the dataset.
-Null Value Check: Check for any null values in the dataset and delete
records with missing data.

SELECT COUNT(*) FROM retail_sales;
SELECT COUNT(DISTINCT customer_id) FROM retail_sales;
SELECT DISTINCT category FROM retail_sales;

SELECT * FROM retail_sales
WHERE 
    sale_date IS NULL OR sale_time IS NULL OR customer_id IS NULL OR 
    gender IS NULL OR age IS NULL OR category IS NULL OR 
    quantity IS NULL OR price_per_unit IS NULL OR cogs IS NULL;

DELETE FROM retail_sales
WHERE 
    sale_date IS NULL OR sale_time IS NULL OR customer_id IS NULL OR 
    gender IS NULL OR age IS NULL OR category IS NULL OR 
    quantity IS NULL OR price_per_unit IS NULL OR cogs IS NULL;






# Data Analysis & Findings


1.Write a SQL query to retrieve all columns for sales made on '2022-11-05:

SELECT *
FROM retail_sales
WHERE sale_date = '2022-11-05';

################################

2.Write a SQL query to retrieve all transactions where the category is 'Clothing' and the quantity sold is more than 4 in the month of Nov-2022:



SELECT * FROM `abc` 
WHERE `category` = 'Clothing'
AND
`quantiy` >= 4
AND
DATE_FORMAT(sale_date, '%Y-%m') = '2022-11'

################################


3. Write a SQL query to calculate the total sales (total_sale) for each category.:


SELECT 
category,SUM(total_sale) as sales 
FROM `abc` 
GROUP BY 1

################################

4. Write a SQL query to find the average age of customers who purchased items from the 'Beauty' category.:


SELECT `category`, round(AVG(age),2) as 'average age' 
FROM `abc` 
WHERE `category` = 'Beauty'

################################

5. Write a SQL query to find all transactions where the total_sale is greater than 1000.:

SELECT `transactions_id`,`total_sale` 
FROM `abc` 
WHERE `total_sale`>1000


################################

6. Write a SQL query to find the total number of transactions (transaction_id) made by each gender in each category.:


SELECT `category`,`gender`,COUNT(`transactions_id`) AS cnt_trns 
FROM `abc` 
GROUP BY `category`,`gender`

################################

7. Write a SQL query to calculate the average sale for each month. Find out best selling month in each year:

SELECT 
    year,
    month,
    avg_sale
FROM 
(
    SELECT 
        YEAR(sale_date) AS year,
        MONTH(sale_date) AS month,
        AVG(total_sale) AS avg_sale,
        RANK() OVER (
            PARTITION BY YEAR(sale_date)
            ORDER BY AVG(total_sale) DESC
        ) AS rank
    FROM retail_sales
    GROUP BY YEAR(sale_date), MONTH(sale_date)
) AS t1
WHERE rank = 1;


################################

8. Write a SQL query to find the top 5 customers based on the highest total sales



SELECT 
	`customer_id`,
    SUM(`total_sale`) as total_sale 
FROM `abc` 
GROUP BY 1
order BY `total_sale` DESC
LIMIT 5



################################

9. Write a SQL query to find the number of unique customers who purchased items from each category.:



SELECT 
`category`,
COUNT(DISTINCT `customer_id`)
FROM `abc` 
group by `category`

################################


10. Write a SQL query to create each shift and number of orders (Example Morning <12, Afternoon Between 12 & 17, Evening >17):

# without CTE

SELECT
    CASE
        WHEN HOUR(sale_time) < 12 THEN 'Morning'
        WHEN HOUR(sale_time) BETWEEN 12 AND 17 THEN 'Afternoon'
        ELSE 'Evening'
    END AS shift,
    COUNT(*) AS total_orders
FROM abc
GROUP BY shift




# with CTE


WITH hourly_sale
AS
(
SELECT 
    *,
    CASE
        WHEN HOUR(sale_time) < 12 THEN 'GM'
        WHEN HOUR(sale_time) BETWEEN 12 AND 17 THEN 'GA'
        ELSE 'Ev'
    END AS tsm
FROM abc;

)
SELECT 
    shift,
    COUNT(*) as total_orders    
FROM hourly_sale
GROUP BY shift

##### or


WITH hourly_sale AS (
    SELECT 
        *,
        CASE
            WHEN HOUR(sale_time) < 12 THEN 'GM'
            WHEN HOUR(sale_time) BETWEEN 12 AND 17 THEN 'GA'
            ELSE 'Ev'
        END AS tsm
    FROM abc
)
SELECT 
    tsm AS shift,
    COUNT(*) AS total_orders
FROM hourly_sale
GROUP BY tsm;

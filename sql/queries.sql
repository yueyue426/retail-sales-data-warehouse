-- Aggregation queries

-- Create a grouping sets query, using GROUPING SETS to specify the different levels of aggregation:
-- By both Productid and Producttype
-- By Productid alone
-- By Producttype alone
-- And a grand total with (), which doesn't group by any column and returns the sum for all sales
SELECT p.Productid,
       p.Producttype,
       SUM(f.Price_PerUnit * f.QuantitySold) AS TotalSales
FROM FactSales f
JOIN DimProduct p
ON f.Productid = p.Productid
GROUP BY GROUPING SETS (
    (p.Productid, p.Producttype),
    p.Productid,
    p.Producttype,
    ()
)
ORDER BY p.Productid, p.Producttype;

-- Create a rollup query; using ROLLUP function to include all combinations of year, city and productid
-- along with their respective subtotals and a grand total for all sales.
SELECT d.Year,
       cs.City,
       p.Productid,
       SUM(f.Price_PerUnit * f.QuantitySold) AS TotalSales
FROM FactSales f
JOIN DimDate d ON f.dateid = d.dateid
JOIN DimProduct p ON f.Productid = p.Productid
JOIN DimCustomerSegment cs ON f.Segmentid = cs.Segmentid
GROUP BY ROLLUP (
    d.Year,
    cs.City,
    p.Productid
)
ORDER BY d.Year DESC, cs.City, p.Productid;

-- Create a cube query; using CUBE clause to create sub-average for all combinations of year, city, and productid
-- in addition to the grand average across all groups.
SELECT d.Year,
       cs.City,
       p.Productid,
       AVG(f.Price_PerUnit * f.QuantitySold) AS AverageSales
FROM FactSales f
JOIN DimDate d ON f.dateid = d.dateid
JOIN DimProduct p ON f.Productid = p.Productid
JOIN DimCustomerSegment cs ON f.Segmentid = cs.Segmentid
GROUP BY CUBE (
    d.Year,
    cs.City,
    p.Productid
);

-- Create a materialized view
CREATE MATERIALIZED VIEW max_sales AS
SELECT cs.City,
       p.Productid,
       p.Producttype,
       MAX(f.Price_PerUnit * f.QuantitySold) AS MaxSales
FROM FactSales f
JOIN DimProduct p ON f.Productid = p.Productid
JOIN DimCustomerSegment cs ON f.Segmentid = cs.Segmentid
GROUP BY cs.City, p.Productid, p.Producttype
WITH DATA;
-- WITH DATA clause is to fill the view with the query results immediately
-- If want to create the view without filling it with data, use WITH NO DATA.

-- Update the materialized view with the latest data
--REFRESH MATERIALIZED VIEW max_sales;
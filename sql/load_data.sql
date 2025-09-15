-- Scrip to load CSV data into the Data Warehouse tables

-- Load DimDate
\COPY DimDate (dateid, date, Year, Quarter, QuarterName, Month, MonthName, Day, Weekday, WeekdayName)
FROM './data/DimDate.csv'
DELIMITER ','
CSV HEADER;

-- Load DimProduct
\COPY DimProduct (Productid, Producttype)
FROM './data/DimProduct.csv'
DILIMITER ','
CSV HEADER;

-- Load DimCustomerSegment
\COPY DimCustomerSegment (Segmentid, City)
FROM './data/DimCustomerSegment.csv'
DILIMITER ','
CSV HEADER;

-- Load FactSales
\COPY FactSales (Salesid, dateid, Productid, Segmentid, Price_PerUnit, QuantitySold)
FROM './data/FactSales.csv'
DILIMITER ','
CSV HEADER;

-- Verify row counts after loading
SELECT 'DimDate' AS TableName, COUNT(*) AS counts FROM DimDate
UNION
SELECT 'DimProduct', COUNT(*) FROM DimProduct
UNION
SELECT 'DimCustomerSegment', COUNT(*) FROM DimCustomerSegment
UNION
SELECT 'FactSales', COUNT(*) FROM FactSales;
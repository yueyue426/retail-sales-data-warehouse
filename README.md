# Sales Data Warehouse with Automated Data Quality Checks

## Overview 
This project showcase the complete lifecycle of building and validating
a retail sales data warehouse. Using PostgreSQL, a start schema with fact
and dimension tables was designed to support analysis of sales trends by
product, city, and time period, with optimized queries and materialized
views for reporting. To ensure data reliability, a Python-based framework 
was implemented to automate data quality checks for nulls, duplicates, 
invalid values, and range violations, generating reports that guarantee 
accuracy before loading into the warehouse. Together, the project
demonstrates practical skills in data modeling, ETL pipeline staging, and 
data governance for real-world data engineering scenarios.

## Table of Contents
- [Tools & Skills](#tools--skills)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Tools & Skills
- **PostgreSQL** - Database design, schema creation, SQL queries, materialized views
- **Python** - Automated data quality checks with custom scripts
- **Pandas** - Generating tabular quality reports
- **SQL** - Start schema implementation, aggregation queries
- **Data Engineering Concepts** - Data warehouse design, staging area, 
data quality assurance, ETL basics

## Features
- Designed dimension and fact tables for structured storage.
- Loaded CSV datasets into the warehouse using PostgreSQL import tools.
- Built aggregation queries to analyze total/average sales by product, city and year.
- Create materialized views for performance optimization in reporting.
- Automated data quality checks:
  - Null value detection
  - Duplicate record checks
  - Range validation (min/max)
  - Valid value enforcement
- Generate data quality reports to document test results and ensure
confidence in downstream analytics.

## Installation
1. Set up PostgreSQL
   - Install PostgreSQL and pgAdmin
   - Create the project database
2. Load Warehouse Schema
   - Run provided SQL scripts to create dimension and fact tables
   - Import CSV files into each table using pgAdmin's Import/Export tool
3. Prepare Python Environment
   - Install dependencies:
```commandline
pip install psycopg2 pandas tabulate
```
  - Update `dbconnect.py` with PostgreSQL credentials
4. Download Data Quality Framework
   - `dataqualitychecks.py`
   - `dbconnect.py`
   - `mytests.py`
   - `generate-data-quality-report.py`

## Usage
- Query the Warehouse, e.g.:
```sql
SELECT year, city, SUM(price_perunit * quantitysold) AS totalsales
FROM FactSales f
JOIN DimDate d ON f.dateid = d.dateid
JOIN DimCustomerSegment cs ON f.segmentid = cs.segmentid
GROUP BY ROLLUP (year, city);
```
- Run Data Quality Checks, execute automated tests:
```commandline
python3 generate-data-quality-report.py
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
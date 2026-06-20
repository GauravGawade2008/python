# Sales Transactions Analysis using Pandas

## Overview

This project demonstrates data analysis using Python and Pandas on a sales transactions dataset. The goal is to practice data inspection, date handling, feature engineering, grouping, aggregation, sorting, filtering, and business KPI calculations.

The analysis helps answer common business questions such as:

* Which product generates the highest revenue?
* Which salesperson performs best?
* Which region sells the most units?
* Which category contributes the most revenue?
* What is the monthly revenue trend?
* What percentage of revenue comes from Electronics products?

---

## Technologies Used

* Python
* Pandas

---

## Dataset

The dataset contains sales transaction records with information such as:

* Date
* Product
* Category
* Quantity
* Revenue / Total Amount
* Region
* Salesperson

---

## Tasks Performed

### 1. Data Inspection

* Loaded the CSV file using Pandas
* Displayed sample records
* Examined dataset structure using:

  * `head()`
  * `info()`
  * `describe()`
* Checked for missing values

### 2. Date Handling

* Converted the date column to datetime format
* Extracted:

  * Quarter
  * Month

### 3. Revenue Analysis

* Calculated total revenue by category
* Calculated total revenue by product
* Identified top-performing products

### 4. Sales Analysis

* Calculated total quantity sold by region
* Identified top salespersons by:

  * Revenue
  * Quantity Sold

### 5. Business KPIs

* Calculated Average Order Value
* Analyzed Monthly Revenue Trend
* Identified Best Selling Month

### 6. Category Contribution Analysis

* Filtered Electronics category sales
* Calculated Electronics revenue contribution as a percentage of total revenue

---

## Pandas Concepts Practiced

* Reading CSV files
* Data inspection
* Missing value analysis
* Datetime conversion
* Feature engineering
* Column insertion
* Filtering data
* GroupBy operations
* Aggregation functions
* Sorting
* KPI calculations

---

## Project Structure

```text

sales-transactions-analysis/
│
├── README.md
├── sales_transactions.csv
├── sales_transactions.py
├── sales_transactions.ipynb
└── updated_sales_transactions.csv
```
---

## Files Description

* `sales_transactions.csv` – Original dataset used for analysis.
* `sales_transactions.py` – Python script containing the complete analysis workflow.
* `sales_transactions.ipynb` – Jupyter Notebook version with code, outputs, and analysis.
* `updated_sales_transactions.csv` – Processed dataset generated during analysis.
* `README.md` – Project documentation and overview.

---

## Learning Outcome

Through this project, I gained hands-on experience with:

* Real-world data analysis workflows
* Business-oriented data insights
* Pandas GroupBy and aggregation operations
* Datetime feature extraction
* KPI calculation and reporting

This project was created as part of my Pandas learning journey and focuses on applying data analysis concepts to practical business scenarios.

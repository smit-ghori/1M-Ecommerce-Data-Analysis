# 1M Ecommerce Data Analysis

This project presents a comprehensive exploratory data analysis of a large e-commerce dataset containing approximately one million orders. The analysis is implemented in [Ecommerce Analysis.ipynb](Ecommerce%20Analysis.ipynb) and focuses on understanding customer behavior, sales performance, product trends, delivery efficiency, and return patterns.

## Project Overview

The notebook walks through the full analytics pipeline, from loading raw transaction data to deriving actionable business insights. It combines data cleaning, descriptive analysis, statistical testing, segmentation, and KPI summarization in a structured and professional workflow.

## Objectives

The analysis aims to answer several important business questions:

- How are customers distributed across gender, city, membership tier, and age groups?
- Which product categories generate the most revenue?
- Which cities perform best in terms of sales and customer activity?
- Do discounts increase sales, or do they reduce revenue per order?
- Does delivery time affect customer satisfaction?
- Are there meaningful differences in spending between customer segments?
- What business recommendations can be drawn from the data?

## Dataset

The project uses the following files:

- [ecommerce_data_1M.csv](ecommerce_data_1M.csv) — raw e-commerce transaction dataset
- [Cleaned dataset](https://drive.google.com/file/d/1u5zvgvJLscXzuI25ehyMnH_Y4mZiemjO/view?usp=sharing) — cleaned version prepared during the notebook workflow

The dataset includes key business and customer-related fields such as:

- customer identifiers
- age and gender
- city and membership tier
- product category and payment method
- price, quantity, discount percentage, and total amount
- delivery days, rating, and return status
- order date for time-based analysis

## Analysis Workflow

The notebook is organized into the following stages:

1. Data Loading and Initial Inspection
   - Load the dataset into a pandas DataFrame
   - Examine shape, columns, data types, and summary statistics

2. Data Cleaning and Preprocessing
   - Handle missing values in key columns
   - Remove duplicate records
   - Convert date columns to datetime format
   - Prepare the dataset for analysis

3. Exploratory Data Analysis
   - Analyze categorical variables such as gender, city, membership tier, product category, and payment method
   - Visualize distributions and identify dominant patterns

4. Advanced Business Analysis
   - Study customer spending by age group and gender
   - Examine product category performance and return behavior
   - Analyze city-wise sales and delivery patterns
   - Review customer satisfaction using ratings and delivery times

5. Revenue and Trend Analysis
   - Investigate monthly revenue trends
   - Explore monthly return-rate patterns
   - Understand how business performance changes over time

6. Correlation and Statistical Analysis
   - Measure relationships between numerical variables
   - Perform an independent t-test to compare spending between male and female customers

7. Customer Segmentation and KPI Dashboard
   - Identify high-value and frequent buyers
   - Analyze customer activity by membership tier over time
   - Summarize key business KPIs for sales, customers, products, and delivery

## Key Findings

The notebook highlights several important insights:

- Gender distribution is nearly balanced, indicating broad and even customer reach across both genders.
- Mumbai has the highest number of orders, while Jaipur has the lowest.
- Bronze is the most common membership tier, while Platinum is the least common.
- Electronics is the most popular and highest-revenue product category.
- UPI is the most frequently used payment method.
- The 36–45 age group contributes the highest revenue.
- Higher discounts do not significantly increase the average quantity sold; in fact, higher discounts are associated with slightly lower average order value.
- Delivery times remain around five days on average and do not appear to significantly affect ratings.
- Price shows a strong positive correlation with total amount.
- There is no statistically significant difference in average spending between male and female customers.

## Business Recommendations

Based on the analysis, the following recommendations are suggested:

- Focus marketing efforts on the 36–45 age group, as it contributes the highest revenue.
- Prioritize top-performing cities such as Mumbai while improving engagement in lower-performing regions.
- Reevaluate discount strategy and avoid relying on discounts as the main driver of sales.
- Strengthen inventory, pricing, and promotions for high-revenue categories such as Electronics, Home & Kitchen, and Clothing.
- Investigate slightly higher return rates in categories like Sports and improve product description or quality where needed.
- Maintain reliable delivery operations and continue monitoring customer satisfaction trends.
- Use loyalty programs to encourage Bronze-tier customers to upgrade to higher-value tiers.

## Technologies Used

- Python
- pandas
- numpy
- seaborn
- matplotlib
- scipy
- Jupyter Notebook

## How to Run

1. Install the required Python packages:
   - pandas
   - numpy
   - seaborn
   - matplotlib
   - scipy

2. Open the notebook in Jupyter:
   - [Ecommerce Analysis.ipynb](Ecommerce%20Analysis.ipynb)

3. Run the cells in sequence to reproduce the analysis and visualizations.

## Visual Outputs

The notebook saves the most important visualizations, and the shared chart gallery is available here:

- [Image folder](https://drive.google.com/drive/folders/1NpeQ4vD1QeMxJz40M9Qfi51DN4yyeSmK?usp=sharing)

## Future Work

Potential next steps for this project include:

- Building a predictive model to classify whether an order will be returned
- Creating a more interactive dashboard for business stakeholders
- Adding automated reporting for monthly performance summaries

## Repository Contents

- [Ecommerce Analysis.ipynb](Ecommerce%20Analysis.ipynb) — main analysis notebook
- [ecommerce_data_1M.csv](ecommerce_data_1M.csv) — source data
- [Cleaned dataset](https://drive.google.com/file/d/1u5zvgvJLscXzuI25ehyMnH_Y4mZiemjO/view?usp=sharing)
- [README.md](README.md) — project documentation

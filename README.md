8# Sales-price-prediction
---

📈 Sales Forecast Analysis

📋 Project Overview

This project focuses on the exploratory data analysis (EDA) of a sales dataset with the aim of uncovering key business insights, such as customer purchasing behavior, shipping preferences, and revenue generation across various segments and geographic locations. The dataset contains 9,800 sales records with 18 features.


---

📦 Dataset Description

The dataset includes records of sales transactions and contains the following key attributes:

Order and shipment details (e.g., order ID, order date, ship date, ship mode)

Customer information (e.g., customer ID, customer name, segment)

Geographic data (e.g., city, state, region, postal code)

Product information (e.g., category, sub-category, product name)

Sales figures



---

🔍 Data Exploration Highlights

✅ Dataset Dimensions

Total Records: 9,800

Total Features: 18


🧼 Data Quality

One column, Postal Code, contained a minimal number of missing values (~0.11%) which were handled appropriately.

No duplicated records were found in the dataset.


📊 Descriptive Statistics

Sales ranged from $0.44 to $22,638.48.

The mean sales value was $230.77, with a standard deviation of $626.65.

Outliers in the Sales column were identified and removed using z-score filtering.



---

📦 Shipping Analysis

🚚 Ship Mode Usage

The Standard Class shipping method was the most frequently used, accounting for 5,788 transactions.


💰 Revenue by Ship Mode

Standard Class also generated the highest revenue, totaling approximately $1,041,468.86.



---

👥 Customer Segment Analysis

📦 Transaction Count by Segment

The Consumer segment had the highest number of transactions, approximately 5,041 records.


💸 Revenue by Segment

The Consumer segment also generated the most revenue, around $896,586.78.



---

🌆 City-wise Insights

🛍️ Top Cities by Transaction Count

New York City topped the list with 868 transactions, followed by Los Angeles and Philadelphia.


💰 Top Cities by Revenue

New York City led in revenue generation, with approximately $165,554.67.



---

🗺️ State-wise Insights

📦 Top States by Transaction Count

California recorded the highest number of sales, with 1,923 transactions.


💸 Top States by Revenue

California also led in revenue generation, contributing approximately $365,159.08.


---

✅ Recommendations

1. Focus Marketing on the Consumer Segment

The Consumer segment accounts for the highest number of transactions and revenue.

Targeted promotions, loyalty programs, and personalized offers for this segment could further boost sales.


2. Optimize Shipping Strategy

Since Standard Class is the most used and highest-revenue-generating shipping mode, consider:

Improving logistics and delivery times for Standard Class.

Offering incentives for customers to choose lower-cost shipping options where applicable to reduce costs.



3. Prioritize Key Regions and Cities

California, particularly New York City and Los Angeles, generate significant revenue.

Increase inventory availability, local marketing campaigns, and customer support in these areas.


4. Address Sales Outliers

A small number of extremely high-value sales heavily influence the average sales figure.

Segment high-value customers and create tailored sales strategies or premium services for them.


5. Leverage Top-Performing Products and Categories

Though not detailed here, a deeper product-level analysis can identify best-selling items.

Promote these products more aggressively and consider bundling them with slower-moving stock.


6. Improve Data Completeness

While missing data was minimal, strive to reduce any loss of key information (e.g., postal codes) during data collection for better geographic analysis.


7. Invest in Forecasting Models

Use time series or machine learning models to forecast demand by product, region, and segment.

This helps optimize stock levels, reduce overstocking, and improve supply chain efficiency.

---

📈 Conclusion

This exploratory analysis provided valuable insights into customer behavior, shipping trends, and revenue contributions across regions and segments. The analysis highlights the importance of certain customer groups (like the Consumer segment), specific cities (such as New York City), and preferred shipping methods (especially Standard Class) in driving sales performance.
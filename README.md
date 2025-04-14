# Payment-Reconciliation-Pipeline

## Overview
This project is an end-to-end data engineering pipeline that generates realistic synthetic data using [Faker](https://faker.readthedocs.io/), modeled after Stripe payment intents. The pipeline produces data in multiple formats—JSON, Parquet, and CSV, which are uploaded to Backblaze B2, the data lake. The raw data is then transformed using Databricks to prepare a clean, structured view that feeds into a Power BI dashboard. The dashboard provides business insights such as payment volume, status breakdowns, and currency distribution.

![Architecture](pipeline/pipeline%20architecture%20flowchart.png)

## Problem Statement
Companies often face challenges in integrating data from disparate sources and formats, processing large-scale data with minimal cost, and transforming it into actionable insights. This project addresses that challenge by combining open source tools and free cloud services to build a reproducible, scalable pipeline. The work demonstrates the ability to manage structured and semi-structured data, perform quality transformations and aggregations using Databricks, and deliver visualizations through Power BI, ultimately empowering businesses to make data-driven decisions without incurring high infrastructure costs.

---

## How the Pipeline Works

1. **Data Generation:**  
   - Synthetic Stripe payment data is generated using Python's Faker library to mimic the real Stripe `payment_intent` JSON schema.
   - Records include fields like `id`, `amount`, `currency`, `status`, timestamps, and nested payment method details.

2. **Format Conversion:**  
   - The generated data is saved as a JSON file.
   - This JSON is then converted into efficient Parquet and human-readable CSV formats.

3. **Data Lake Upload:**  
   - The files (JSON, Parquet, and CSV) are uploaded to a data lake.  
   - This project uses Backblaze B2, but any S3-compatible data lake can be configured.

4. **Databricks Integration:**  
   - Databricks is used for advanced data transformation, validation, and quality checks.
   - Processed data is stored and prepared as a "warehouse" layer, from which Power BI can draw the latest analytics.

5. **Dashboard Visualization:**  
   - A Power BI dashboard connects to the final processed CSV/Parquet files.
   - Key insights such as total payment amount, status breakdown, trend over time, and top customers are visualized.
   - The dashboard refreshes manually (or automatically if configured) upon detecting new uploads.

---
## To Clone This Repo

```bash
git clone https://github.com/your-username/stripe-data-pipeline.git

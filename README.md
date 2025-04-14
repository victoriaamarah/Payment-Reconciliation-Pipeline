# Payment-Reconciliation-Pipeline

## Overview
This project is an end-to-end data engineering pipeline that generates realistic synthetic data using [Faker](https://faker.readthedocs.io/), modeled after Stripe payment intents. The pipeline produces data in multiple formats—JSON, Parquet, and CSV, which are uploaded to Backblaze B2, the data lake. The raw data is then transformed using Databricks to prepare a clean, structured view that feeds into a Power BI dashboard. The dashboard provides business insights such as payment volume, status breakdowns, and currency distribution.

![Architecture](pipeline/pipeline%20architecture%20flowchart.png)

## Problem Statement
Companies often face challenges in integrating data from disparate sources and formats, processing large-scale data with minimal cost, and transforming it into actionable insights. This project addresses that challenge by combining open source tools and free cloud services to build a reproducible, scalable pipeline. The work demonstrates the ability to manage structured and semi-structured data, perform quality transformations and aggregations using Databricks, and deliver visualizations through Power BI, ultimately empowering businesses to make data-driven decisions without incurring high infrastructure costs.

---

## How to reproduce**Clone the Repository:**

1. **Clone the repository**
2. **Install Dependencies:** Ensure you have Python 3 installed.
    
    ```bash
    pip install -r requirements.txt
    ```
    
    _(This installs packages such as `faker`, `pandas`, `pyarrow`, and `boto3`.)_
    
3. **Set Up Environment Variables:** Store your data lake credentials in a `.env` file that your scripts load:
4. **Run the Pipeline:** From the project root, run:
    
    ```bash
    python scripts/run_pipeline.py
    ```
    
    This one-click script will:
    - Generate synthetic Stripe payment data.  
    - Convert it into JSON, Parquet, and CSV formats. 
    - Upload all files to your Backblaze B2 bucket.
        

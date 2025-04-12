# Payment-Reconciliation-Pipeline

## Overview
This project builds a complete end-to-end data pipeline using synthetic Stripe payment data. The goal is to simulate a real-world scenario where business insights are extracted from payment transactions using modern data engineering tools and BI platforms.

**Data Generation**: Uses [Faker](https://faker.readthedocs.io/) to generate realistic synthetic Stripe payment data modeled on actual API responses. 

## Folder Structure

| Folder         | Description                                      |
|----------------|--------------------------------------------------|
| `data/`        | Some raw data used for the project               |
| `scripts/`     | Scripts to load or transform data                |
| `powerbi/`     | Power BI .pbix file and visual assets            |
| `notebooks/`   | (Optional) Databricks/Colab notebooks            |
| `docs/`        | Documentation and architecture notes             |

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

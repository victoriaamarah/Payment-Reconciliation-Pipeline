from generator import save_json
from convert_format import convert_json_to_parquet, convert_parquet_to_csv
from uploader import upload_to_b2

BUCKET_NAME = "reconciliation-pipeline-data"  # Replace with your actual B2 bucket name

def run():
    json_path = save_json()
    parquet_path = convert_json_to_parquet(json_path)
    upload_to_b2(parquet_path, BUCKET_NAME)

    csv_path = convert_parquet_to_csv(parquet_path)
    upload_to_b2(csv_path, BUCKET_NAME)

if __name__ == "__main__":
    run()

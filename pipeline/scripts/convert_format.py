# convert json to parquet
import pandas as pd
import json

def convert_json_to_parquet(json_file="stripe_payments.json", parquet_file="stripe_payments.parquet"):
    with open(json_file, "r") as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df.to_parquet(parquet_file, index=False)
    print(f"Saved Parquet to {parquet_file}")
    return parquet_file

# convert parquet to csv 

def convert_parquet_to_csv(parquet_path="stripe_payments.parquet", csv_path="stripe_payments.csv"):
    df = pd.read_parquet(parquet_path)
    df.to_csv(csv_path, index=False)
    print(f"Converted Parquet to CSV → {csv_path}")
    return csv_path

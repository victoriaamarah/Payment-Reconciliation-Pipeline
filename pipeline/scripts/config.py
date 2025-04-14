# config.py
import os

B2_BUCKET_NAME = "reconciliation-pipeline-data"
B2_KEY_PREFIX = "raw/stripe"
B2_ENDPOINT_URL = "https://s3.us-east-005.backblazeb2.com"

AWS_ACCESS_KEY = os.getenv("B2_ACCESS_KEY")  # Set in your terminal
AWS_SECRET_KEY = os.getenv("B2_SECRET_KEY")

RECORD_MIN = 50
RECORD_MAX = 100

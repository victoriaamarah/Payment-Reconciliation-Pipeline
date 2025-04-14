import boto3
import os

def upload_to_b2(file_path, bucket_name, object_name=None):
    s3 = boto3.client(
        's3',
        endpoint_url="https://s3.us-east-005.backblazeb2.com",  # Adjust based on your B2 region
        aws_access_key_id=os.getenv("0050178912f8b490000000001"),
        aws_secret_access_key=os.getenv("K005JdvI9++WrGdEKWQ8C6pw9h7143U")
    )

    object_name = object_name or os.path.basename(file_path)

    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"Uploaded {file_path} to B2 bucket '{bucket_name}' as '{object_name}'")
    except Exception as e:
        print(f"Upload failed: {e}")

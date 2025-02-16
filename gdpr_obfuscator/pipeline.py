import boto3
import pandas as pd
from io import StringIO
from gdpr_obfuscator.s3_handler import read_csv_from_s3
from gdpr_obfuscator.obfuscator import obfuscate_pii

def upload_to_s3(bucket_name, file_key, df):
    """
    Uploads a Pandas DataFrame as a CSV file to AWS S3.

    """
    s3 = boto3.client('s3')
    
    try:
    
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_content = csv_buffer.getvalue()


        s3.put_object(Bucket=bucket_name, Key=file_key, Body=csv_content)
        print(f"File uploaded successfully to s3://{bucket_name}/{file_key}")
    
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def process_s3_file(bucket_name, input_key, output_key, pii_fields):
    """
    Reads a CSV from S3, obfuscates PII fields, and uploads the obfuscated file back to S3.
    """
    print(f"Processing file: s3://{bucket_name}/{input_key}")


    df = read_csv_from_s3(bucket_name, input_key)
    if df is None:
        print("Failed to read file from S3.")
        return

    df_obfuscated = obfuscate_pii(df, pii_fields)

    upload_to_s3(bucket_name, output_key, df_obfuscated)

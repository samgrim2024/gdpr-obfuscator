import boto3
import pandas as pd
from io import StringIO

def read_csv_from_s3(bucket_name, file_key):
    """
    Reads a CSV file from AWS S3 and returns a Pandas DataFrame.
    
    """
    s3 = boto3.client('s3')
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        csv_content = response['Body'].read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_content))
        return df
    
    except Exception as e:
        print(f"Error reading CSV from S3: {e}")
        return None

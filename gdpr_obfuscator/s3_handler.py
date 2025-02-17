import boto3
import pandas as pd

def read_csv_from_s3(bucket_name, file_key):
    """
    Reads a CSV file from AWS S3 and returns a Pandas DataFrame.

    :param bucket_name: The name of the S3 bucket.
    :param file_key: The key of the file in the S3 bucket.

    :return: A Pandas DataFrame.
    """
    s3 = boto3.client('s3')
    
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    csv_file = response['Body']

    df = pd.read_csv(csv_file)
    return df

import boto3
import pandas as pd
import io


def read_csv_from_s3(bucket_name, file_key):
    """
    Reads a CSV file from AWS S3 and returns a Pandas DataFrame.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key of the file in the S3 bucket.

    Returns:
        pandas.DataFrame: A Pandas DataFrame containing the CSV data.
    """
    s3 = boto3.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    csv_file = response["Body"]

    df = pd.read_csv(csv_file)
    return df


def read_json_from_s3(bucket_name, file_key):
    """
    Reads a JSON file from an S3 bucket and returns it as a pandas DataFrame.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key of the file in the S3 bucket.

    Returns:
        pandas.DataFrame: A Pandas DataFrame containing the JSON data.
    """
    s3 = boto3.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    json_file = response["Body"]

    df = pd.read_json(json_file, orient="records")
    return df


def read_parquet_from_s3(bucket_name, file_key):
    """
    Reads a Parquet file from an S3 bucket and returns it as a pandas DataFrame.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key of the file in the S3 bucket.

    Returns:
        pandas.DataFrame: A Pandas DataFrame containing the Parquet data.
    """
    s3 = boto3.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    parquet_file = io.BytesIO(response["Body"].read())

    df = pd.read_parquet(parquet_file)

    return df

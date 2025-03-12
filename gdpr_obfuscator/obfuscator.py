import io
import json
from .s3_handler import read_csv_from_s3, read_json_from_s3, read_parquet_from_s3


def obfuscate_csv_from_json(json_string):
    """
    Takes a JSON string, reads a CSV file from S3, obfuscates specified PII fields, and returns a byte-stream.

    :param json_string: JSON string containing S3 file location and fields to obfuscate.
    :return: Byte-stream of the obfuscated CSV file.
    """
    input_data = json.loads(json_string)
    s3_location = input_data["file_to_obfuscate"]
    pii_fields = input_data["pii_fields"]

    # Extract bucket and key from S3 location
    bucket, key = s3_location.replace("s3://", "").split("/", 1)

    # Read the CSV file from S3
    df = read_csv_from_s3(bucket, key)

    # Obfuscate specified fields
    for field in pii_fields:
        if field in df.columns:
            df[field] = "***"

    # Convert DataFrame back to CSV in a byte-stream
    output = io.StringIO()
    df.to_csv(output, index=False)

    # Return byte-stream
    return output.getvalue().encode()


def obfuscate_json_from_json(json_string):
    """
    Takes a JSON string, reads a JSON file from S3, obfuscates specified PII fields, and returns a byte-stream.

    :param json_string: JSON string containing S3 file location and fields to obfuscate.
    :return: Byte-stream of the obfuscated JSON file.
    """
    input_data = json.loads(json_string)
    s3_location = input_data["file_to_obfuscate"]
    pii_fields = input_data["pii_fields"]

    # Extract bucket and key from S3 location
    bucket, key = s3_location.replace("s3://", "").split("/", 1)

    # Read the JSON file from S3
    df = read_json_from_s3(bucket, key)

    # Obfuscate specified fields
    for field in pii_fields:
        if field in df.columns:
            df[field] = "***"

    # Convert object back to JSON in a byte-stream
    output = io.StringIO()
    df.to_json(output, orient="records", index=False)

    # Return byte-stream
    return output.getvalue().encode()


def obfuscate_parquet_from_json(json_string):
    """
    Takes a JSON string, reads a Parquet file from S3, obfuscates specified PII fields, and returns a byte-stream.

    :param json_string: JSON string containing S3 file location and fields to obfuscate.
    :return: Byte-stream of the obfuscated Parquet file.
    """
    input_data = json.loads(json_string)
    s3_location = input_data["file_to_obfuscate"]
    pii_fields = input_data["pii_fields"]

    # Extract bucket and key from S3 location
    bucket, key = s3_location.replace("s3://", "").split("/", 1)

    # Read the Parquet file from S3
    df = read_parquet_from_s3(bucket, key)

    # Obfuscate specified fields
    for field in pii_fields:
        if field in df.columns:
            df[field] = "***"

    # Convert object back to Parquet in a byte-strea
    output = io.BytesIO()
    df.to_parquet(output, index=False)

    # return byte-stream
    return output.getvalue()

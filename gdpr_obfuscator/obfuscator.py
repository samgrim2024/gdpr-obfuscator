import io
import json
from s3_handler import read_csv_from_s3

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
            df[field] = '***'
    
    # Convert DataFrame back to CSV in a byte-stream
    output = io.StringIO()
    df.to_csv(output, index=False)
    
    # Return byte-stream
    return output.getvalue().encode()
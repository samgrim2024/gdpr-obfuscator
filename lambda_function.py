import json
import boto3
from gdpr_obfuscator.pipeline import process_s3_file

PII_FIELDS = ["name", "email", "phone_number"]

def lambda_handler(event, context):
    """
    AWS Lambda handler that triggers on S3 file uploads.
    """
    try:
        s3_event = event['Records'][0]['s3']
        bucket_name = s3_event['bucket']['name']
        input_key = s3_event['object']['key']
        
        print(f"Received event for file: s3://{bucket_name}/{input_key}")

        output_key = f"processed/{input_key}"

        process_s3_file(bucket_name, input_key, output_key, PII_FIELDS)

        return {
            "statusCode": 200,
            "body": json.dumps(f"Successfully processed {input_key}")
        }

    except Exception as e:
        print(f"Error processing file: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps("Error processing file")
        }

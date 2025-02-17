from unittest.mock import patch, MagicMock
import pandas as pd
from gdpr_obfuscator.s3_handler import read_csv_from_s3
import io

@patch('gdpr_obfuscator.s3_handler.boto3.client')
def test_read_csv_from_s3(mock_boto_client):
    # Mock the S3 client and response
    mock_s3 = MagicMock()
    mock_response = {
        'Body': io.StringIO('name,email,age\nJohn,john@example.com,30\n')
    }
    mock_s3.get_object.return_value = mock_response
    mock_boto_client.return_value = mock_s3
    
    # Call the function
    df = read_csv_from_s3('bucket', 'key')
    
    # Verify the DataFrame
    expected_df = pd.DataFrame({
        'name': ['John'],
        'email': ['john@example.com'],
        'age': [30]
    })
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Verify that the mock was called correctly
    mock_boto_client.assert_called_once_with('s3')
    mock_s3.get_object.assert_called_once_with(Bucket='bucket', Key='key')

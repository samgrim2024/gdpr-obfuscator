import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from gdpr_obfuscator.s3_handler import read_csv_from_s3

@patch("gdpr_obfuscator.s3_handler.boto3.client")
def test_read_csv_from_s3(mock_boto3_client):
    """
    Test reading a CSV file from S3.
    """
    
    mock_s3 = MagicMock()
    mock_boto3_client.return_value = mock_s3
    mock_s3.get_object.return_value = {'Body': MagicMock(read=MagicMock(return_value=b"col1,col2\nval1,val2"))}

  
    df = read_csv_from_s3("test-bucket", "test-file.csv")

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 2)  
    assert df.iloc[0]["col1"] == "val1"
    assert df.iloc[0]["col2"] == "val2"

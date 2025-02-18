import pytest
from unittest.mock import patch
import json
import pandas as pd
from gdpr_obfuscator import obfuscate_csv_from_json
from gdpr_obfuscator import obfuscate_json_from_json


@patch("gdpr_obfuscator.obfuscator.read_csv_from_s3")
def test_obfuscate_csv_from_json(mock_read_csv):
    # Create a mock DataFrame
    mock_df = pd.DataFrame(
        {"name": ["John"], "email": ["john@example.com"], "age": [30]}
    )
    mock_read_csv.return_value = mock_df

    # JSON input
    json_input = json.dumps(
        {"file_to_obfuscate": "s3://bucket/key.csv", "pii_fields": ["name", "email"]}
    )

    # Call the function
    result = obfuscate_csv_from_json(json_input)

    # Verify the result
    expected_output = "name,email,age\n***,***,30\n".encode()
    assert result == expected_output

    # Verify that the mock was called correctly
    mock_read_csv.assert_called_once_with("bucket", "key.csv")


@patch("gdpr_obfuscator.obfuscator.read_csv_from_s3")
def test_obfuscate_csv_with_no_pii_fields(mock_read_csv):
    # Create a mock DataFrame
    mock_df = pd.DataFrame(
        {"name": ["John"], "email": ["john@example.com"], "age": [30]}
    )
    mock_read_csv.return_value = mock_df

    # JSON input
    json_input = json.dumps(
        {"file_to_obfuscate": "s3://bucket/key.csv", "pii_fields": []}
    )

    # Call the function
    result = obfuscate_csv_from_json(json_input)

    # Verify the result
    expected_output = "name,email,age\nJohn,john@example.com,30\n".encode()
    assert result == expected_output

    # Verify that the mock was called correctly
    mock_read_csv.assert_called_once_with("bucket", "key.csv")


@patch("gdpr_obfuscator.obfuscator.read_json_from_s3")
def test_obfuscate_json_from_json(mock_read_json):
    # Create a mock DataFrame
    mock_df = pd.DataFrame(
        {"name": ["John"], "email": ["john@example.com"], "age": [30]}
    )
    mock_read_json.return_value = mock_df

    # JSON input
    json_input = json.dumps(
        {"file_to_obfuscate": "s3://bucket/key.json", "pii_fields": ["name", "email"]}
    )

    # Call the function
    result = obfuscate_json_from_json(json_input)

    # Verify the result
    expected_output = '[{"name":"***","email":"***","age":30}]'.encode()
    assert result == expected_output

    # Verify that the mock was called correctly
    mock_read_json.assert_called_once_with("bucket", "key.json")


@patch("gdpr_obfuscator.obfuscator.read_json_from_s3")
def test_obfuscate_json_with_no_pii_fields(mock_read_json):
    # Create a mock DataFrame
    mock_df = pd.DataFrame(
        {"name": ["John"], "email": ["john@example.com"], "age": [30]}
    )
    mock_read_json.return_value = mock_df

    # JSON input
    json_input = json.dumps(
        {"file_to_obfuscate": "s3://bucket/key.json", "pii_fields": []}
    )

    # Call the function
    result = obfuscate_json_from_json(json_input)

    # Verify the result
    expected_output = '[{"name":"John","email":"john@example.com","age":30}]'.encode()
    assert result == expected_output

    # Verify that the mock was called correctly
    mock_read_json.assert_called_once_with("bucket", "key.json")

import pytest
import pandas as pd
from gdpr_obfuscator.obfuscator import obfuscate_pii

def test_obfuscate_pii():
    """
    Test obfuscation of PII fields.
    """
   
    data = {
        "name": ["Alice", "Bob"],
        "email": ["alice@example.com", "bob@example.com"],
        "age": [25, 30]
    }
    df = pd.DataFrame(data)

   
    pii_fields = ["name", "email"]

    
    obfuscated_df = obfuscate_pii(df, pii_fields)

    
    assert all(obfuscated_df["name"] == "***")
    assert all(obfuscated_df["email"] == "***")

   
    assert obfuscated_df["age"].equals(df["age"])

def test_obfuscate_pii_column_not_found():
    """
    Test obfuscation when a specified column is missing.
    """
    df = pd.DataFrame({"name": ["Alice"], "age": [25]})
    pii_fields = ["email"]  

    obfuscated_df = obfuscate_pii(df, pii_fields)

    assert "email" not in obfuscated_df.columns  
    assert obfuscated_df["name"][0] == "Alice"  

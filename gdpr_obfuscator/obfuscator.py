import pandas as pd

def obfuscate_pii(df, pii_fields):
    """
    Obfuscates specified PII fields in a Pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input data must be a Pandas DataFrame.")

    for field in pii_fields:
        if field in df.columns:
            df[field] = "***" 
        else:
            print(f"Warning: Column '{field}' not found in the DataFrame.")

    return df

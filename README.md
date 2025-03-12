# GDPR Obfuscator

A package to obfuscate PII data in CSV files stored in S3.

## Installation

### For Development:

Clone the repository:
```sh
git clone https://github.com/samgrim2024/gdpr-obfuscator.git
```

Change directory to the cloned repository:
```sh
cd gdpr-obfuscator
```

It's best practice to install the package in a virtual environment:
```sh
python3 -m venv venv
```
Activate the virtual environment:
- On macos/linux:
```sh
source venv/bin/activate
```

Install the requirements:
```sh
pip install -r requirements.txt
```

To run the tests, you have to set the `PYTHONPATH` environment variable to the current directory so that the package can be found:
```sh
export PYTHONPATH=$(pwd)
pytest tests/
```

### For Production:

You can install the package using pip:

#### Install directly from the repository:
```sh
pip install git+https://github.com/samgrim2024/gdpr-obfuscator.git
```

#### Install from a local clone:
Navigate to the cloned repository and run:
```sh
pip install .
```

For development, you can install the package in editable mode:
```sh
pip install -e .
```

## Requirements

The package will automatically install the required dependencies:

- pandas
- pyarrow (for parquet support)
- boto3

## Usage

### Obfuscate CSV from S3

To obfuscate a CSV file stored in S3, use the `obfuscate_csv_from_json` function. Below is an example:

```python
import json
from gdpr_obfuscator import obfuscate_csv_from_json

# JSON string containing S3 file location and fields to obfuscate
json_string = json.dumps({
    "file_to_obfuscate": "s3://your-bucket-name/path/to/your-file.csv",
    "pii_fields": ["name", "email"]
})

# Obfuscate the CSV file
obfuscated_csv = obfuscate_csv_from_json(json_string)

# Save the obfuscated CSV to a file
with open("obfuscated_file.csv", "wb") as f:
    f.write(obfuscated_csv)
```

### Obfuscate JSON from S3

To obfuscate a JSON file stored in S3, user the `obfuscate_json_from_json` function. Below is an example:

```python
import json
from gdpr_obfuscator import obfuscate_json_from_json

# JSON string containing S3 file location and fields to obfuscate
json_string = json.dumps({
    "file_to_obfuscate": "s3://your-bucket-name/path/to/your-file.json",
    "pii_fields": ["name", "email"]
})

# Obfuscate the JSON file
obfuscated_json = obfuscate_json_from_json(json_string)

# Save the obfuscated JSON to a file
with open("obfuscated_file.json", "wb") as f:
    f.write(obfuscated_json)
```

### Obfuscate Parquet from S3

To obfuscate a Parquet file stored in S3, user the `obfuscate_parquet_from_json` function. Below is an example:

```python
import json
from gdpr_obfuscator import obfuscate_parquet_from_json

# JSON string containing S3 file location and fields to obfuscate
json_string = json.dumps({
    "file_to_obfuscate": "s3://your-bucket-name/path/to/your-file.parquet",
    "pii_fields": ["name", "email"]
})

# Obfuscate the Parquet file
obfuscated_parquet = obfuscate_parquet_from_json(json_string)

# Save the obfuscated Parquet to a file
with open("obfuscated_file.parquet", "wb") as f:
    f.write(obfuscated_parquet)
```

## License

This project is licensed under the MIT License.

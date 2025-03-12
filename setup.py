from setuptools import setup, find_packages

setup(
    name="gdpr-obfuscator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pyarrow",
        "boto3"
    ],
    description="A package to obfuscate PII data in CSV files stored in S3.",
    python_requires='>=3.6',
)

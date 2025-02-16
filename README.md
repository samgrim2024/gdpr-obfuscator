## Deployment Options
This project can run in two modes:

1. **AWS Mode** 
   - Connects to real AWS S3 & Lambda services.
   - Requires AWS credentials.

2. **Local Development Mode** (Using LocalStack & Docker)
   - Simulates AWS services locally.
   - No AWS account needed.
   - Requires **Docker** and **LocalStack** installed.

## Running Locally with LocalStack
To test without AWS, install Docker and run:

```bash
localstack start

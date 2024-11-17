## Requirements
- AWS CLI
- Docker
- Python >= 3.9
- Terraform

## Setup
```bash
python deploy.py
```

Setup-scriptet kommer returnera api-url efter att LocalStack och Terraform har gjort sitt.

## Example Curl
```bash
curl -X POST http://localhost:4566/_aws/execute-api/<API_ID>/dev/uppercase \
  -H "Content-Type: application/json" \
  -d '{"text": "lorem ipsum"}'
```

## Overview
Om du har ett konto på LocalStack så kan du se alla tjänster och logs som körs på din [Dashboard](https://app.localstack.cloud)

## Remove container
```bash
docker-compose down -v
```
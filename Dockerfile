# Dockerfile for Mind TEE
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Entry point: run the TEE CLI demonstration
CMD ["python", "-m", "mind_tee.cli.mindtee_cli", "--input-data", "confidential_input"]

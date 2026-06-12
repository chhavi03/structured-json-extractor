#!/bin/bash
set -e

echo "==================================================="
echo "Stopping and removing existing container if active..."
echo "==================================================="
docker stop structured-json-extractor-app >/dev/null 2>&1 || true
docker rm structured-json-extractor-app >/dev/null 2>&1 || true

echo "==================================================="
echo "Building Docker image for Structured JSON Extractor..."
echo "==================================================="
docker build -t structured-json-extractor:latest .

echo "==================================================="
echo "Starting Container..."
echo "==================================================="
if [ -f .env ]; then
    echo "Loading environment variables from .env file..."
    docker run -d --name structured-json-extractor-app -p 8501:8501 --env-file .env structured-json-extractor:latest
else
    echo "Warning: No .env file found. Running without preconfigured environment variables..."
    docker run -d --name structured-json-extractor-app -p 8501:8501 structured-json-extractor:latest
fi

echo "==================================================="
echo "Container started successfully!"
echo "Access the application dashboard at: http://localhost:8501"
echo "==================================================="

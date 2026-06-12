# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install compilation tools for potential dependency build requirements
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies to user directory to keep runner clean
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Production runtime stage
FROM python:3.11-slim AS runner

WORKDIR /app

# Copy installed python dependencies from builder stage
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# Ensure local packages are on the binary PATH
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy application layers
COPY app/ app/
COPY main.py .

# Expose standard Streamlit port
EXPOSE 8501

# Streamlit command configuration
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

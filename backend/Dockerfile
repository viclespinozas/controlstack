# syntax=docker/dockerfile:1
# ===========================
# Stage 1: Builder
# ===========================
FROM python:3.12-slim AS builder

# Prevent Python from writing .pyc files and buffering logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install build tools (only for this stage)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for layer caching
COPY requirements.txt .

# Check and install latest pip version
RUN pip install --upgrade pip

# Install dependencies into a local user directory
RUN pip install --user --no-cache-dir -r requirements.txt

# ===========================
# Stage 2: Runner
# ===========================
FROM python:3.12-slim

# Security best practice — non-root user
RUN useradd -m appuser
USER appuser

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Ensure local bin is in PATH
ENV PATH=/home/appuser/.local/bin:$PATH

# Copy only necessary app code
COPY ./src ./src

# Expose FastAPI default port
EXPOSE 8000

# Run FastAPI with uvicorn (high-perf ASGI server)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["fastapi", "run", "main.py", "--port", "8000"]

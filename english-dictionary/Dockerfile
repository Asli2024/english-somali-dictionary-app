# Single stage
FROM python:3.12-alpine

WORKDIR /app

# Install build and runtime dependencies
RUN apk add --no-cache --no-scripts \
    gcc \
    musl-dev \
    libffi-dev \
    curl && \
    pip install --no-cache-dir --upgrade pip

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN addgroup -g 1000 appgroup && \
    adduser -u 1000 -D -G appgroup appuser

# Copy application code
COPY --chown=appuser:appgroup ./app ./app
COPY --chown=appuser:appgroup ./static ./static

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

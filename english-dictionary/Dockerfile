# Build stage
FROM python:3.12-alpine AS builder

WORKDIR /app

RUN apk add --no-cache --no-scripts --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev && \
    pip install --no-cache-dir "pip>=25.3,<26"

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt && \
    apk del --no-scripts .build-deps

# Runtime stage
FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/install/bin:$PATH \
    PYTHONPATH=/install/lib/python3.12/site-packages

RUN apk add --no-cache --no-scripts curl && \
    addgroup -g 1000 appgroup && \
    adduser -u 1000 -D -G appgroup appuser

COPY --from=builder /install /install
COPY --chown=appuser:appgroup ./app ./app
COPY --chown=appuser:appgroup ./static ./static

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

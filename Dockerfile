# ---- Stage 1: Build stage ----
    FROM python:3.12-slim AS builder

    WORKDIR /app
    
    COPY requirements.txt .
    RUN pip install --no-cache-dir --upgrade pip \
        && pip install --no-cache-dir --prefix=/install -r requirements.txt
    
    # ---- Stage 2: image finale minimale ----
    FROM python:3.12-slim
    
    WORKDIR /app
    
    COPY --from=builder /install /usr/local
    COPY script.py .
    
    CMD ["python", "script.py"]
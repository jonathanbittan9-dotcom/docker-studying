# syntax=docker/dockerfile:1

# ============ STAGE 1: BUILDER (fat, throwaway) ============
FROM python:3.12-slim-bookworm AS builder

ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Native build toolchain — needed for wheels like psycopg2 / tokenizers.
# It lives ONLY in this stage; runtime never gets it.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Create the venv at /opt/venv so stage 2 can copy a self-contained interpreter
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install -r requirements.txt

# ============ STAGE 2: RUNTIME (thin, hardened) ============
FROM python:3.12-slim-bookworm AS runtime

# Python hygiene: no .pyc litter, unbuffered logs (critical for `docker logs`)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# --- Non-root user: fixed high UID (10001) for Kubernetes-friendliness ---
RUN groupadd --gid 10001 bot \
    && useradd --uid 10001 --gid bot --shell /usr/sbin/nologin --create-home bot

# Runtime shared libs only (no compiler!) for psycopg
RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

# The ONLY thing we carry over from stage 1
COPY --from=builder /opt/venv /opt/venv

WORKDIR /app
# chown at copy-time so files are already owned by bot — not root
COPY --chown=bot:bot src/ ./src/

USER bot

CMD ["python", "-m", "src.main"]

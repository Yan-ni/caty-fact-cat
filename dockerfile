# Step 1: Build stage to install UV
FROM python:3.12-slim-bookworm AS builder

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and run the UV installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

FROM python:3.11

# Copy UV binary from build stage
COPY --from=builder /root/.local/bin/uv /root/.local/bin/uv

# add UV to path
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

COPY pyproject.toml .

COPY uv.lock .

RUN uv sync --locked

COPY src/ .

CMD ["uv", "run", "main.py"]
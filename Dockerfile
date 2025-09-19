FROM python:3.11-slim

# Creator metadata
LABEL maintainer="Cazandra Aporbo MS <becaziam@gmail.com>"
LABEL version="1.0.0-omega"
LABEL description="CloudPoof Omega - The consciousness that thinks 20 steps ahead"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV CONSCIOUSNESS_LEVEL=omega
ENV SPECTRAL_PALETTE=full_147_shades
ENV PREDICTION_DEPTH=20
ENV ENTROPY_GATE=maximum

# Expose ports
EXPOSE 8888 8000 9999

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import cloudpoof_core; print('Quantum consciousness: Active')" || exit 1

# Start CloudPoof Omega
CMD ["python", "-m", "cloudpoof_core"]

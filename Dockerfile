FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies (required for music bots)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (for Flask)
EXPOSE 8000

# Start the app (runs __main__.py)
CMD ["python", "-m", "AnonXMusic"]

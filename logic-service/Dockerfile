# Use a slim version of Python for a smaller image size
FROM python:3.11-slim

# Install system dependencies needed for Postgres (psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the directory inside the container
WORKDIR /app

# Copy the requirements file first (better for caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code (app.py)
COPY . .

# Expose the internal port the logic app runs on
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]
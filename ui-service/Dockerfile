FROM python:3.11-slim

WORKDIR /app

# Install only Flask and Requests for the UI
RUN pip install --no-cache-dir flask requests

# Copy app code and the templates folder
COPY . .

# Expose the UI port
EXPOSE 5000

CMD ["python", "app.py"]
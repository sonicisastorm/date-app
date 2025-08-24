FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

# Expose port 80
EXPOSE 80

# Run app
ENTRYPOINT ["python", "app.py"]

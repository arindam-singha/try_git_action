# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files to container
COPY first_project .

# Run the Python script
CMD ["python", "first_script.py"]

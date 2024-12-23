# Use a Python base image
FROM python:3.9-slim

# Copy the application files into the container
COPY calculator.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "calculator.py"]

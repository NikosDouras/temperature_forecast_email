# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY projectFiles/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY projectFiles /app/projectFiles

# Ensure the working directory is set correctly
WORKDIR /app/projectFiles

# Create an empty email_list.txt file
RUN touch /app/projectFiles/email_list.txt

# Set the entry point command
CMD ["python", "email_forecast.py"]


# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY temperature_forecast_email/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY temperature_forecast_email /app/temperature_forecast_email

# Set the working directory to temperature_forecast_email
WORKDIR /app/temperature_forecast_email

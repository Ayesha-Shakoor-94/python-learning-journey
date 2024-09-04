# Base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Ensure root user
USER root



# Command to run application
CMD ["python", "guessing_game.py"]

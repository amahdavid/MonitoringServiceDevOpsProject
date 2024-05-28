# Description: Dockerfile for the Flask application

# Use the official image as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /src

# Copy the dependencies file to the working directory
COPY requirements.txt /src/

# Install any dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt -v

# Copy the content of the local src directory to the working directory
COPY . .

# Envirnoment variables
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 8000
CMD ["flask", "run"]


## Overview

## Steps
- Create an app.py file, which will be a simple flask application
- Create a Dockerfile and add the necessary commands to build the docker image

## Requirements
- AWS Account
- Docker
- Python 3.8
- Pip
- Kubernetes

## Commands
- `pip install -r requirements.txt`: Install the required packages
- `docker build -t dev-ops-project .`: Build the docker image
- `docker run -p 8000:8000 dev-ops-project`: Run the docker image
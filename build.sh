#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -o errexit

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Run database migrations
python manage.py migrate

# Create a superuser if it doesn't exist
if [ ! -z "$DJANGO_SUPERUSER_USERNAME" ] && [ ! -z "$DJANGO_SUPERUSER_EMAIL" ] && [ ! -z "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py createsuperuser --noinput || true
fi

# Execute the CMD from the Dockerfile
exec "$@"
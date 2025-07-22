#!/bin/bash

echo "Executando migrations..."
python manage.py migrate --noinput

exec "$@"

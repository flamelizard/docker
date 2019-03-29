#!/bin/bash

# stop execution on non-zero command exit code
set -e

if [ "$ENV" = "DEV" ]; then
    echo "Running development server"
#    replace current shell, do not fork off
    exec python "identidock.py"
elif [ "$ENV" = 'UNIT' ]; then
    echo "Running tests"
    exec python tests.py
else
    echo "Running production server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py \
            --callable app --stats 0.0.0.0:9191
fi
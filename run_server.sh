#!/bin/bash
until gunicorn main:main_start --reload --bind 0.0.0.0:8080 --worker-class aiohttp.worker.GunicornWebWorker 2>/dev/null; do
  echo "Database is unavailable - sleeping (10s)"
  sleep 10
done
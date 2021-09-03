#! /usr/bin/env bash
set -e

python /app/app/celery_pre_start.py

celery -A app.worker worker -l info -Q main-queue -c 1

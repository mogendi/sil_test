#!/bin/bash
echo "Starting up celery workers"

echo "Dropping all existing workers"
pkill -9 -f celery

REPLICAS=${REPLICAS:-1}
echo "Starting up ${REPLICAS} celery workers"
cd src &&
$HOME/.local/bin/pipenv run celery -A store worker -c $REPLICAS -Q notifications-q -l INFO

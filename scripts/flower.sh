#!/bin/sh

cd src

until timeout 10 $HOME/.local/bin/pipenv run celery -A kinetic_schools_api inspect ping; do
    >&2 echo "Celery workers not available"
done

echo 'Starting flower'
$HOME/.local/bin/pipenv run celery -A store flower
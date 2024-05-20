#!/usr/bin/env bash

set -e
set -x

black src --check
isort --check-only src
flake8 src

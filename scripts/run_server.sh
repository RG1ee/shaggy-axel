#!/bin/bash

# Create Environment "Virtual Environment file path", "Deploy Flag file path"
VENV=./.venv

# Check if not exists VENV, -> create VENV
if [ ! -d $VENV ]; then
    `which python3` -m venv $VENV
    $VENV/bin/pip install -U pip
fi

# Installing requirements from file
$VENV/bin/pip install -r requirements.txt

# Do migrate (for creating tables in the database) 
$VENV/bin/python src/manage.py migrate
$VENV/bin/python src/manage.py collectstatic --no-input

$VENV/bin/python src/manage.py runserver 0.0.0.0:8000
echo "Run Django"

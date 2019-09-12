#!/bin/bash

echo 'Creating environment variables for development'
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_export=development
export FLASK_DEBUG=1
export FLASK_APP=autoapp.py
export DATABASE_URL="sqlite:////tmp/dev.db"
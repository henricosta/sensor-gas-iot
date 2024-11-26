#!/bin/bash

set -e

echo "Navigating to the api/ directory..."
cd api/

python create_database.py

python inserir_mock_data.py

echo "Starting the API..."
python app.py

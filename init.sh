#!/bin/bash

set -e

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Navigating to the api/ directory..."
cd api/

python create_database.py

python inserir_mock_data.py

echo "Starting the API..."
python app.py

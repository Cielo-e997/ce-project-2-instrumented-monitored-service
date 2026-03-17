#!/bin/bash

set -e

echo "Starting deployment for order-service..."

if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting application..."
python3 server.py
#!/usr/bin/env bash

echo "Validating personal diary application setup..."

# Check that required directories exist
echo "Checking directory structure..."
if [ ! -d "backend" ]; then
    echo "ERROR: backend directory missing"
    exit 1
fi

if [ ! -d "frontend" ]; then
    echo "ERROR: frontend directory missing"
    exit 1
fi

if [ ! -f "Dockerfile" ]; then
    echo "ERROR: Dockerfile missing"
    exit 1
fi

if [ ! -f "compose.yaml" ]; then
    echo "ERROR: compose.yaml missing"
    exit 1
fi

# Check that core Python files exist
echo "Checking backend files..."
if [ ! -f "backend/app/main.py" ]; then
    echo "ERROR: main.py missing"
    exit 1
fi

if [ ! -f "backend/requirements.txt" ]; then
    echo "ERROR: requirements.txt missing"
    exit 1
fi

# Check that core frontend files exist
echo "Checking frontend files..."
if [ ! -f "frontend/src/App.tsx" ]; then
    echo "ERROR: App.tsx missing"
    exit 1
fi

echo "Setup validation completed successfully!"
echo ""
echo "To start the application:"
echo "1. docker compose build"
echo "2. docker compose up -d"
echo "3. Visit http://localhost:8888"
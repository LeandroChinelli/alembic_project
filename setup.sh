#!/bin/bash
python3 -m venv venv
source venv/bin/activate

python -m pip install -r requirements.txt

docker run --name postgresql -e POSTGRES_PASSWORD=testpassword -e POSTGRES_USER=testuser -e POSTGRES_DB=testuser -p 5432:5432 -d postgres:14.3-alpine
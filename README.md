# Flask to FastAPI

This repository contains equivalent sample applications built with Flask and
FastAPI. Both applications serve a page and use the same text-classification
model.

## Installation

From the repository root, install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Run the Flask app

```bash
python3 flask_app/main.py
```

The app runs at <http://127.0.0.1:5000>.

## Run the FastAPI app

```bash
uvicorn fastapi_app.main:app --reload
```

The app runs at <http://127.0.0.1:8000>. Interactive API documentation is
available at <http://127.0.0.1:8000/docs>.

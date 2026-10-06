# Task 06 — Real-Time ML Inference REST API & Capstone

## Overview
Production-style FastAPI service for real-time ML inference.

## Architecture
Client → FastAPI `/predict` → Pydantic validation → saved ML model → probability/confidence → JSON response.

## Files
- `app.py` — FastAPI server
- `model/champion_model.joblib` — trained model
- `requirements.txt` — pinned dependencies
- `Dockerfile` — container setup
- `test_app.py` — unit tests
- `README.md` — documentation

## Run
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Example request
```json
{"Pclass":3,"Sex":"male","Age":22,"SibSp":1,"Parch":0,"Fare":7.25,"Embarked":"S"}
```

## Tests
```bash
pytest -q
```

## Docker
```bash
docker build -t task06-ml-api .
docker run -p 8000:8000 task06-ml-api
```

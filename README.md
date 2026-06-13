# FastAPI_Churn_Scoring_Service_Reproducible_ML_Workflow
Capstone Project

# FastAPI Churn Prediction Service

## Project Overview

This project provides a FastAPI service that loads a churn prediction model and exposes REST APIs for real-time and batch churn scoring.

The API is designed to support CRM and retention systems by returning churn probability, predicted class, and a human-readable risk explanation.

---

## Project Structure

app/
├── main.py
├── schemas.py
└── utils.py

tests/
└── test_api.py

model.pkl
train_model.py
requirements.txt
monitoring_plan.md

---

## Installation

```bash
pip install -r requirements.txt
```

## Train Model

```bash
python train_model.py
```

This creates:

```text
model.pkl
```

## Run API

```bash
uvicorn app.main:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Endpoints

### GET /health

Response:

```json
{
  "status": "ok"
}
```

### POST /predict

Sample Request

```json
{
  "recency": 30,
  "frequency": 5,
  "monetary": 2500,
  "support_tickets": 2,
  "event_count": 20
}
```

Sample Response

```json
{
  "churn_probability": 0.72,
  "predicted_class": 1,
  "risk_level": "high",
  "risk_explanation": "Low activity and elevated support complaints indicate increased churn risk."
}
```

### POST /batch_predict

Accepts multiple customer records and returns predictions for each.

---

## Run Tests

```bash
pytest tests/test_api.py
```

---

## Model Notes

The model was trained using customer behavior features available before the churn observation window.

Potential leakage features were excluded from training.

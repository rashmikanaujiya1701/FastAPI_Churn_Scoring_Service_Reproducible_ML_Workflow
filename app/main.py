from fastapi import FastAPI
from app.schemas import CustomerFeatures, BatchRequest
from app.utils import (
    generate_risk_explanation,
    get_risk_level
)

import pandas as pd
import joblib

app = FastAPI(
    title="Churn Prediction API"
)

model = joblib.load("model.pkl")


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.post("/predict")
def predict(customer: CustomerFeatures):

    df = pd.DataFrame([customer.dict()])

    probability = float(
        model.predict_proba(df)[0][1]
    )

    prediction = int(
        probability >= 0.50
    )

    return {
        "churn_probability": round(probability,4),
        "predicted_class": prediction,
        "risk_level": get_risk_level(probability),
        "risk_explanation":
        generate_risk_explanation(probability)
    }


@app.post("/batch_predict")
def batch_predict(
    request: BatchRequest
):

    outputs = []

    for customer in request.customers:

        df = pd.DataFrame(
            [customer.dict()]
        )

        probability = float(
            model.predict_proba(df)[0][1]
        )

        outputs.append(
            {
                "churn_probability":
                round(probability,4),

                "predicted_class":
                int(probability >= 0.50),

                "risk_level":
                get_risk_level(probability)
            }
        )

    return outputs

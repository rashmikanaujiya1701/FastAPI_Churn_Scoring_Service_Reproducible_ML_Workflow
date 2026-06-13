from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200


def test_predict():

    payload = {
        "recency":30,
        "frequency":5,
        "monetary":2000,
        "support_tickets":1,
        "event_count":25
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    assert (
        "churn_probability"
        in response.json()
    )


def test_batch_predict():

    payload = {
        "customers":[
            {
                "recency":10,
                "frequency":6,
                "monetary":5000,
                "support_tickets":0,
                "event_count":80
            },
            {
                "recency":120,
                "frequency":1,
                "monetary":500,
                "support_tickets":5,
                "event_count":2
            }
        ]
    }

    response = client.post(
        "/batch_predict",
        json=payload
    )

    assert response.status_code == 200

from src.predict import predict


def test_prediction_output():
    order = {
        "purchase_hour": 10,
        "purchase_day_of_week": 2,
        "purchase_month": 5,
        "purchase_year": 2018,
        "approval_delay_hours": 1.5,
        "estimated_delivery_days": 20,
    }

    result = predict(order)

    assert "prediction" in result
    assert "probability" in result
    assert result["prediction"] in ["late", "on time"]
    assert 0 <= result["probability"] <= 1

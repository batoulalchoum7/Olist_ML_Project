import pytest

from src.validation import validate_input


def test_valid_input():
    order = {
        "purchase_hour": 10,
        "purchase_day_of_week": 2,
        "purchase_month": 5,
        "purchase_year": 2018,
        "approval_delay_hours": 1.5,
        "estimated_delivery_days": 20,
    }

    assert validate_input(order) is True


def test_invalid_hour():
    order = {
        "purchase_hour": 25,
        "purchase_day_of_week": 2,
        "purchase_month": 5,
        "purchase_year": 2018,
        "approval_delay_hours": 1.5,
        "estimated_delivery_days": 20,
    }

    with pytest.raises(ValueError):
        validate_input(order)
        
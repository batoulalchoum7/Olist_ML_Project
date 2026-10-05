import json
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
EXPECTATIONS_PATH = BASE_DIR / "config" / "expectations" / "order_expectations.json"


def load_expectations():
    with open(EXPECTATIONS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_input(order):
    expectations = load_expectations()
    df = pd.DataFrame([order])

    required_columns = expectations["required_columns"]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if df[required_columns].isnull().any().any():
        raise ValueError("Input contains missing values.")

    for column, limits in expectations["ranges"].items():
        minimum, maximum = limits

        if minimum is not None and not df[column].ge(minimum).all():
            raise ValueError(f"{column} must be >= {minimum}.")

        if maximum is not None and not df[column].le(maximum).all():
            raise ValueError(f"{column} must be <= {maximum}.")

    return True

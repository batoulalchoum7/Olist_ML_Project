import time
import pandas as pd

from config.config import (
    MODEL_PATH,
    IMPUTER_PATH,
    SCALER_PATH,
    FEATURE_LIST_PATH,
    THRESHOLD,
)
from src.utils import load_artifact, setup_logger
from src.validation import validate_input


logger = setup_logger()

model = load_artifact(MODEL_PATH)
imputer = load_artifact(IMPUTER_PATH)
scaler = load_artifact(SCALER_PATH)
feature_list = load_artifact(FEATURE_LIST_PATH)

MODEL_VERSION = "1.0"


def predict(order):
    start_time = time.time()

    logger.info(f"Prediction request: {order}")

    try:
        validate_input(order)
        df = pd.DataFrame([order])
        df = df[feature_list]

        df = imputer.transform(df)

        df = pd.DataFrame(scaler.transform(df), columns=feature_list)

        probability = model.predict_proba(df)[0][1]
        prediction = "late" if probability >= THRESHOLD else "on time"

        latency = time.time() - start_time

        logger.info(
            f"Prediction output: prediction={prediction}, "
            f"probability={probability:.4f}, "
            f"latency={latency:.4f}s, "
            f"model_version={MODEL_VERSION}"
        )

        return {
            "prediction": prediction,
            "probability": float(probability),
            "model_version": MODEL_VERSION,
        }

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise

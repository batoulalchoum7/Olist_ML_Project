import joblib
import logging
import sys


def load_artifact(path):
    return joblib.load(path)


def setup_logger():
    logger = logging.getLogger("olist_ml")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler("prediction.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

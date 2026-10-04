from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Model artifacts
MODEL_PATH = BASE_DIR / "models" / "random_forest_model.pkl"
IMPUTER_PATH = BASE_DIR / "models" / "imputer.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
FEATURE_LIST_PATH = BASE_DIR / "models" / "feature_list.pkl"

# Prediction
THRESHOLD = 0.5
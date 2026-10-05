import mlflow
import mlflow.sklearn

from config.config import MODEL_PATH
from src.utils import load_artifact


MODEL_VERSION = "1.0"


def log_model():
    model = load_artifact(MODEL_PATH)

    mlflow.set_experiment("olist_late_delivery")

    with mlflow.start_run():
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_param("model_version", MODEL_VERSION)

        mlflow.sklearn.log_model(
            model,
            name="random_forest_model",
            skops_trusted_types=["sklearn.tree._tree.Tree"],
        )

        print("Model logged successfully.")


if __name__ == "__main__":
    log_model()

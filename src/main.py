from fastapi import FastAPI

from config.schema import OrderRequest, PredictionResponse
from src.predict import predict


app = FastAPI(title="Olist Late Delivery Prediction API")


@app.get("/")
def root():
    return {"message": "Olist inference service is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/model-info")
def model_info():
    return {
        "model_name": "random_forest",
        "model_version": "1"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_order(order: OrderRequest):
    return predict(order.model_dump())


@app.post("/predict/batch")
def predict_batch(orders: list[OrderRequest]):
    return [
        predict(order.model_dump())
        for order in orders
    ]
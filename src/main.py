from fastapi import FastAPI

from config.schema import OrderRequest, PredictionResponse
from src.predict import predict


app = FastAPI(title="Olist Late Delivery Prediction API")


@app.get("/")
def root():
    return {"message": "Olist inference service is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict_order(order: OrderRequest):
    return predict(order.model_dump())

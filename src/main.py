import time

from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest

from config.schema import OrderRequest, PredictionResponse
from src.predict import predict


app = FastAPI(title="Olist Late Delivery Prediction API")


# =========================
# Monitoring Metrics
# =========================

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "API request latency in seconds",
    ["method", "endpoint"],
)

PREDICTION_COUNT = Counter(
    "predictions_total",
    "Total number of predictions",
    ["prediction"],
)


# =========================
# Request Monitoring
# =========================


@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code,
        ).inc()

        return response

    except Exception:
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=500,
        ).inc()

        raise

    finally:
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path,
        ).observe(time.time() - start_time)


# =========================
# API Endpoints
# =========================


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
        "model_version": "1.0",
    }


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain",
    )


@app.post("/predict", response_model=PredictionResponse)
def predict_order(order: OrderRequest):
    result = predict(order.model_dump())

    PREDICTION_COUNT.labels(prediction=result["prediction"]).inc()

    return result


@app.post("/predict/batch")
def predict_batch(orders: list[OrderRequest]):
    results = []

    for order in orders:
        result = predict(order.model_dump())

        PREDICTION_COUNT.labels(prediction=result["prediction"]).inc()

        results.append(result)

    return results

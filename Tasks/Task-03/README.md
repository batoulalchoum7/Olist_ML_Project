# Task 03 — Production Inference & MLOps

## Objective

Convert the trained Olist late-delivery model into a production-ready inference service.

The service performs inference only and does not retrain the model.

## Project Structure

The production implementation includes:

* `src/` — prediction logic and FastAPI application
* `config/` — application configuration and request/response schemas
* `models/` — trained model and preprocessing artifacts
* `tests/` — automated tests
* `Dockerfile` — container image definition
* `docker-compose.yml` — local container orchestration
* `.github/workflows/` — CI/CD workflow
* DVC configuration — data/version tracking
* Great Expectations — data validation
* MLflow — experiment/model tracking
* Prometheus metrics — API and prediction monitoring

## Inference API

The FastAPI service provides:

* Health check endpoint
* Model information endpoint
* Single-order prediction
* Batch prediction
* Prometheus metrics

A prediction returns:

* Prediction: `late` or `on time`
* Probability
* Model version

Example:

```json
{
  "prediction": "on time",
  "probability": 0.3257134593683888,
  "model_version": "1.0"
}
```

## Data Validation

Great Expectations is used to validate input data before inference.

Automated tests verify both valid and invalid input cases.

## MLflow

MLflow is used for model/experiment tracking and logging.

The trained model was successfully logged.

## Docker

The inference API was containerized using Docker.

Docker Compose is provided for local execution.

## Testing

Automated tests cover:

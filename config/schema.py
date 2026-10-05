from pydantic import BaseModel, Field


class OrderRequest(BaseModel):
    purchase_hour: int = Field(ge=0, le=23)
    purchase_day_of_week: int = Field(ge=0, le=6)
    purchase_month: int = Field(ge=1, le=12)
    purchase_year: int = Field(ge=2017, le=2030)
    approval_delay_hours: float = Field(ge=0)
    estimated_delivery_days: float = Field(ge=0)


class PredictionResponse(BaseModel):
    prediction: str
    probability: float
    model_version: str

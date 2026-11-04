import logging
import joblib
import numpy as np

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Iris ML Prediction API",
    description="Machine Learning model deployed using Docker and FastAPI",
    version="1.0"
)

# Load trained model
try:
    model = joblib.load("iris_model.pkl")
    logger.info("Model loaded successfully")
except Exception:
    model = None
    logger.exception("Model loading failed")


class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)


@app.get("/")
def home():
    return {"message": "Iris ML API is running"}


@app.get("/health")
def health():
    if model is None:
        raise HTTPException(status_code=503, detail="Model unavailable")

    return {"status": "healthy", "model_loaded": True}


@app.post("/predict")
def predict(data: IrisInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model unavailable")

    features = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}
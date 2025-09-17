import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="BY-WMS PickTime Model")

class Features(BaseModel):
    distance_est: float
    sku_volume: float
    wave_size: int
    weekday: int
    hour: int

model = joblib.load("artifacts/model.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(feat: Features):
    X = np.array([[
        feat.distance_est, feat.sku_volume, feat.wave_size, feat.weekday, feat.hour
    ]])
    y_hat = float(model.predict(X)[0])
    return {"eta_minutes": round(y_hat,2)}

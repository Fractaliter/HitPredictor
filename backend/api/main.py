# backend/api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware

class SongFeatures(BaseModel):
    danceability: float
    valence: float
    energy: float

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # albo ["http://localhost:5173"] dla bezpieczeństwa
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Ścieżka względna do modelu
model_path = os.path.join(os.path.dirname(__file__), '../model/hit_predictor.pkl')
model = joblib.load(model_path)

@app.get("/")
def root():
    return {"message": "Hit Predictor API is running 🎧"}

@app.post("/predict")
def predict(features: SongFeatures):
    X = np.array([[features.danceability, features.valence, features.energy]])
    prediction = model.predict(X)[0]
    return {"predicted_popularity": round(float(prediction), 2)}

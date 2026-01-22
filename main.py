from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="API de Análisis de Sentimientos", version="1.0.0")

try:
    model = joblib.load("sentiment_model.pkl")
    print("Modelo cargado correctamente.")
except FileNotFoundError:
    print("Modelo no encontrado.")
    model = None

class ReviewText(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(review: ReviewText):
    if model is None:
        return {"error": "Modelo no disponible"}
    
    prediction = model.predict([review.text])
    return {
        "text": review.text,
        "sentiment": prediction[0]
    }

@app.get("/")
def root():
    return {"message": "API de Análisis de Sentimientos activa"}

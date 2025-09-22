from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# 1. Inicializamos la aplicación FastAPI
app = FastAPI(title="API de Análisis de Sentimientos", version="1.0.0")

# 2. Cargamos el modelo entrenado al iniciar la app
# Esto asegura que el modelo esté listo en memoria para hacer predicciones rápidas.
try:
    model = joblib.load('sentiment_model.pkl')
    print("Modelo cargado correctamente.")
except FileNotFoundError:
    print("Error: El archivo 'sentiment_model.pkl' no fue encontrado.")
    model = None

# 3. Definimos el formato de la entrada de datos
# Pydantic se encarga de validar que la petición entrante tenga esta estructura.
class ReviewText(BaseModel):
    text: str # Esperamos un JSON con una clave "text"

# 4. Creamos el endpoint de predicción
@app.post("/predict")
def predict_sentiment(review: ReviewText):
    """
    Endpoint para predecir el sentimiento de un texto dado.
    - Recibe: un JSON con la clave "text".
    - Devuelve: un JSON con la clave "sentiment" y el resultado.
    """
    if model is None:
        return {"error": "El modelo no está disponible."}
        
    # El modelo espera una lista de textos, por eso usamos [review.text]
    prediction = model.predict([review.text])
    
    # Devolvemos la primera (y única) predicción en un formato JSON amigable.
    return {"text": review.text, "sentiment": prediction[0]}

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Análisis de Sentimientos"}
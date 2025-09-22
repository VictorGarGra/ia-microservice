import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 
import joblib

print("Iniciando el entrenamiento con Regresión Logística desde archivo CSV...")

try:
    # --- CAMBIO 1: Eliminamos sep='@'. Pandas detectará la coma automáticamente. ---
    df = pd.read_csv('reviews_espanol.csv') 
    print(f"Dataset cargado desde CSV con {len(df)} filas.")
except FileNotFoundError:
    print("Error: 'reviews_espanol.csv' no encontrado.")
    exit()

# Limpiamos filas que puedan estar vacías
df.dropna(inplace=True)
print(f"Entrenando el modelo con {len(df)} reseñas limpias.")

# --- CAMBIO 2: Usamos los nombres de columna EXACTOS de tu imagen ---
# Nota la 'R' mayúscula en 'Review' y que 'sentimiento' está en español.
X_train = df['Review']
y_train = df['sentimiento']

# (Opcional pero recomendado) Convertimos los sentimientos a mayúsculas para estandarizar
y_train = y_train.str.upper()

# El resto del código no cambia
model = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))

model.fit(X_train, y_train)
print("Modelo de Regresión Logística entrenado exitosamente.")

joblib.dump(model, 'sentiment_model.pkl')
print("¡Nuevo modelo más potente guardado!")
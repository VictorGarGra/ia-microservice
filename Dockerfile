# Usa una imagen base ligera de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos e instala las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto (main.py, modelo, etc.)
COPY . .

# Cloud Run usa la variable PORT (por defecto 8080)
ENV PORT 8080

# Ejecutar la aplicación (suponiendo que usas Flask o FastAPI)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
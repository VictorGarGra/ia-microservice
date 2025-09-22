# Usa una imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos e instala las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto (main.py, modelo, etc.)
COPY . .

# Comando para iniciar el servidor de FastAPI
# --host 0.0.0.0 es necesario para que sea accesible en Render
# --port 10000 es el puerto que Render usa por defecto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
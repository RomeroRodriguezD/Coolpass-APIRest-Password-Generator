# Utilizamos una imagen base de python:3.8
FROM python:3.10

# Establecemos el directorio de trabajo
WORKDIR /app

ENV FLASK_APP=pass_api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copiamos el archivo de requirements
COPY requirements.txt .
COPY src/ .
COPY templates/ .

# Instalamos las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos el resto de archivos necesarios
COPY . .

# Exponemos el puerto 5000
EXPOSE 5000

# Ejecutamos la aplicación
CMD ["flask", "run"]


# Python base image
FROM python:3.10

# Working directory + environment variables
WORKDIR /app
ENV FLASK_APP=pass_api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy required stuff
COPY requirements.txt .
COPY src/ .
COPY templates/ .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos anything else on workdir
COPY . .

# Expose port
EXPOSE 5000

# Run flask
CMD ["flask", "run"]


# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

# Only copy necessary files
COPY app.py ./
COPY scaler.pkl ./
COPY pca_model.pkl ./
COPY logistic_model_tuned.pkl ./

# Set environment variables for model paths (these should match your .env or defaults)
ENV SCALER_PATH="/app/scaler.pkl"
ENV PCA_PATH="/app/pca_model.pkl"
ENV LOGISTIC_PATH="/app/logistic_model_tuned.pkl"
ENV FLASK_PORT=1111

# Expose the port Flask runs on
EXPOSE 1111

# Run the Flask app
CMD ["python", "/app/app.py"]

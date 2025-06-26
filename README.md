# MLOps in Travel: Price Prediction Suite

This repository is an end-to-end MLOps project focused on building, training, deploying, and orchestrating machine learning models for the travel industry. It includes solutions for flight price prediction, hotel price prediction, and gender classification, demonstrating best practices in reproducibility, automation, and scalable deployment using Docker, Airflow, and MLflow.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Features](#features)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Model Training & Tracking](#model-training--tracking)
- [Orchestration (Airflow)](#orchestration-airflow)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview
This project demonstrates a full MLOps pipeline for:
- **Flight Price Prediction**: Predicts flight prices using machine learning models.
- **Hotel Price Prediction**: Predicts hotel prices based on various features.
- **Gender Classification**: Classifies gender from data using ML models.

Each module is containerized and can be orchestrated using Airflow, with experiment tracking via MLflow.

## Directory Structure

A well-organized, modular repository to support robust MLOps workflows for travel industry solutions:

```text
mlops_in_travel/
│
├── Datasets/
│   ├── flights.csv                # Raw flight data for model training and evaluation
│   ├── hotels.csv                 # Raw hotel data for model training and evaluation
│   └── users.csv                  # User data for analytics and personalization
│
├── flight_price/
│   ├── .env                       # Environment variables for configuration
│   ├── .gitignore                 # Git ignore rules for sensitive and build files
│   ├── Dockerfile                 # Containerization for reproducible deployment
│   ├── Jenkinsfile                # Jenkins pipeline for CI/CD automation
│   ├── requirements.txt           # Python dependencies specific to this module
│   ├── eda.ipynb                  # Exploratory Data Analysis notebook
│   ├── flight_price_prediction.ipynb # Model development and experimentation notebook
│   ├── app.py                     # Production-ready API/web app for flight price prediction
│   ├── deployment.yaml            # Kubernetes deployment manifest
│   ├── *.pkl                      # Serialized trained model artifacts
│   ├── MLflow/
│   │   └── flight_price_mlflow.py # MLflow experiment tracking scripts
│   ├── airflow_home/
│   │   ├── docker-compose.yaml    # Docker Compose for Airflow orchestration
│   │   ├── dags/
│   │   │   └── flight_price_dags.py # Airflow DAGs for automated workflow management
│   │   └── config/
│   │       └── airflow.cfg        # Airflow configuration
│   └── templates/
│       └── index.html             # Web UI template for the flight price app
│
├── gender_classification/
│   ├── .env                       # Environment variables for configuration
│   ├── Dockerfile                 # Containerization for deployment
│   ├── requirements.txt           # Python dependencies
│   ├── app.py                     # API/web app for gender classification
│   ├── gender_classification.ipynb # Model development and experimentation notebook
│   └── *.pkl / *.joblib           # Serialized trained model artifacts
│
├── hotel_price/
│   ├── .env                       # Environment variables for configuration
│   ├── Dockerfile                 # Containerization for deployment
│   ├── requirements.txt           # Python dependencies
│   ├── app.py                     # API/web app for hotel price prediction
│   ├── hotel-price-app-deployment.yaml # Kubernetes deployment manifest
│   ├── hotel_price_pridiction.ipynb # Model development and experimentation notebook
│   └── *.joblib / *.pkl           # Serialized trained model artifacts
│
└── README.md                      # Project documentation and usage guidelines
```

This structure ensures clear separation of concerns, scalability, and ease of onboarding for new contributors. Each module is self-contained, with dedicated configuration, dependencies, and deployment scripts, supporting best practices in modern MLOps.

## Features
- Modular ML projects for different travel industry tasks
- Automated data pipelines and orchestration with Airflow
- Experiment tracking with MLflow
- Containerized with Docker for reproducibility
- Deployment-ready (Kubernetes YAML, Docker Compose)
- Example notebooks for EDA and model training

## Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hritikrai55/mlops_in_travel.git
   cd mlops_in_travel
   ```
2. **Install dependencies:**
   - Each module (`flight_price`, `gender_classification`, `hotel_price`) has its own `requirements.txt`.
   - Use virtual environments for isolation.
   ```bash
   cd flight_price
   pip install -r requirements.txt
   ```
3. **Environment Variables:**
   - Copy `.env.example` to `.env` in each module and fill in required values.

4. **Docker (Recommended):**
   - Build and run containers for each module:
   ```bash
   docker build -t flight-price-app ./flight_price
   docker run -p 8000:8000 flight-price-app
   ```

## Usage
- **Flight Price Prediction:**
  - Run `app.py` in `flight_price` for API/web interface.
  - Access the web UI at the exposed port (default: 8000).
- **Hotel Price Prediction:**
  - Similarly, run `hotel_price/app.py`.
- **Gender Classification:**
  - Run `gender_classification/app.py`.

## Model Training & Tracking
- Notebooks (`*.ipynb`) provided for EDA and model training.
- MLflow integration for experiment tracking (`flight_price/MLflow/flight_price_mlflow.py`).
- Trained models are saved as `.pkl` or `.joblib` files in respective module folders.

## Orchestration (Airflow)
- Airflow setup is provided in `flight_price/airflow_home/`.
- Start Airflow with Docker Compose:
  ```bash
  cd flight_price/airflow_home
  docker-compose up
  ```
- DAGs are located in `dags/` and can be customized for your pipeline.

## Deployment
- Dockerfiles provided for all modules.
- Kubernetes deployment YAML for hotel price app (`hotel_price/hotel-price-app-deployment.yaml`).
- CI/CD example with Jenkins (`flight_price/Jenkinsfile`).

## Contributing
Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or new features.

## License
[MIT License](LICENSE)

---

For more details, refer to the source code and comments in each module.

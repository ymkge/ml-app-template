# FastAPI + scikit-learn ML Application Template

This is a template project for a machine learning application using FastAPI, scikit-learn, and Docker, with a CI/CD pipeline using GitHub Actions.

## Project Structure

```
ml-app-template/
├── app/
│   ├── main.py         # FastAPI entrypoint
│   ├── model.py        # Load model & predict
│   ├── utils.py        # Helper functions
│   ├── data.csv        # Training data
│   └── model.pkl       # Trained model file
├── train.py            # Model retraining script
├── requirements.txt    # Dependencies
├── Dockerfile          # Docker container definition
├── docker-compose.yml  # For local development
├── .github/
│   └── workflows/
│       └── ci-cd.yml   # GitHub Actions CI/CD pipeline
└── README.md
```

## Getting Started

### Local Development

1.  **Build and run the container:**
    ```bash
    docker-compose up --build
    ```
    The application will be available at `http://localhost:8000`.

2.  **Test the endpoints:**
    -   Health Check: `curl http://localhost:8000/health`
    -   Prediction:
        ```bash
        curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{"feature1": 0.5, "feature2": 0.5}'
        ```

### Model Retraining

1.  **Update `app/data.csv`** with new data if necessary.

2.  **Run the training script:**
    ```bash
    python3 train.py
    ```
    This will overwrite `app/model.pkl` with the newly trained model.

3.  **Rebuild your Docker image** to include the new model:
    ```bash
    docker-compose up --build
    ```

## CI/CD Pipeline

The CI/CD pipeline is configured in `.github/workflows/ci-cd.yml` and automates testing, building, and deploying the application.

### Flow

1.  **Trigger**: A push to the `main` branch.
2.  **Lint & Test**: (Placeholder) Runs linters and tests.
3.  **Build & Push**: Builds a Docker image and pushes it to GitHub Container Registry.
4.  **Deploy**: Triggers a new deployment on Render.com using their deploy hook.

### Setup

To make the CI/CD pipeline work, you need to configure the following secrets in your GitHub repository (`Settings > Secrets and variables > Actions`):

-   `RENDER_API_KEY`: Your API key from Render.
-   `RENDER_SERVICE_ID`: The ID of the service on Render you want to deploy to.

The Docker image will be pushed to GitHub Container Registry, which should be automatically enabled for your repository. You'll need to connect your Render service to this container registry.


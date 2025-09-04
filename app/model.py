import joblib
import pandas as pd
from pathlib import Path

# Build the path to the model file
model_path = Path(__file__).parent / "model.pkl"

# Load the model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    # This is a fallback for environments where the model might not be present initially.
    # In a real-world scenario, you'd handle this more gracefully.
    model = None

def predict(data: dict) -> list:
    """
    Runs a prediction using the loaded model.
    """
    if model is None:
        raise RuntimeError("Model is not loaded. Please train the model first.")
        
    # Convert input data into a DataFrame
    df = pd.DataFrame(data, index=[0])
    
    # Make prediction
    prediction = model.predict(df)
    
    return prediction.tolist()

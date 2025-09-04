from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import model

app = FastAPI()

# Define the input data schema
class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(data: InputData):
    """Prediction endpoint."""
    try:
        prediction = model.predict(data.dict())
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib

model = joblib.load("stress_prediction_model.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StressInput(BaseModel):
    academic_pressure: float

@app.post("/predict")
def predict_stress(data: StressInput):
    import pandas as pd
    # Create DataFrame with proper feature names to match training data
    input_df = pd.DataFrame({"academic_pressure_score": [data.academic_pressure]})
    prediction = model.predict(input_df)[0]

    return {
        "stress_score": float(prediction)
    }

# Run server:
# uvicorn main:app --reload
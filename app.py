from pathlib import Path
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

MODEL = joblib.load(Path(__file__).parent / "model" / "champion_model.joblib")
app = FastAPI(title="Task 06 - Real-Time ML Inference API", version="1.0.0")

class PassengerInput(BaseModel):
    Pclass: int = Field(..., ge=1, le=3)
    Sex: str
    Age: float = Field(..., ge=0, le=120)
    SibSp: int = Field(..., ge=0)
    Parch: int = Field(..., ge=0)
    Fare: float = Field(..., ge=0)
    Embarked: str

class PredictionResponse(BaseModel):
    prediction: int
    label: str
    probability: float
    confidence: float

def make_features(p):
    if p.Sex.lower() not in {"male", "female"}: raise HTTPException(422, "Sex must be male or female")
    if p.Embarked.upper() not in {"C", "Q", "S"}: raise HTTPException(422, "Embarked must be C, Q or S")
    return np.array([[p.Pclass, int(p.Sex.lower()=="female"), p.Age, p.SibSp, p.Parch, p.Fare, {"C":0,"Q":1,"S":2}[p.Embarked.upper()]])

@app.get("/")
def root(): return {"message":"Task 06 ML API is running", "docs":"/docs", "predict":"/predict"}

@app.get("/health")
def health(): return {"status":"healthy", "model_loaded":True}

@app.post("/predict", response_model=PredictionResponse)
def predict(p: PassengerInput):
    prob=float(MODEL.predict_proba(make_features(p))[0][1])
    pred=int(prob>=0.5)
    return {"prediction":pred,"label":"Survived" if pred else "Did not survive","probability":round(prob,6),"confidence":round(max(prob,1-prob),6)}

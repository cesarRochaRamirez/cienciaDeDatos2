from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Cargar el modelo
model = joblib.load("random_forest_model.pkl")

# Crear la API
app = FastAPI()

# Definir la estructura de entrada
class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}

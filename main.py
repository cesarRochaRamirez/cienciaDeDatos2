from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Cargar el modelo guardado en el archivo 'random_forest_model.pkl'
with open('/home/cloudshell-user/random_forest_model.pkl', 'rb') as model_file:
    modelo = pickle.load(model_file)

# Crear una instancia de FastAPI
app = FastAPI()

# Definir el modelo de datos para los datos de entrada
class InputData(BaseModel):
    LoginAttempts: float  # La única característica de entrada según tu código

# Endpoint para realizar predicciones
@app.post("/predict")
async def predict(data: InputData):
    # Convertir los datos de entrada a un formato adecuado para la predicción (matriz de 2D)
    input_data = np.array([[data.LoginAttempts]])
    
    # Realizar la predicción con el modelo
    prediction = modelo.predict(input_data)
    
    # Devolver la predicción (0 para normal, 1 para sospechoso)
    return {"prediction": int(prediction[0])}

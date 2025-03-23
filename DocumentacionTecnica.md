# Documentación Técnica

## Propósito del Proyecto

El propósito de este proyecto es entrenar un modelo de **Machine Learning** utilizando el algoritmo **Random Forest** para predecir una variable basada en ciertos datos de entrada, en este caso, la cantidad de intentos de inicio de sesión de un usuario. La implementación de este modelo está realizada en **Python** y se ha desplegado como una **API RESTful** utilizando el framework **FastAPI**. El modelo está cargado en un archivo `random_forest_model.pkl` y se puede utilizar para realizar predicciones a través de un servicio web.

El modelo de Machine Learning fue entrenado previamente utilizando un conjunto de datos que contiene características relacionadas con intentos de inicio de sesión de usuarios, y la API expone un endpoint que permite a los usuarios enviar datos de entrada y recibir las predicciones en tiempo real.

## Estructura del Código


project_folder

│ 

├── app.py # Archivo principal de la aplicación FastAPI 

├── random_forest_model.pkl # Archivo con el modelo entrenado 

├── requirements.txt # Archivo con las dependencias del proyecto 

├── README.md # Documentación general del proyecto 

└── DocumentacionTecnica.md # Documentación técnica detallada

### Descripción de los Archivos:

- **`app.py`**: Este es el archivo que contiene la lógica principal de la API. En él se cargan las dependencias necesarias, se carga el modelo entrenado con `joblib`, y se define el endpoint para recibir las solicitudes de predicción.
  
- **`random_forest_model.pkl`**: Este es el archivo que contiene el modelo de Machine Learning que ha sido entrenado previamente y guardado usando `joblib`.

- **`requirements.txt`**: Contiene las dependencias necesarias para ejecutar el proyecto. Se incluyen bibliotecas como FastAPI, Uvicorn, Joblib y Numpy.

- **`README.md`**: Documento que proporciona una descripción general del proyecto, los requisitos de instalación, cómo ejecutar la aplicación y ejemplos de uso de la API.

- **`DOCUMENTACION.md`**: Documento de la documentación técnica que se explica a continuación.

## Descripción de `app.py`

El archivo `app.py` contiene el código para crear una API usando el framework **FastAPI**. A continuación se describe la funcionalidad de cada parte del código:

1. **Carga del Modelo**:
   El modelo entrenado es cargado desde un archivo `.pkl` usando la librería **joblib**.

   ```python
   model = joblib.load("random_forest_model.pkl")
2.	Creación de la API: Usamos FastAPI para crear la API. En el siguiente bloque de código, se define una clase InputData que espera un parámetro de entrada llamado features, que es una lista de números. Esta clase se usa para validar los datos de entrada.
3.	from pydantic import BaseModel
5.	class InputData(BaseModel):
6.	    features: list
7.	Endpoint para Predicciones: Se define un endpoint POST en /predict que acepta solicitudes con datos de entrada, y pasa estos datos al modelo para realizar la predicción. La predicción es luego devuelta como respuesta en formato JSON.
8.	@app.post("/predict")
9.	def predict(data: InputData):
10.	    features = np.array(data.features).reshape(1, -1)
11.	    prediction = model.predict(features)
12.	    return {"prediction": prediction.tolist()}
13.	Inicio del Servidor: El servidor se puede ejecutar usando Uvicorn, que es un servidor ASGI compatible con FastAPI.
14.	uvicorn app:app --reload
Pasos para Replicar el Proyecto
Para replicar este proyecto en tu entorno, sigue estos pasos:
1. Clonar el Repositorio
Primero, clona el repositorio de GitHub en tu máquina local o servidor:
git clone https://github.com/cesarRochaRamirez/cienciaDeDatos2.git
cd cienciaDeDatos2
2. Instalar las Dependencias
Instala las dependencias necesarias desde el archivo requirements.txt:
pip install -r requirements.txt
Este comando instalará FastAPI, Uvicorn, Joblib y Numpy, que son las bibliotecas necesarias para ejecutar el proyecto.
3. Cargar el Modelo
Asegúrate de que el archivo del modelo random_forest_model.pkl esté en el directorio del proyecto. Este archivo debe ser cargado correctamente cuando ejecutes el código.
4. Ejecutar la Aplicación FastAPI
Inicia el servidor FastAPI usando Uvicorn. Esto abrirá el servicio web en http://127.0.0.1:8000.
uvicorn app:app --reload
5. Realizar Predicciones
Una vez que el servidor esté en funcionamiento, puedes enviar solicitudes POST al endpoint /predict para obtener predicciones. A continuación, se muestra un ejemplo de cómo realizar una solicitud usando curl:
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{"features": [5]}'
La respuesta será un JSON con la predicción del modelo:
{"prediction": [1]}
6. Despliegue en la Nube
Para desplegar el proyecto en la nube, sigue los pasos necesarios para crear una instancia de Amazon EC2 o cualquier otra infraestructura de nube de tu elección, y configura el servidor para ejecutar la API en una dirección IP pública. Asegúrate de configurar el puerto adecuado y la seguridad de la instancia para permitir conexiones externas.
Enlace al Repositorio de GitHub
Puedes encontrar el código fuente y más detalles en el siguiente enlace:
Repositorio de GitHub - cienciaDeDatos2

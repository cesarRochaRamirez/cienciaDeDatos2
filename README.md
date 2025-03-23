# API de Detección de Intentos de Inicio de Sesión Sospechosos(prototipo)

Este proyecto implementa una API utilizando **FastAPI** para cargar y utilizar un modelo de Machine Learning (Random Forest) entrenado previamente. La API permite realizar predicciones basadas en intentos de inicio de sesión.

## Requisitos Previos

Antes de ejecutar la API, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install fastapi uvicorn numpy pydantic scikit-learn joblib
```

También necesitas tener un modelo de Machine Learning previamente entrenado y guardado en un archivo `random_forest_model.pkl`.

## Estructura del Proyecto

```
/
|-- app.py  # Archivo principal con la API
|-- random_forest_model.pkl  # Modelo entrenado guardado
```

## Ejecución de la API

Para iniciar la API, ejecuta el siguiente comando en la terminal:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

La API **solo estará disponible desde la terminal de la instancia EC2**.

## Uso de la API

### Realizar *una Predicción*

Para hacer una predicción, envía una solicitud `POST` al endpoint `/predict` con un JSON en el siguiente formato:

```json
{
  "features": [3.5]
}
```

Ejemplo de petición en `curl`:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{"features": [3.5]}'
```

### Respuesta esperada

```json
{
  "prediction": [1]
}
```

Donde `0` indica un inicio de sesión normal y `1` indica un inicio de sesión sospechoso.

## Documentación Automática

FastAPI proporciona una interfaz de documentación automática, pero **solo estará accesible desde la instancia EC2**, no de forma pública:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Despliegue en AWS EC2

Para desplegar la API en una instancia de **AWS EC2**, sigue estos pasos:

1. **Conectarse a la instancia** mediante SSH:
   ```bash
   ssh -i "tu_clave.pem" ubuntu@3.21.44.240
   ```
2. **Actualizar e instalar dependencias**:
   ```bash
   sudo apt update && sudo apt install python3-pip -y
   pip3 install fastapi uvicorn numpy pydantic scikit-learn joblib
   ```
3. **Subir los archivos **`app.py`** y **`random_forest_model.pkl`** a la instancia.
4. **Ejecutar la API**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

**Nota:** La API solo será accesible desde la terminal de la instancia EC2.

## Contribución

Si deseas mejorar esta API, puedes hacer un *fork* del repositorio, trabajar en una nueva rama y enviar un *pull request*.

## Licencia

Este proyecto está bajo la licencia MIT.


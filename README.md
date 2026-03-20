#  Titanic ML Pipeline con Valohai y Evidently AI

Implementa y automatiza el ciclo de vida de un modelo de Machine Learning utilizando **Valohai** como plataforma de MLOps. Predice la supervivencia de los pasajeros del Titanic basándote en sus características y detecta posibles desviaciones en los datos (*Data Drift*) mediante el uso de **Evidently AI**.

##  Estructura del Proyecto

Organiza el repositorio con la siguiente estructura de directorios para garantizar el despliegue correcto del pipeline:

```text
valohai-titanic-ml/
├── data/
│   └── train.csv             # Dataset original del Titanic (Kaggle) 
├── src/                      # Scripts de ejecución del pipeline 
│   ├── preprocess.py         # Limpieza, codificación y manejo de nulos 
│   ├── train.py              # Entrenamiento del modelo RandomForest 
│   └── evaluate.py           # Evaluación de métricas (Accuracy,...) 
├── Dockerfile                # Receta para construir la imagen base del entorno 
├── requirements.txt          # Dependencias (pandas, scikit-learn, joblib, evidently) 
├── valohai.yaml              # Orquestador de pasos y configuración del pipeline 
└── evi.py                    # Script local para generar el reporte HTML de Evidently
```

##  Tecnologías Utilizadas

* **Lenguaje:** Python 3.10
* **Librerías ML:** Pandas, Scikit-Learn, Joblib
* **MLOps & Orquestación:** Valohai 
* **Contenedores:** Docker 
* **Monitoreo:** Evidently AI (v0.4.39)

##  Guía de Ejecución

### 1. Construcción de Imagen Docker
Construye y sube la imagen a Docker Hub para aislar el entorno y evitar la instalación de dependencias en cada paso del pipeline:

```bash
# Construir la imagen localmente
docker build -t <tu-usuario-docker>/titanic-ml:latest .

# Subir la imagen a Docker Hub
docker push <tu-usuario-docker>/titanic-ml:latest
```
*(Asegúrate de actualizar la propiedad `image` en el archivo `valohai.yaml` con el nombre exacto de la imagen generada).*

### 2. Ejecución del Pipeline en Valohai
Despliega y ejecuta las fases de preprocesamiento, entrenamiento y evaluación siguiendo estos pasos:

1. Ingresar a [Valohai](https://valohai.com/) y crear un nuevo proyecto.
2. Navegar a **Settings > Repository** y enlazar la URL de este repositorio de GitHub.
3. Ingresar a la pestaña **Pipelines** y haz clic en **Create Pipeline**.
4. Seleccionar el Blueprint `training-pipeline` y ejecutar el proceso.

> **Nota:** Tener en cuenta la asignación de máquinas virtuales para ejecutar el modelo en Valohai requiere un plan de pago activo.

### 3. Monitoreo de Data Drift (Local)
Genera el reporte de monitoreo local con Evidently para evaluar el comportamiento del modelo frente a nuevos datos de producción:

1. Instalar la versión de Evidently requerida: `pip install evidently==0.4.39`.
2. Ejecutar el script de análisis: `python evi.py`.
3. Abrir el archivo generado `reporte_drift_titanic.html` en un navegador web para explorar las métricas y los gráficos interactivos.

---
*Proyecto desarrollado como práctica de MLOps y empaquetamiento de modelos predictivos.*

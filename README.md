# 🚢 Titanic ML Pipeline con Valohai y Evidently AI

Este proyecto automatiza el ciclo de vida de un modelo de Machine Learning utilizando **Valohai** como plataforma de MLOps. El objetivo del modelo es predecir si un pasajero sobrevive o no al hundimiento del Titanic basándose en sus características. 

Además, se incluye una fase de monitoreo utilizando **Evidently AI** para detectar posibles desviaciones en los datos (*Data Drift*).

## 📂 Estructura del Proyecto

El repositorio sigue la estructura estándar requerida para el despliegue del pipeline:

\`\`\`text
valohai-titanic-ml/
├── data/
│   └── train.csv             # Dataset original del Titanic (Kaggle) 
├── src/                      # Scripts de ejecución del pipeline 
│   ├── preprocess.py         # Limpieza, codificación y manejo de nulos 
│   ├── train.py              # Entrenamiento del modelo RandomForest 
│   └── evaluate.py           # Evaluación de métricas (Accuracy) 
├── Dockerfile                # Receta para construir la imagen base del entorno 
├── requirements.txt          # Dependencias (pandas, scikit-learn, joblib, evidently) 
├── valohai.yaml              # Orquestador de pasos y configuración del pipeline 
└── drift_report.py           # Script local para generar el reporte HTML de Evidently
\`\`\`

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10
* **Librerías ML:** Pandas, Scikit-Learn, Joblib
* **MLOps & Orquestación:** Valohai 
* **Contenedores:** Docker 
* **Monitoreo:** Evidently AI (v0.4.39) 

## 🚀 Guía de Ejecución

### 1. Construcción de la Imagen Docker
Para que Valohai pueda ejecutar el código sin instalar dependencias desde cero en cada paso, primero se debe construir y subir la imagen a Docker Hub:

\`\`\`bash
# Construir la imagen localmente
docker build -t <tu-usuario-docker>/titanic-ml:latest.

# Subir la imagen a Docker Hub
docker push <tu-usuario-docker>/titanic-ml:latest.
\`\`\`
*(Asegúrate de actualizar la propiedad `image` en el archivo `valohai.yaml` con el nombre de tu imagen).*

### 2. Ejecución del Pipeline en Valohai
El pipeline consta de tres pasos: **preprocesamiento, entrenamiento y evaluación**.

1. Ingresa a [Valohai](https://valohai.com/) y crea un nuevo proyecto.
2. Ve a **Settings > Repository** y enlaza la URL de este repositorio de GitHub.
3. Ve a la pestaña **Pipelines**, haz clic en **Create Pipeline**.
4. Selecciona el Blueprint `training-pipeline` y ejecútalo.

> **⚠️ Nota de infraestructura:** La ejecución en la nube de Valohai con máquinas virtuales asignadas puede requerir que la cuenta esté en un plan de pago para habilitar el entorno de ejecución.

### 3. Monitoreo de Data Drift (Local)
Para evaluar cómo se comporta el modelo y detectar si los datos actuales de producción difieren de los de entrenamiento, ejecutamos Evidently de forma local:

1. Asegúrate de tener instalado Evidently: `pip install evidently==0.4.39`.
2. Ejecuta el script de análisis: `python drift_report.py`.
3. Abre el archivo generado `titanic_drift_report.html` en cualquier navegador web para explorar las métricas y gráficos interactivos.

---
*Proyecto desarrollado como práctica de MLOps y empaquetamiento de modelos predictivos.*

# 🚢 Titanic ML Pipeline con Valohai y Evidently AI

[cite_start]Este proyecto automatiza el ciclo de vida de un modelo de Machine Learning utilizando **Valohai** como plataforma de MLOps[cite: 2]. [cite_start]El objetivo del modelo es predecir si un pasajero sobrevive o no al hundimiento del Titanic basándose en sus características[cite: 7]. 

[cite_start]Además, se incluye una fase de monitoreo utilizando **Evidently AI** para detectar posibles desviaciones en los datos (*Data Drift*)[cite: 169, 174].

## 📂 Estructura del Proyecto

[cite_start]El repositorio sigue la estructura estándar requerida para el despliegue del pipeline[cite: 9]:

\`\`\`text
valohai-titanic-ml/
├── data/
[cite_start]│   └── train.csv             # Dataset original del Titanic (Kaggle) [cite: 4, 15, 16]
[cite_start]├── src/                      # Scripts de ejecución del pipeline [cite: 17]
[cite_start]│   ├── preprocess.py         # Limpieza, codificación y manejo de nulos [cite: 18]
[cite_start]│   ├── train.py              # Entrenamiento del modelo RandomForest [cite: 18]
[cite_start]│   └── evaluate.py           # Evaluación de métricas (Accuracy) [cite: 18]
[cite_start]├── Dockerfile                # Receta para construir la imagen base del entorno [cite: 12]
[cite_start]├── requirements.txt          # Dependencias (pandas, scikit-learn, joblib, evidently) [cite: 14]
[cite_start]├── valohai.yaml              # Orquestador de pasos y configuración del pipeline [cite: 13]
└── drift_report.py           # Script local para generar el reporte HTML de Evidently
\`\`\`

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10
* **Librerías ML:** Pandas, Scikit-Learn, Joblib
* [cite_start]**MLOps & Orquestación:** Valohai [cite: 2]
* [cite_start]**Contenedores:** Docker [cite: 3]
* [cite_start]**Monitoreo:** Evidently AI (v0.4.39) [cite: 181]

## 🚀 Guía de Ejecución

### 1. Construcción de la Imagen Docker
Para que Valohai pueda ejecutar el código sin instalar dependencias desde cero en cada paso, primero se debe construir y subir la imagen a Docker Hub:

\`\`\`bash
# Construir la imagen localmente
docker build -t <tu-usuario-docker>/titanic-ml:latest .

# Subir la imagen a Docker Hub
docker push <tu-usuario-docker>/titanic-ml:latest
\`\`\`
*(Asegúrate de actualizar la propiedad `image` en el archivo `valohai.yaml` con el nombre de tu imagen).*

### 2. Ejecución del Pipeline en Valohai
[cite_start]El pipeline consta de tres pasos: **preprocesamiento, entrenamiento y evaluación**[cite: 8].

1. [cite_start]Ingresa a [Valohai](https://valohai.com/) y crea un nuevo proyecto[cite: 82].
2. [cite_start]Ve a **Settings > Repository** y enlaza la URL de este repositorio de GitHub[cite: 115, 120].
3. [cite_start]Ve a la pestaña **Pipelines**, haz clic en **Create Pipeline**[cite: 134, 141].
4. [cite_start]Selecciona el Blueprint `training-pipeline` y ejecútalo[cite: 148].

> [cite_start]**⚠️ Nota de infraestructura:** La ejecución en la nube de Valohai con máquinas virtuales asignadas puede requerir que la cuenta esté en un plan de pago para habilitar el entorno de ejecución[cite: 167].

### 3. Monitoreo de Data Drift (Local)
[cite_start]Para evaluar cómo se comporta el modelo y detectar si los datos actuales de producción difieren de los de entrenamiento[cite: 170, 174], ejecutamos Evidently de forma local:

1. [cite_start]Asegúrate de tener instalado Evidently: `pip install evidently==0.4.39`[cite: 181].
2. Ejecuta el script de análisis: `python drift_report.py`.
3. [cite_start]Abre el archivo generado `titanic_drift_report.html` en cualquier navegador web para explorar las métricas y gráficos interactivos[cite: 177, 178].

---
*Proyecto desarrollado como práctica de MLOps y empaquetamiento de modelos predictivos.*

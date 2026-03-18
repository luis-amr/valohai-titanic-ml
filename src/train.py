import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Rutas Valohai
in_path = "/valohai/inputs/processed-data/processed.csv"
out_path = "/valohai/outputs"
os.makedirs(out_path, exist_ok=True)

# Leer inputs de Valohai
df = pd.read_csv(in_path)

X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, f"{out_path}/model.joblib")
print("Model trained and saved to Valohai outputs")
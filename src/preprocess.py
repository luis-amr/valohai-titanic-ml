import pandas as pd
import os

# Rutas salida de Valohai
out_path = "/valohai/outputs"
os.makedirs(out_path, exist_ok=True)

# Leer CSV del dataset original
df = pd.read_csv("data/train.csv")

# Preprocesamiento
df = df[["Pclass","Sex","Age","Fare","Survived"]]
df["Sex"] = df["Sex"].map({"male":0,"female":1})
df["Age"] = df["Age"].fillna(df["Age"].median())

# Guardar archivo procesado para Valohai
df.to_csv(f"{out_path}/processed.csv", index=False)
print("Dataset processed and saved to Valohai outputs")
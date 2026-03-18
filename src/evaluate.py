import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Rutas entrada de Valohai
data_path = "/valohai/inputs/processed-data/processed.csv"
model_path = "/valohai/inputs/trained-model/model.joblib"

# Cargamos datos y modelo
df = pd.read_csv(data_path)
X = df.drop("Survived", axis=1)
y = df["Survived"]

model = joblib.load(model_path)
pred = model.predict(X)
acc = accuracy_score(y, pred)

print("accuracy:", acc)
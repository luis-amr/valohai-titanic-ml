import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

df = pd.read_csv("processed.csv")
X = df.drop("Survived",axis=1)
y = df["Survived"]
model = joblib.load("model.joblib")
pred = model.predict(X)
acc = accuracy_score(y,pred)
print("accuracy:",acc)

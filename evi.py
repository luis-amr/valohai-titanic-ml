import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

df = pd.read_csv("data/titanic.csv")

features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
target = "Survived"

df = df[features + [target]].copy()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

train_df, prod_df = train_test_split(
    df, test_size=0.3, random_state=42, stratify=df[target]
)

X_train = train_df.drop(columns=[target])
y_train = train_df[target]

X_prod = prod_df.drop(columns=[target])
y_prod = prod_df[target]

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

train_pred = model.predict(X_train)
prod_pred = model.predict(X_prod)

print("Accuracy train:", accuracy_score(y_train, train_pred))
print("Accuracy prod :", accuracy_score(y_prod, prod_pred))

reference_data = X_train.copy()
reference_data[target] = y_train.values
reference_data["prediction"] = train_pred

current_data = X_prod.copy()
current_data[target] = y_prod.values
current_data["prediction"] = prod_pred

report = Report(metrics=[DataDriftPreset()])

report.run(
    reference_data=reference_data,
    current_data=current_data
)

report.save_html("reporte_drift_titanic.html")
print("Reporte generado: reporte_drift_titanic.html")
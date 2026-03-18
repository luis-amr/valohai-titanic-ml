import pandas as pd
df = pd.read_csv("train.csv")
df = df[["Pclass","Sex","Age","Fare","Survived"]]
df["Sex"] = df["Sex"].map({"male":0,"female":1})
df["Age"] = df["Age"].fillna(df["Age"].median())
df.to_csv("processed.csv",index=False)
print("Dataset processed")

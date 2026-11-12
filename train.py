import pandas as pd, sqlite3, joblib
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv("IndiaTelecomData.csv").dropna().drop_duplicates()
df = df[df["data_used"] >= 0]
df.to_sql("customers", sqlite3.connect("telco.db"), if_exists="replace", index=False)
X = df[["age", "num_dependents", "estimated_salary", "calls_made", "sms_sent", "data_used"]]
joblib.dump(RandomForestClassifier().fit(X, df["churn"]), "model.pkl")

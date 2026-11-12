from flask import Flask, request
import joblib, pandas as pd, sqlite3
app = Flask(__name__)
model = joblib.load("model.pkl")
form = "<form><input name='id'></form>"

@app.route("/")
def home():
    db = sqlite3.connect("telco.db")
    p = pd.read_sql("SELECT * FROM customers WHERE customer_id = ?", db, params=[request.args.get("id")])
    if p.empty:
        return form + "Not found"
    risk = model.predict_proba(p[model.feature_names_in_])[0][1]
    return form + f"<h3>Churn risk: {risk:.0%}</h3>" + p.T.to_html(header=False)
app.run()

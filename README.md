# Customer Churn Prediction (Indian Telco)

A small web app that predicts how likely a telecom customer is to churn (leave). Type a customer ID and it shows the churn risk and the customer's full record.

## How it works
1. `train.py` loads `IndiaTelecomData.csv`, removes missing rows, duplicates and rows with negative `data_used` (59 invalid rows).
2. The cleaned customers are stored in a SQLite table (`telco.db`).
3. A Random Forest is trained on six numeric columns (age, dependents, salary, calls, SMS, data used) and saved as `model.pkl`.
4. `app.py` is a Flask app. It fetches the customer with a SQL `SELECT`, predicts the churn risk and shows it with the customer's record.

## Tech
Python, Pandas, SQLite, scikit-learn, Flask

## Run it
```
pip install -r requirements.txt
python train.py
python app.py
```
Open `http://127.0.0.1:5000/`, type a customer ID such as `2` and press Enter.
Customers removed during cleaning (for example ID `1`, which had negative data usage) show "Customer not found".

## Results and limitations
- About 19% of customers churn, so a model that always says "no churn" is already about 80% accurate. Accuracy is therefore not a useful measure here; ROC-AUC is used instead.
- In testing (5-fold cross-validation), ROC-AUC was about 0.5, which is the same as random guessing. No feature in this dataset is related to churn, so the predicted risk is not meaningful.
- The project shows the full pipeline (cleaning, SQL, model, web app). With a dataset that has real churn signal, the same code would work unchanged apart from column names.
- Learning project, not for real business decisions.

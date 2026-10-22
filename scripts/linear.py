from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(
    "https://github.com/whitead/dmol-book/raw/main/data/curated-solubility-dataset.csv"
)
features_start_at = list(data.columns).index("MolWt")
feature_names = "MolLogP"#, "MolWt"  #data.columns[features_start_at:]
features = [feature_names]

train, test = train_test_split(data, test_size = 0.2, random_state=42)

## Standardize Features

lr = Pipeline([
    ('scaler', StandardScaler()),
    ('lr', LinearRegression())])

X, y = train[features], train["Solubility"]
X_test, y_test = test[features], test["Solubility"]

lr.fit(X, y)
y_pred = lr.predict(X_test)

root_mean_squared_error(y_test, y_pred)
r2_score(y_test, y_pred)

plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, 'black')
plt.show()

plt.close()

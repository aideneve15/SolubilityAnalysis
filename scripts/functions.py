import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(features = True):
    data = pd.read_csv("https://github.com/whitead/dmol-book/raw/main/data/curated-solubility-dataset.csv")
    features_start_at = list(data.columns).index("MolWt")
    feature_names = data.columns[features_start_at:]
    features = feature_names.to_list()

    if features:
        return data, features
    else:
        return data
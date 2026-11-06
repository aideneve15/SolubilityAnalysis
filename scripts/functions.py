import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit import RDLogger

def load_data(return_features = True, metadata_only = False):
    data = pd.read_csv("https://github.com/whitead/dmol-book/raw/main/data/curated-solubility-dataset.csv")
    features_start_at = list(data.columns).index("MolWt")
    feature_names = data.columns[features_start_at:]
    features = feature_names.to_list()

    # if metadata_only:
    #     features_start_at = list(data.columns).index("MolWt")
    #     metadata_columns = list(data.columns)[features_start_at]
    #     data = data[:metadata_columns]
    if return_features:
        return data, features
    else:
        return data

def get_morgan_feats(df, suppress_warnings = False):
    if suppress_warnings:
        lg = RDLogger.logger() 
        lg.setLevel(RDLogger.CRITICAL) ## Suppress warnings

    fpgen = AllChem.GetMorganGenerator(radius = 2, fpSize = 2048)
    rows = []
    column_names = ['SMILES'] + [f"bit_{i}" for i in range(2048)]
    for smile in df['SMILES']:
        mol = Chem.MolFromSmiles(smile)
        if mol is None: continue
        fp = list(fpgen.GetFingerprint(mol))
        
        rows.append([smile] + fp)

    new_df = pd.DataFrame(rows, columns = column_names)

    return new_df
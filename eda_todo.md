

Potential outliers in `NumAromaticRings`:

```
smiles = data[data['NumAromaticRings'] > 10]['SMILES']
smiles = smiles.values
m = Chem.MolFromSmiles(smiles[4])
Draw.MolToImage(m)
```
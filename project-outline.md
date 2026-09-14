# Aqueous Solubility Prediction: Classical Baseline vs. PyTorch MLP

## Overall Goal

Build a rigorous, well-documented comparison of a classical regression baseline against a PyTorch neural network for predicting aqueous solubility from molecular structure — demonstrating chemistry domain fluency, RDKit/feature-engineering skill, numerical-methods rigor, and practical PyTorch competence in a single, defensible piece of work.

**The question this project answers:** does a small neural net actually learn something a well-chosen classical model misses, and if so, where?

---

## 1. Framing & Success Criteria

Before touching code, write a short problem statement covering:
- **What** you're predicting: log aqueous solubility
- **Why** it matters: a real pharma/materials-relevant property, not an arbitrary benchmark target
- **What success looks like**: e.g., the MLP should beat the baseline's RMSE by a meaningful margin — or, just as valid, document that it doesn't and explain why

Decide this now so the goalposts don't move later.

*Aligns with: Ch. 2, "Introduction to Machine Learning" — the book's framing of what deep learning adds over classical methods.*

---

## 2. Load the Dataset & Explore It (EDA)

Pull in **AqSolDB** (~10,000 compounds, SMILES + measured solubility + the book's 17 built-in descriptors). Check distributions, look for outliers or duplicate structures, visualize the solubility target, and confirm there's no leakage or obviously broken rows before building anything on top of it.

*Aligns with: Ch. 2 (dataset introduction), Ch. 1, "Tensors and Shapes" (useful for getting comfortable with how the data is shaped once it moves into arrays/tensors).*

---

## 3. RDKit Feature Engineering (Original Extension)

This is the part the book doesn't hand you — it uses precomputed descriptors, but here you compute your own directly from SMILES with RDKit. Pick a deliberate, chemically-justified set:

- Molecular weight
- LogP
- TPSA (topological polar surface area)
- H-bond donor/acceptor counts
- Rotatable bond count
- Aromatic ring proportion

This is the same family of descriptors the original ESOL paper found predictive — avoid just importing every descriptor RDKit offers. Write a short paragraph justifying *why* each descriptor should relate to solubility; that reasoning is the actual feature-engineering skill being showcased, not just the code that computes them.

*No direct chapter — this is intentionally beyond the source material, worth stating explicitly in the write-up as a point of differentiation.*

---

## 4. Classical / Numerical Baseline Model

Fit OLS (or nonlinear least squares) on the engineered descriptors, with a proper train/test split and evaluation metrics.

**Numerical-methods tie-in:** implement gradient descent by hand for the linear case and compare it against scipy/sklearn's solver — same coefficients, different convergence path. This mirrors the book's own from-scratch teaching approach and gives a concrete "I understand what's happening under the hood" talking point.

*Aligns with: Ch. 2 (manual gradient-descent example), Ch. 3, "Regression & Model Assessment" (evaluation methodology, train/test discipline).*

---

## 5. PyTorch MLP Model

Same engineered features, same split. Build a small feedforward network (2–3 hidden layers) and train it properly: loss curves, a validation set, light hyperparameter tuning (a modest sweep is enough — don't over-invest here). Keep it apples-to-apples with the baseline so the comparison stays honest.

*Aligns with: Ch. 6, "Deep Learning Overview" (PyTorch fundamentals — tensors, autograd, training loop), Ch. 7, "Standard Layers" (the dense-layer building blocks), Ch. 11, "Explaining Predictions" (the book's own dense NN on this exact dataset — read closely as a direct reference point).*

---

## 6. Compare & Evaluate

Head-to-head on the held-out test set:
- RMSE, R²
- Parity plots
- Residual plots for both models
- Feature importance (coefficient magnitudes for the baseline, permutation importance for the MLP)

Write an honest paragraph on where the nonlinear model helps and where it doesn't — that discussion is what elevates this from "I trained two models" to "I understand my models."

*Aligns with: Ch. 3 (assessment methodology, reused here), Ch. 11 (explainability techniques applicable to interpreting the MLP).*

---

## 7. Write-Up & Publish

Structure the report as: **problem statement → data → methods (baseline + MLP) → results → discussion**.

- Clean notebook (restarted kernel, run top to bottom) → GitHub, with a README summarizing the project and key plots
- Quarto-rendered HTML report → personal website
- Optional PDF export from the same Quarto source, for direct attachment to applications

---

## 8. Stretch Goal (Only If Time Remains)

A graph neural network operating directly on molecular structure rather than hand-picked descriptors. Note in the write-up that this is the natural next step, citing that the book itself builds exactly this model on the same dataset.

*Aligns with: Ch. 8, "Graph Neural Networks."*

---

## Reference: dmol.pub Chapters Used

| Step | Chapter | Link |
|---|---|---|
| Framing / dataset intro | Ch. 2, Introduction to Machine Learning | `ml/introduction.html` |
| Data shapes/tensors | Ch. 1, Tensors and Shapes | `math/tensors-and-shapes.html` |
| Classical baseline | Ch. 3, Regression & Model Assessment | `ml/regression.html` |
| PyTorch fundamentals | Ch. 6, Deep Learning Overview | `dl/introduction.html` |
| Dense layers | Ch. 7, Standard Layers | `dl/layers.html` |
| PyTorch MLP reference | Ch. 11, Explaining Predictions | `dl/xai.html` |
| Stretch goal | Ch. 8, Graph Neural Networks | `dl/gnn.html` |
| Optional enrichment | Ch. 5, Kernel Learning | `ml/kernel.html` |

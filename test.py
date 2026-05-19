# Test scikit-learn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
clf = RandomForestClassifier()
clf.fit(iris.data, iris.target)
print(f"✅ Scikit-learn OK! Accuracy: {clf.score(iris.data, iris.target):.2f}")

# Test PyTorch
import torch

x = torch.rand(3, 3)
print(f"\n✅ PyTorch OK! Version: {torch.__version__}")
print(f"Tensor:\n{x}")

# Test library lainnya
import numpy as np
import pandas as pd
import matplotlib
import plotly

print(f"\n✅ NumPy: {np.__version__}")
print(f"✅ Pandas: {pd.__version__}")
print(f"✅ Matplotlib: {matplotlib.__version__}")
print(f"✅ Plotly: {plotly.__version__}")
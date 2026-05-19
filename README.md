# 🐧 Arch Linux Data Science Setup

A personal documentation of setting up an AI and Data Science environment on Arch Linux from scratch — covering environment configuration, library installation, and verification of core tools used for graduate-level research.

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.x | Core programming language |
| PyTorch | 2.12.0+cu130 | Deep learning & neural networks |
| Scikit-learn | Latest | Classical machine learning |
| NumPy | 2.4.5 | Numerical computing |
| Pandas | 3.0.3 | Data manipulation & analysis |
| Matplotlib | 3.10.9 | Static data visualization |
| Plotly | 6.7.0 | Interactive data visualization |
| JupyterLab | Latest | Interactive computing environment |

## ⚙️ Environment Setup

This project uses `uv` as the Python package manager inside a virtual environment — a modern, fast alternative to pip recommended for Arch Linux systems.

### 1. Install uv
```bash
sudo pacman -S python-pipx
pipx install uv
pipx ensurepath
```

### 2. Create virtual environment
```bash
mkdir ~/datascience && cd ~/datascience
uv venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
uv pip install numpy pandas matplotlib seaborn plotly scipy scikit-learn
uv pip install jupyter jupyterlab
uv pip install torch torchvision torchaudio
```

## ✅ Verification

Run `test.py` to verify all libraries are correctly installed:

```bash
python test.py
```

Expected output:
✅ Scikit-learn OK! Accuracy: 1.00
✅ PyTorch OK! Version: 2.12.0+cu130
✅ NumPy: 2.4.5
✅ Pandas: 3.0.3
✅ Matplotlib: 3.10.9
✅ Plotly: 6.7.0

## 📁 Project Structure
arch_linux_data-science/
│
├── 00_Try_Vscode_folder/
│   └── test.py        # Library verification script
└── README.md

## 🎯 Purpose

This repository is part of my preparation for graduate study (S2), documenting the process of building a reproducible data science environment on Linux for research in geophysics, geospatial analysis, and applied machine learning.

## 👤 Author

**Muhd. Zhafir Ar-Radhi**  
Geophysics | Data Science | Prompt Engineering  
📧 zhafirmuhammad06@gmail.com  
🐙 [@zhafirmuhammad06202](https://github.com/zhafirmuhammad06202)
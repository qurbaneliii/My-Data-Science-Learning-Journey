# My Data Science Learning Journey

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11+-blue" alt="Python Version" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status" />
  <img src="https://img.shields.io/badge/Notebooks-Jupyter-orange" alt="Jupyter" />
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-blue" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Data-Pandas%20%7C%20NumPy-lightgrey" alt="Pandas NumPy" />
  <img src="https://img.shields.io/badge/Viz-Matplotlib%20%7C%20Seaborn-purple" alt="Visualization" />
</p>

End-to-end data science learning journey — from Python fundamentals through machine learning pipelines, covering real datasets, SQL integration, EDA, classification, regression, encoding, and imbalanced-data handling.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [Datasets](#datasets)
- [Quick Start](#quick-start)
- [Roadmap](#roadmap)
- [Notes & Language](#notes--language)
- [License](#license)

---

## Overview

This repository is a structured, hands-on record of my progress in data science and machine learning. It spans multiple phases:

1. **Python fundamentals** — syntax, data structures, functions, mini-projects
2. **Data analysis & visualization** — Pandas, NumPy, Matplotlib, Seaborn
3. **Machine learning** — supervised learning, classification, regression, encoding, imbalanced data
4. **End-to-end ML pipeline** — data ingestion from PostgreSQL, preprocessing, modeling, evaluation, visualization

---

## Repository Structure

```
My-Data-Science-Learning-Journey/
│
├── python learning journey/              # Phase 1 – Python Basics
│   ├── practice and experiment 1.ipynb   Core Python: data structures, slicing, comprehensions
│   ├── Python task 1.ipynb               Arithmetic, strings, type conversion
│   ├── Python task 2.ipynb               Sets, functions, comprehensions, sorting
│   ├── test and small projects 1.ipynb   Mini-projects: calculator, login, grade converter
│   ├── matplotlib_practice.ipynb         Matplotlib plotting exercises
│   └── Qurbaneli Feyzullayev 134 (1).ipynb  Assignment notebook
│
├── Data/                                 # Phase 2 & 3 – ML & Data Science Notebooks
│   ├── Supervised_Machine_Learning.ipynb                          Theory: supervised learning concepts
│   ├── Basic_Concept_of_Classification_(Data_Mining).ipynb        Classification in data mining
│   ├── Getting_started_with_Classification.ipynb                  Hands-on classification
│   ├── Polynomial Regression Model.ipynb                          Polynomial regression from scratch
│   ├── Polynomial Regression.ipynb                               Applied polynomial regression
│   ├── Polynomial_Regression_and_Logistic_Regression.ipynb        Regression comparison
│   ├── ML___Understanding_Data_Processing (2).ipynb               EDA & preprocessing
│   ├── ML___Dummy_variable_trap_in_Regression_Models (1).ipynb    One-hot encoding & dummy trap
│   ├── One_Hot_Encoding_in_Machine_Learning.ipynb                 Encoding categorical features
│   ├── Label_Encoding_in_Python.ipynb                             Label encoding techniques
│   ├── ML___Handling_Imbalanced_Data_with_SMOTE_and_Near_Miss_Algorithm_in_Python.ipynb
│   ├── Loan-Approval-Prediction-Dataset.ipynb                     End-to-end loan prediction
│   ├── ML projectt 1.ipynb                                        Personal ML project
│   └── Lorenz Attractor.ipynb                                     Chaos theory simulation
│
├── ML pipeline/                          # Phase 4 – Production-style ML Pipeline
│   ├── ml_pipeline.ipynb   Full pipeline: PostgreSQL → EDA → preprocessing → modeling → evaluation
│   └── ml.py               Python script version of the pipeline
│
├── examples/
│   └── mini_apps.py        Reusable utility functions refactored from notebook snippets
│
├── requirements.txt
└── README.md
```

---

## Topics Covered

### Python Fundamentals
- Data structures: lists, tuples, sets, dictionaries
- String manipulation, type conversion, slicing, indexing
- List / dict / set comprehensions
- Functions: parameters, scope, `global` keyword
- Control flow: conditionals, loops, input handling
- Mini-projects: calculator, login attempts, grade converter, data filters

### Data Analysis & Visualization
- Exploratory Data Analysis (EDA) with Pandas
- Data cleaning: missing values, outliers, type casting
- Visualization with Matplotlib and Seaborn (line, bar, scatter, heatmap, pairplot)

### Machine Learning — Theory & Practice

| Topic | Notebook |
|---|---|
| Supervised Learning concepts | `Supervised_Machine_Learning.ipynb` |
| Classification theory (Data Mining) | `Basic_Concept_of_Classification_(Data_Mining).ipynb` |
| Classification hands-on | `Getting_started_with_Classification.ipynb` |
| Polynomial Regression | `Polynomial Regression Model.ipynb` |
| Logistic Regression | `Polynomial_Regression_and_Logistic_Regression.ipynb` |
| Data preprocessing & feature engineering | `ML___Understanding_Data_Processing (2).ipynb` |
| One-Hot Encoding & Dummy Variable Trap | `ML___Dummy_variable_trap_in_Regression_Models (1).ipynb` |
| Label Encoding | `Label_Encoding_in_Python.ipynb` |
| Imbalanced data: SMOTE & NearMiss | `ML___Handling_Imbalanced_Data_with_SMOTE_and_Near_Miss_Algorithm_in_Python.ipynb` |
| End-to-end prediction project | `Loan-Approval-Prediction-Dataset.ipynb` |

### End-to-End ML Pipeline (`ML pipeline/`)
- PostgreSQL database connection via SQLAlchemy
- Raw data ingestion (Seoul Bike Sharing dataset)
- Column normalization and null value handling
- Feature engineering & train/test split
- Model training, evaluation, and result visualization

---

## Datasets

| File | Description |
|---|---|
| `Iris.csv` | Classic iris flower classification dataset |
| `Admission_Predict_Ver1.1.csv` | Graduate admission prediction |
| `aug_train.csv` | HR analytics / employee job change data |
| `IT_customer_churn.csv` | Customer churn in the IT sector |
| `water_potability.csv` | Water quality and potability classification |
| `data.csv` | General-purpose dataset |
| `Employees.sql` | Employee records (SQL) |
| `France.sql` | France region data (SQL) |
| `Store.sql` | Retail store data (SQL) |
| `World.sql` | World countries data (SQL) |

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/qurbaneliii/My-Data-Science-Learning-Journey.git
cd My-Data-Science-Learning-Journey

# Create and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install notebook pandas numpy matplotlib seaborn scikit-learn imbalanced-learn sqlalchemy

# Launch Jupyter Notebook
jupyter notebook
```

### Suggested Learning Path

1. `python learning journey/practice and experiment 1.ipynb` — Python basics
2. `Data/ML___Understanding_Data_Processing (2).ipynb` — EDA & preprocessing
3. `Data/Basic_Concept_of_Classification_(Data_Mining).ipynb` — Classification theory
4. `Data/Getting_started_with_Classification.ipynb` — Classification in practice
5. `Data/Polynomial Regression Model.ipynb` — Regression models
6. `Data/One_Hot_Encoding_in_Machine_Learning.ipynb` + `Label_Encoding_in_Python.ipynb` — Encoding
7. `Data/ML___Handling_Imbalanced_Data_with_SMOTE...ipynb` — Imbalanced data
8. `ML pipeline/ml_pipeline.ipynb` — Full end-to-end pipeline

---

## Roadmap

- [x] Python fundamentals and mini-projects
- [x] Data visualization with Matplotlib & Seaborn
- [x] Supervised learning theory and classification
- [x] Regression models (polynomial, logistic)
- [x] Feature encoding (one-hot, label)
- [x] Imbalanced data handling (SMOTE, NearMiss)
- [x] End-to-end ML pipeline with PostgreSQL integration
- [ ] Deep learning introduction (Keras / TensorFlow)
- [ ] Time series analysis
- [ ] Model deployment (Flask / FastAPI)
- [ ] Add unit tests for pipeline functions
- [ ] Refactor notebooks with type hints and `ruff` linting

---

## Notes & Language

Some variable names, comments, and markdown cells are written in **Azerbaijani** (the author's native language). All code follows standard Python conventions and is fully functional regardless of comment language.

---

## Security Note

Login examples in early notebooks use plaintext credentials for demonstration purposes only. In production, always store password hashes (e.g., `hashlib.pbkdf2_hmac`) and never hard-code secrets.

---

## License

Personal learning repository — free to browse and learn from. No warranty provided.

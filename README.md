# Understanding-Core-ML-Concepts-Training-Optimization-Regularization-and-Model-Interpretability
 This project is an interactive web dashboard built using Flask that allows users to understand how machine learning models train and behave. The main goal is to visualize the core concepts of ML, such as training behavior, overfitting, regularization, and feature importance, in a clear and accessible way.
# -> ML Training Visualizer Dashboard

An interactive **Flask-based dashboard** to visualize and understand core machine learning training concepts such as **overfitting**, **underfitting**, **loss minimization**, **regularization**, and **feature importance** using real-world datasets.

---

## -> Project Purpose

This tool was built to help learners, educators, and developers **visualize how machine learning models train and make predictions**. It focuses on interpretability, offering real-time insights into training dynamics and model behavior.

---

## -> Features

-  **Upload any CSV** dataset with numerical/categorical features and a binary target
-  Choose between **Logistic Regression** and **Decision Tree** models
-  Add optional **L1/L2 regularization** (Logistic Regression)
-  Auto-generated **plots**:
  - Training vs Test Accuracy
  - **Confusion Matrix**
  - **ROC-AUC Score**
  - **Feature Importance**
-  Real-time **input prediction** with confidence score
-  Educational insights into **overfitting**, **underfitting**, and **generalization**

---

##  Folder Structure

ml_training_visualizer/
│
├── app.py # Flask application (main backend)
├── uploads/ # Stores uploaded CSV files
├── static/ # Generated plots (feature importance, confusion matrix)
├── templates/ # HTML templates (upload, train, predict)
├── utils/
│ └── ml_helpers.py # ML logic: training, preprocessing, plotting, prediction
├── requirements.txt
└── README.md


---

##  Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ml-training-visualizer.git
cd ml-training-visualizer

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

pip install -r requirements.txt

python app.py

```

# SaaS Customer Churn Prediction

## 📌 Project Overview

This project uses machine learning classification techniques to predict whether a customer is likely to churn from a SaaS (Software as a Service) business.

The project covers data exploration, preprocessing, feature scaling, model training, evaluation, and saving the trained model. It also includes a Streamlit application for interacting with the project.

## 🎯 Objective

The main objective is to build machine learning models that can identify customers who may be likely to leave a SaaS service.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook
- Streamlit

## 📂 Project Files

- `customer_churn_dataset.csv` — Dataset used for the project.
- `saas _customer_churn_prediction.ipynb` — Jupyter Notebook containing the machine learning workflow.
- `model.pkl` — Saved trained model.
- `scaler.pkl` — Saved feature scaler.
- `app.py` — Streamlit application.

## 🔄 Project Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Train-Test Split
5. Feature Scaling using `MinMaxScaler`
6. K-Nearest Neighbors (KNN) Classification
7. Random Forest Classification
8. Model Evaluation
9. Saving the model and scaler using Joblib
10. Creating a Streamlit application using `app.py`

## 📊 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset and examine the available customer information before applying machine learning models.

## ⚙️ Data Preprocessing

The dataset was prepared for machine learning by performing the required preprocessing steps. The data was divided into training and testing sets, and feature scaling was performed using `MinMaxScaler`.

## 🤖 Machine Learning Models

### 1. K-Nearest Neighbors (KNN)

A KNN classifier was used to predict customer churn.

```python
KNeighborsClassifier(n_neighbors=4)
```

### 2. Random Forest Classifier

A Random Forest classifier was also trained to predict customer churn. The model's performance was evaluated alongside the KNN classifier.

## 📈 Model Evaluation

The trained models were evaluated using the performance metrics calculated in the project.

The evaluation results can be reviewed in the Jupyter Notebook.

## 💾 Model Saving

The trained model and feature scaler were saved using Joblib so they could be reused by the application.

- `model.pkl`
- `scaler.pkl`

## 🌐 Streamlit Application

The project includes a Streamlit application (`app.py`) that provides an interface for interacting with the customer churn prediction model.

### Run the Application Locally

1. Open a terminal in the project folder.
2. Install Streamlit if it is not already installed:

```bash
python -m pip install streamlit
```

3. Start the application:

```bash
python -m streamlit run app.py
```

4. Open the local URL displayed in the terminal to use the application.

## 🚀 Future Improvements

- Improve model performance through further experimentation.
- Enhance the application interface.
- Add additional visualizations to help interpret customer churn predictions.

## 👩‍💻 Author

Preethip

# SaaS Customer Churn Prediction

## 📌 Project Overview

This project focuses on predicting customer churn in a SaaS business using machine learning classification techniques.

The project includes data exploration, preprocessing, feature scaling, model training, and evaluation.

## 🎯 Objective

The main objective of this project is to build a machine learning model that can predict whether a customer is likely to churn.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook

## 🔄 Project Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Train-Test Split
5. Feature Scaling using MinMaxScaler
6. K-Nearest Neighbors (KNN) Classification
7. Random Forest Classification
8. Model Evaluation
9. Model Saving using Joblib

## 📊 Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the dataset and examine the available customer information before applying machine learning models.

## ⚙️ Data Preprocessing

The dataset was prepared for machine learning by performing the required preprocessing steps.

The data was divided into:

- Training data
- Testing data

Feature scaling was performed using `MinMaxScaler`.

## 🤖 Machine Learning Models

### 1. K-Nearest Neighbors (KNN)

A KNN classifier was trained using:

```python
KNeighborsClassifier(n_neighbors=4)

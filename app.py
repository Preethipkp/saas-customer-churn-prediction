import streamlit as st
import pandas as pd
import joblib


# load model
model = joblib.load("model.pkl")
scaler=joblib.load("scaler.pkl")


st.title("SaaS Customer Churn Prediction")


# 3 Inputs

account_age = st.number_input(
    "Account Age Days"
)


login = st.selectbox(
    "Login Frequency",
    ["Rarely", "Weekly", "Daily"]
)


daily_usage = st.number_input(
    "Daily Usage Minutes"
)


# Encode Login Frequency

login_map = {
    "Rarely":0,
    "Weekly":1,
    "Daily":2
}


if st.button("Predict"):


    data = pd.DataFrame({

        "Account_Age_Days":[account_age],

        "Login_Frequency":[
            login_map[login]
        ],

        "Daily_Usage_Mins":[daily_usage]

    })


    result = model.predict(data)


    if result[0] == 1:

        st.error("⚠️ Customer will Churn")

    else:

        st.success("✅ Customer will not Churn")
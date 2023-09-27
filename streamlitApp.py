import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

# Set Streamlit app title and page icon
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="✅",
)

# Streamlit app title and description
st.title("Diabetes Prediction App")
st.markdown("This app predicts diabetes based on user input.")

# Sidebar with user input fields
st.sidebar.header("User Input")

# Get user input features
pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, step=1)
glucose = st.sidebar.number_input("Glucose", min_value=0, max_value=200, step=1)
blood_pressure = st.sidebar.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, step=1)
skin_thickness = st.sidebar.number_input("Skin Thickness (mm)", min_value=0, max_value=100, step=1)
insulin = st.sidebar.number_input("Insulin (mu U/ml)", min_value=0, max_value=500, step=1)
bmi = st.sidebar.number_input("BMI (kg/m²)", min_value=0.0, max_value=70.0, step=0.1)
diabetes_pedigree = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.0, step=0.01)
age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)

# Create a data frame with user input
user_input = pd.DataFrame({
    "Pregnancies": [pregnancies],
    "Glucose": [glucose],
    "BloodPressure": [blood_pressure],
    "SkinThickness": [skin_thickness],
    "Insulin": [insulin],
    "BMI": [bmi],
    "DiabetesPedigreeFunction": [diabetes_pedigree],
    "Age": [age]
})

# Predict diabetes
if st.sidebar.button("Predict"):
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(user_input)

    # Display prediction result
    if results[0] == 1:
        st.error("You may have diabetes.")
    else:
        st.success("You may not have diabetes.")

# Streamlit app footer
st.sidebar.text("Designed By: Ayodele Ayodeji")
st.sidebar.text("Connect with me on LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/ayo-ayodeji/)")

# Streamlit app description
st.subheader("About This App")
st.markdown(
    "This web app predicts the likelihood of diabetes based on user-provided input features. "
    "The prediction is made using a machine learning model. Enter your information on the left sidebar "
    "and click the 'Predict' button to get your result."
)

# Streamlit app source code
st.subheader("Explore the Code")
st.markdown(
    "Visit the GitHub repository to explore the code and documentation: "
    "[GitHub Repository](https://github.com/yourusername/your-repo)"
)

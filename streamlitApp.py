import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

# Define the paths to your HTML templates
home_template_path = "streamlitTemplates/index.html"
index_template_path = "streamlitTemplates/home.html"

# Render the "Home" tab
def home():
    with open(home_template_path, "r") as file:
        html_content = file.read()
    html(html_content, width=800, height=600, scrolling=True)

# Render the "Prediction" tab
def prediction():
    with open(index_template_path, "r") as file:
        html_content = file.read()
    html(html_content, width=800, height=600, scrolling=True)

# Create the Streamlit app
def main():
    st.title("Diabetes Prediction App")

    # Create tabs for "Home" and "Prediction"
    tabs = ["Home", "Prediction"]
    selected_tab = st.radio("Select a Tab", tabs)

    if selected_tab == "Home":
        home()
    elif selected_tab == "Prediction":
        st.subheader("Diabetes Risk Prediction")

        # Get user input features
        pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=13, step=1)
        glucose = st.sidebar.number_input("Glucose", min_value=44, max_value=199, step=1)
        blood_pressure = st.sidebar.number_input("Blood Pressure (mm Hg)", min_value=24, max_value=122, step=1)
        skin_thickness = st.sidebar.number_input("Skin Thickness (mm)", min_value=24, max_value=122, step=1)
        insulin = st.sidebar.number_input("Insulin (mu U/ml)", min_value=0, max_value=415, step=1)
        bmi = st.sidebar.number_input("BMI (kg/m²)", min_value=18.2, max_value=55.0, step=0.1)
        diabetes_pedigree = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=1.0, step=0.01)
        age = st.sidebar.number_input("Age", min_value=21, max_value=68, step=1)

        # Make a prediction
        if st.button("Get Prediction"):
            predict_pipeline = PredictPipeline()

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
            result = predict_pipeline.predict(user_input)
        # Display prediction result
            if result[0] == 1:
                st.error("You may have diabetes.")
            else:
                st.success("Congrats! You do not have diabetes.")


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
                "[GitHub Repository](https://github.com/Fortunatetech/Diabetes-Prediction-with-Deployment-Using-flask-streamlit-DVC)"
            )


if __name__ == "__main__":
    main()

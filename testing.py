import streamlit as st
from streamlit.components.v1 import html

# Define the paths to your HTML templates
home_template_path = "streamlitTemplates/home.html"
index_template_path = "streamlitTemplates/index.html"

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
        prediction()

if __name__ == "__main__":
    main()

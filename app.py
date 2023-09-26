from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for predicting a data point
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Pregnancies=request.form.get('Pregnancies'),
            Glucose=request.form.get('Glucose'),
            BloodPressure=request.form.get('BloodPressure'),
            SkinThickness=request.form.get('SkinThickness'),
            Insulin=request.form.get('Insulin'),
            BMI=request.form.get('BMI'),
            DiabetesPedigreeFunction=request.form.get('DiabetesPedigreeFunction'),
            Age=request.form.get('Age')
        )
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Modify this part to display the result message
        if results[0] == 1:
            result_message = "Yes, you have diabetes."
        else:
            result_message = "Congrats! You do not have diabetes."

        return render_template('home.html', result_message=result_message)

if __name__ == "__main__":
    app.run(debug=True)

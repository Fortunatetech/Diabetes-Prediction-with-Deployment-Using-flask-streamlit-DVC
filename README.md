# Diabetes Prediction App

![Alt text](<diabete Pic-1.png>)

## Table of Contents

- [About](#about)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Use](#how-to-use)
- [Input Features](#input-features)
- [Sample Data](#sample-data)
- [Real-time Demo](#real-time-demo)
- [Explore the Code](#explore-the-code)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

The Diabetes Prediction App is a web application that allows users to assess their risk of developing diabetes based on their health data. This tool provides real-time predictions and empowers individuals to make informed decisions about their health.

## Key Features

- Input health data and receive real-time diabetes risk predictions.
- Interactive and user-friendly interface.
- Easy integration of the prediction model into other applications.

## Getting Started

### Prerequisites

Before running the app, make sure you have the following prerequisites installed:

- Python 3.11.5
- Flask (for running the web app)
- Required Python libraries (see requirements.txt)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Fortunatetech/Diabetes-Prediction-with-Deployment-Using-flask-streamlit-DVC.git
   ```

2. Navigate to the project directory:

   ```bash
   cd diabetes-prediction-app
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

The app should now be running locally. You can access it in your web browser at `http://localhost:5000`.

## How to Use

1. Navigate to the [Prediction Page](http://localhost:5000/predictdata).
2. Enter your health data, including pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function score, and age.
3. Click the "Get Prediction" button to receive your real-time diabetes risk prediction.

## Input Features

The features required for diabetes risk prediction are as follows:

- **Pregnancies**: Number of pregnancies (integer).
- **Glucose**: Fasting blood glucose level (mg/dL) (float).
- **Blood Pressure**: Resting blood pressure (mm Hg) (integer).
- **Skin Thickness**: Skinfold thickness (mm) (integer).
- **Insulin**: Fasting serum insulin level (mu U/ml) (integer).
- **BMI (Body Mass Index)**: Current BMI (kg/m²) (float).
- **Diabetes Pedigree Function**: Diabetes pedigree function score (float).
- **Age**: Age in years (integer).

## Sample Data

For your convenience, you can download a sample dataset [here](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset).

## Real-time Demo

![Demo](project demo\diabete video demo.mp4)

[Watch the demo video](project demo\diabete video demo.mp4)

## Explore the Code

Visit our [GitHub repository](https://github.com/Fortunatetech/Diabetes-Prediction-with-Deployment-Using-flask-streamlit-DVC) to explore the code, contribute, or report issues.

## Contributing

Contributions are welcome! Please read our [Contribution Guidelines](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the Apache License 2.0 LICENSE - see the [LICENSE](LICENSE) file for details.

## Contact

- Ayodele Ayodeji
- LinkedIn: [Connect with me](https://www.linkedin.com/in/ayo-ayodeji/)
- Twitter: [Connect with me](https://twitter.com/Ayo_dataanalyst)
- Email: ayodeleayodeji250@gmail.com

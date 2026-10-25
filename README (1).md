# Car Insurance Claim Prediction

A Machine Learning project that predicts whether a car insurance claim is likely to be approved based on customer, vehicle, and policy-related information.

The project follows a complete ML pipeline including data preprocessing, exploratory data analysis, model training, evaluation, prediction, and risk scoring.

---

## Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation
- Insurance claim prediction
- Risk score generation
- Saved trained model for inference

---

## Project Structure

```
Insurance-Prediction/
│
├── data/
│   └── Car Insurance Claim Prediction - Project.csv
│
├── models/
│   └── best_model.pkl
│
├── outputs/
│
├── src/
│   ├── eda.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── risk_scoring.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>.git
```

### 2. Navigate to the project folder

```bash
cd Insurance-Prediction
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the main application

```bash
python main.py
```

Depending on your implementation, the project will:

- Load the dataset
- Preprocess the data
- Train or load the saved model
- Evaluate performance
- Generate predictions
- Calculate risk scores

---

## Running Individual Modules

### Exploratory Data Analysis

```bash
python src/eda.py
```

### Data Preprocessing

```bash
python src/preprocessing.py
```

### Train Model

```bash
python src/train.py
```

### Evaluate Model

```bash
python src/evaluate.py
```

### Make Predictions

```bash
python src/predict.py
```

### Generate Risk Scores

```bash
python src/risk_scoring.py
```

---

## Model

The trained machine learning model is stored in:

```
models/best_model.pkl
```

This model is loaded during prediction to classify insurance claim outcomes.

---

## Dataset

The dataset used is:

```
data/Car Insurance Claim Prediction - Project.csv
```

It contains customer, vehicle, and policy information used for training and prediction.

---

## Output

The project generates:

- Trained machine learning model
- Evaluation metrics
- Prediction results
- Risk scores
- Output files inside the `outputs` directory

---

## Future Improvements

- Build a Streamlit web application
- Deploy the model using Flask/FastAPI
- Hyperparameter optimization
- Feature importance visualization
- Support batch prediction from CSV files
- Model monitoring and retraining

---

## Author

**V.CHINNACHAMY**




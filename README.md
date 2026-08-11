# concrete-strength-ann-prediction
# 🧱 Concrete Strength Prediction using Artificial Neural Network

A Machine Learning project that predicts the **compressive strength of concrete** based on its mixture components and curing age.

The project uses an **Artificial Neural Network (ANN)** built with TensorFlow/Keras to learn the relationship between concrete composition and its compressive strength.

---

## 🚀 Project Overview

Concrete strength depends on several factors such as the amount of cement, water, aggregates, additives, and the age of the concrete.

This project takes **8 input parameters** and predicts the expected **Concrete Compressive Strength in MPa**.

### Input Features

| Feature            | Description                          |
| ------------------ | ------------------------------------ |
| Cement             | Cement quantity in kg/m³             |
| Blast Furnace Slag | Blast furnace slag quantity in kg/m³ |
| Fly Ash            | Fly ash quantity in kg/m³            |
| Water              | Water quantity in kg/m³              |
| Superplasticizer   | Superplasticizer quantity in kg/m³   |
| Coarse Aggregate   | Coarse aggregate quantity in kg/m³   |
| Fine Aggregate     | Fine aggregate quantity in kg/m³     |
| Age                | Age of concrete in days              |

### 🎯 Output

**Predicted Concrete Compressive Strength (MPa)**

---

## 🧠 Machine Learning Model

The project uses an **Artificial Neural Network (ANN)** with the following architecture:

```text
Input Layer
    ↓
Dense Layer: 64 neurons + ReLU
    ↓
Dense Layer: 32 neurons + ReLU
    ↓
Output Layer: 1 neuron
```

The model contains **2,689 trainable parameters**.

### Training Configuration

* Optimizer: Adam
* Learning Rate: 0.01
* Loss Function: Mean Squared Error (MSE)
* Metric: Mean Absolute Error (MAE)
* Epochs: 50
* Validation: 20% test data
* Early Stopping: Enabled

---

## 📊 Model Performance

The model was evaluated using the test dataset.

| Metric   |     Result |
| -------- | ---------: |
| MAE      | 4.7383 MPa |
| MSE      |    42.1720 |
| RMSE     | 6.4940 MPa |
| R² Score | **0.8586** |

### ⭐ R² Score: 85.86%

An R² score of **0.8586** means that the model explains approximately **85.86% of the variation** in concrete compressive strength on the test data.

The average prediction error measured by MAE is approximately **4.74 MPa**.

---

## 🧪 Example Prediction

For example, the following concrete mixture can be given to the model:

```text
Cement:              540
Blast Furnace Slag:  0
Fly Ash:             0
Water:               162
Superplasticizer:    2.5
Coarse Aggregate:    1040
Fine Aggregate:      676
Age:                  28 days
```

The model produced:

```text
Predicted Concrete Strength: 64.68 MPa
```

The notebook includes an interactive input section where users can enter their own values and receive a prediction.

---

## 🔄 How the Prediction Works

```text
User enters concrete mixture values
              ↓
       Input is collected
              ↓
      StandardScaler
              ↓
       ANN Model (.keras)
              ↓
   Predicted Strength in MPa
```

The same scaler used during training must be used when making predictions. The project therefore stores the trained scaler separately as `scaler.pkl`.

---

## 💾 Saved Model Files

The repository contains the trained model and preprocessing object:

```text
concrete_strength_model.keras
scaler.pkl
```

### `concrete_strength_model.keras`

Contains the trained Artificial Neural Network.

### `scaler.pkl`

Contains the `StandardScaler` used to scale the input features before prediction.

Keeping both files is important because the model expects the input data to be scaled in the same way as during training.

---

## 📁 Project Structure

```text
Concrete-Strength-Prediction/
│
├── concrete_strength_model.keras
├── scaler.pkl
├── app.py
├── requirements.txt
├── Conrete_Strength_ANN.ipynb
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* TensorFlow
* Keras
* Matplotlib
* Joblib

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Concrete-Strength-Prediction
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

Then enter the required concrete mixture values when prompted.

---

## 🌐 Deployment

This project can be deployed so that users can make predictions without running the Jupyter Notebook.

The trained model and scaler are loaded directly:

```python
from tensorflow.keras.models import load_model
import joblib

model = load_model("concrete_strength_model.keras")
scaler = joblib.load("scaler.pkl")
```

The user only needs to provide the 8 input values.

---

## 📈 Model Development

The original dataset contains **1,030 rows and 9 columns**, including 8 input features and 1 target variable. The dataset was checked for missing values and duplicate records. 25 duplicate rows were identified and removed before training.
The data was divided into training and testing sets using an **80/20 split** and the input features were standardized using `StandardScaler`.

---

## 🎯 Objective

The main objective of this project is to build a practical machine learning model that can estimate concrete compressive strength from its mixture composition and age.

This project demonstrates:

* Data preprocessing
* Feature scaling
* Train-test splitting
* Artificial Neural Networks
* Model evaluation
* Model saving
* User-based prediction
* Machine Learning model deployment

---

## 👨‍💻 Author

**Karthik Kumar**

Aspiring Data Analyst / Machine Learning Enthusiast

---

## ⭐ If you find this project useful

Feel free to explore the repository, use the trained model, and improve the project further.

**Built with Python, TensorFlow and Machine Learning.**



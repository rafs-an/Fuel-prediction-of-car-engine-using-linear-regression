🚗 Fuel Consumption Prediction using Machine Learning
📌 Overview

This project is a Machine Learning web application that predicts a car’s fuel consumption (L/100 km) based on its engine specifications and driving characteristics.

It uses a Linear Regression model trained on real vehicle data and is deployed using a Flask web app for interactive predictions.

🎯 Problem Statement

Predict the combined fuel consumption (L/100 km) of a vehicle using:

Engine size
Number of cylinders
City fuel consumption
Highway fuel consumption

This helps understand how different car attributes affect fuel efficiency.

⚙️ Tech Stack
Python 🐍
Pandas
Scikit-learn
Flask
Joblib
HTML (Frontend)
CSS (Optional styling)
🧠 Machine Learning Model
Algorithm: Linear Regression
Target Variable: Combined (L/100 km)
Features Used:
Engine size (L)
Cylinders
City (L/100 km)
Highway (L/100 km)
📊 Model Performance
R² Score: ~0.99 (on dataset)
Indicates strong correlation between features and fuel consumption
📂 Project Structure
FuelPredictionML/
│
├── app.py # Flask backend
├── trainModel.py # Model training script
├── model.pkl # Saved ML model
├── fuelData.csv # Dataset
├── requirements.txt # Dependencies
│
├── templates/
│ └── index.html # Web UI

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/fuel-prediction-ml.git
cd fuel-prediction-ml
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the Flask app
python app.py
4️⃣ Open in browser
http://127.0.0.1:5000/
🖥️ Features
Predict fuel consumption instantly
Simple web interface
Real-time user input
Machine Learning powered backend
📊 Example Prediction

Input:

Engine size: 2.0 L
Cylinders: 4
City: 9.5 L/100 km
Highway: 7.0 L/100 km

Output:

Predicted Fuel Consumption: ~8.3 L/100 km

📚 What I Learned
End-to-end ML pipeline (data → model → deployment)
Linear Regression in real-world datasets
Flask web development
Model serialization using Joblib
Basic full-stack ML deployment

🔥 Future Improvements
Try Random Forest / Gradient Boosting models
Add UI improvements (modern frontend)
Deploy on cloud (Render / Railway)
Add feature importance visualization

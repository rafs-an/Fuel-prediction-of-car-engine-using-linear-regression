from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    engine = float(request.form["engine"])
    cylinders = float(request.form["cylinders"])
    city = float(request.form["city"])
    highway = float(request.form["highway"])

    sample = pd.DataFrame([[
        engine, cylinders, city, highway
    ]], columns=[
        "Engine size (L)",
        "Cylinders",
        "City (L/100 km)",
        "Highway (L/100 km)"
    ])

    prediction = model.predict(sample)[0]

    return render_template("index.html", prediction=round(prediction, 2))


if __name__ == "__main__":
    app.run(debug=True)
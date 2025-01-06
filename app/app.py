import pickle
import numpy as np
import pandas as pd 
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

#load model 
with open('model/rf_model.pkl', 'rb') as model_file : 
    rf_model = pickle.load(model_file)


print(rf_model)

@app.route('/')
def home() : 
    return render_template('index.html')

@app.route('/predict', methods= ['POST'])
def predict() : 
    data = [
        float(request.form['gender']),
        float(request.form['age']),
        float(request.form['education']),
        float(request.form['currentSmoker']),
        float(request.form['cigsPerDay']),
        float(request.form['BPMeds']),
        float(request.form['prevalentStroke']),
        float(request.form['prevalentHyp']),
        float(request.form['diabetes']),
        float(request.form['totChol']),
        float(request.form['sysBP']),
        float(request.form['diaBP']),
        float(request.form['BMI']),
        float(request.form['heartRate']),
        float(request.form['glucose']),
    ]

    feature_names = ['gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']

    input_df = pd.DataFrame([data], columns=feature_names)

    prediction = rf_model.predict(input_df)
    probability = rf_model.predict_proba(input_df)[:, 1]
    
    #result predict
    result = {
        'prediction' : 'CHD' if prediction[0] == 1 else 'Non CHD',
        'probability' : round(probability[0], 4)
    }
    print(f"Prediction: {result['prediction']}, Probability: {result['probability']}")
    return render_template('index.html', predict = result['prediction'], probability = result['probability'])

if __name__ == '__main__' : 
    app.run(debug=True)
   

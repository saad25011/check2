from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = int(request.form['Gender'])
        HasPartner = int(request.form['HasPartner'])
        SubscriptionType = int(request.form['SubscriptionType'])
        Total_Subscription_Cost = int(request.form['Total_Subscription_Cost'])
        HasPhoneService = int(request.form['HasPhoneService'])
        PaymentMethod = int(request.form['PaymentMethod'])
        HasCloudSecurity = int(request.form['HasCloudSecurity'])
        HasStreamingMovies = int(request.form['HasStreamingMovies'])
        HasStreamingTV = int(request.form['HasStreamingMovies'])
        HasElectronicBilling = int(request.form['HasElectronicBilling'])
        ServiceDuration = int(request.form['ServiceDuration'])
        
        prediction = predict()

        
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave the bank")
        else:
             return render_template('index.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True)

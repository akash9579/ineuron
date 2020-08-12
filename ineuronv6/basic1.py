"""
In this we just creating home page and predict page 
"""

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle
import pandas as pd


app=Flask(__name__)

pickle_in = open("classifier1.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('home'))

@app.route('/predict',methods=['GET','POST'])
def predict():
    df=pd.read_csv('file.csv')
    #my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    #my_prediction=my_prediction.tolist()
    #my_prediction=df.head(5)
    #print(type(my_prediction))
    #my_prediction=my_prediction.values.tolist()
    #print(my_prediction)
    #return render_template('result.html',prediction = my_prediction)   
    data=df.drop(df.columns[0], axis = 1) 
    print(data.head())
    my_prediction=classifier.predict(data)
    print(my_prediction)
    #return "Welcome to prediction" 
    return render_template('result.html',prediction = my_prediction) 

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    

 
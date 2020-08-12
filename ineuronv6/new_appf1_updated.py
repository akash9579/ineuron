
import numpy as np
from flask import Flask,request
import pickle
import pandas as pd

app=Flask(__name__)
#Swagger(app)

#pickle_in = open("diabetes_prediction_5aug.pkl","rb")
pickle_in = open("classifier1.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
   return "Welcome All"


@app.route('/predict')
def diabetic_prediction():
    var = "akash"
    Age = request.args.get('Age')
    Gender = request.args.get('Gender')
    #Polyuria = request.args.get('Polyuria')
    #Polydipsia = request.args.get('Polydipsia')
    #sudden_weight_loss= request.args.get('sudden_weight_loss')
    #weakness = request.args.get('weakness')
    #Polyphagia = request.args.get('Polyphagia')
    #Genital_thrush = request.args.get('Genital_thrush')
    #visual_blurring = request.args.get('visual_blurring')
    #Itching = request.args.get('Itching')
    #Irritability = request.args.get('Irritability')
    #delayed_healing = request.args.get('delayed_healing')
    #partial_paresis = request.args.get('partial_paresis')
    #muscle_stiffness = request.args.get('muscle_stiffness')
    #Alopecia = request.args.get('Alopecia')
    #Obesity = request.args.get('Obesity')
    return "Welcome to prediction" 

    #prediction=classifier.predict([[Age,Gender,Polyuria,Polydipsia,sudden_weight_loss,
    #                                  weakness,Polyphagia,Genital_thrush,
    #
    #                                  visual_blurring,Itching,
    #                                  Irritability,delayed_healing,
    #                                  partial_paresis,muscle_stiffness,
    #                                  Alopecia,Obesity]])
    #print(prediction)




@app.route('/predict_file',methods=["POST"])
def predict_bulk_file():

    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    #prediction=classifier.predict(df_test)
    
    #return str(list(prediction))
    return "Welcome to prediction" 

if __name__=='__main__':
    app.run()
    
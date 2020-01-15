from numpy import loadtxt
from keras.models import load_model
import pandas as pd
import training as t
import mapsh as mp

notif=""
def test(age,sex,cp,trestbps,chol,fbs,restcg,thalach,exang,oldpeak,slope,ca,thal):
    global notif
    t.user(age,sex,cp,trestbps,chol,fbs,restcg,thalach,exang,oldpeak,slope,ca,thal)
    model = load_model('trainingH.h5')
    model.summary()

    data1=pd.read_csv('t.csv')
    data=pd.read_csv("heart.csv")
    OutputY= data.iloc[:,13]
    training=data1.iloc[:,:13]

    predictions = model.predict(training) 
    rounded = [round(x[0]) for x in predictions]
    predictions = model.predict_classes(training)

    for i in range(1):
        print((predictions[i]))
        if(predictions[i][0]==[1]):
            
            notif="It's seems you have Cardiac disease"
        else:
            
            notif="Most probably you don't have Cardiac disease"    

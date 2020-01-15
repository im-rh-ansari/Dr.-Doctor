from numpy import loadtxt
from keras.models import load_model
import pandas as pd
import trainingd as t
import maps as mp
notif=""
def test(pregnancies,glucose,bp,skinthickness,insulin,bmi,dpf,age):
    global notif
    t.user(pregnancies,glucose,bp,skinthickness,insulin,bmi,dpf,age)
    model = load_model('trainingD.h5')
    model.summary()

    data1=pd.read_csv('d.csv')
    data=pd.read_csv("pima-indians-diabetes.csv")
    OutputY= data.iloc[:,8]
    training=data1.iloc[:,:8]

    predictions = model.predict(training) 
    rounded = [round(x[0]) for x in predictions]
    predictions = model.predict_classes(training)

    for i in range(1):
        print('%s(predicted)' %(predictions[i]))
        if(predictions[i]==1):
            notif="It's seems you have Diabetes"
        else:
            notif="Most probably you don't have diabetes"         
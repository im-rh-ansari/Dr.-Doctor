import pandas as pd

def user(pregnancies,glucose,bp,skinthickness,insulin,bmi,dpf,age):
    '''pregnancies=int(input("Enter no. of times preganant: "))
    glucose=int(input("Enter plasma glucose concentration in a 2 hours oral glucose tolerance test: "))
    bp=int(input("Enter diastolic blood pressure(mm Hg):  "))
    skinthickness=int(input("Enter tricep skinfold thickness(mm): "))
    insulin=int(input("Enter 2 hour serum insulin(muU/ml): "))
    bmi=float(input("Enter body mass index(weight in Kg/(height in m)^2: "))
    dpf=float(input("Enter DiabetesPedigreeFunction : "))
    age=int(input("Enter age: "))'''
    pregnancies=[pregnancies]
    glucose=[glucose]
    bp=[bp]
    skinthickness=[skinthickness]
    insulin=[insulin]
    bmi=[bmi]
    dpf=[dpf]
    age=[age]
    dictionary={"pregnancies":pregnancies,"glucose":glucose,"bp":bp,"skin Thick":skinthickness,"Insulin":insulin,"bmi":bmi,"dpf":dpf,"age":age}
    df=pd.DataFrame(dictionary)
    df.to_csv('D:\Ennovate/d.csv',index=False)

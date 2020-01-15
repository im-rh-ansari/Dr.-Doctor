import pandas as pd

def user(age,sex,cp,trestbps,chol,fbs,restcg,thalach,exang,oldpeak,slope,ca,thal):
    '''age=int(input("Enter age: "))
    sex=int(input("Enter sex(0: female,1:male): "))
    cp=int(input("Enter Chest type ranging from 0 to 3: "))
    trestbps=int(input("Enter resting blood pressure(in mm Hg on admission to the hospital): "))
    chol=int(input("Enter serum cholestrol in mg/dl: "))
    fbs=int(input("Enter 0(false) or 1(true) (fasting blood sugar> 120 mg/dl): "))
    restcg=int(input("Enter resting electrocardiographic results: "))
    thalach=int(input("Enter maximum heart rate achieved: "))
    exang=int(input("Enter exercise induced angima(1=yes;0=no): "))
    oldpeak=float(input("ST depression induced by exercise relative to rest:  "))
    slope=int(input("Enter the slope of the peak exercise:  "))
    ca=int(input("Enter number of major vessels(0-3) colored by flouroscopy: "))
    thal=int(input("Enter 3=normal,6=fixed defect,7=reversible defect: "))'''
    age=[age]
    sex=[sex]
    cp=[cp]
    trestbps=[trestbps]
    chol=[chol]
    fbs=[fbs]
    restcg=[restcg]
    thalach=[thalach]
    exang=[exang]
    oldpeak=[oldpeak]
    slope=[slope]
    ca=[ca]
    thal=[thal]
    dictionary={"age":age,"sex":sex,"cp":cp,"trestbps":trestbps,"chol":chol,"fbs":fbs,"restcg":restcg,"thalach":thalach,"exang":exang,"oldpeak":oldpeak,"slope":slope,"ca":ca,"thal":thal}
    df=pd.DataFrame(dictionary)
    df.to_csv('D:\Ennovate/t.csv',index=False)


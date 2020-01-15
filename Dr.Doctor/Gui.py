import tkinter as tk
import testingdiabetes as td
import testingheart as th
import mapsh as mh
import maps as md
age=""
sex=""
cp=""
trestbps=""
chol=""
fbs=""
restcg=""
thalach=""
exang=""
oldpeak=""
slope=""
ca=""
thal=""
pregnancies=""
glucose=""
bp=""
skinthickness=""
insulin=""
bmi=""
dpf=""
notif=""
from PIL import Image,ImageTk
    
def create_window():
    root=tk.Toplevel(window)
    root.title("Cardiac Disease")
    background_boy(root)
    root.configure(background='black')
    root.state("zoomed")
    message = tk.Label(root, text="Cardiac Disease Testing Center", bg="blue", fg="white", width=43,
                   height=1, font=('times', 30, 'italic bold'))
    message.place(x=170, y=10)
    lbl = tk.Label(root, text="Enter age", width=8, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lbl.place(x=100, y=80)
    txt = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt.place(x=750, y=80)

    lbl2 = tk.Label(root, text="Enter sex(0: female,1:male)", width=20, fg="black", bg="#ededed", height=2, font=('times', 15, ' bold '))
    lbl2.place(x=100, y=130)
    txt2 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt2.place(x=750, y=130)

    lbl3 = tk.Label(root, text="Enter Chest type ranging from 0 to 3: ", width=27, fg="black", bg="#ededed", height=2,
                font=('times', 15, ' bold'))
    lbl3.place(x=100, y=180)
    txt3 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt3.place(x=750, y=180)

    lb4 = tk.Label(root, text="Enter resting blood pressure(in mm Hg on admission to the hospital)", width=48, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lb4.place(x=100, y=230)
    txt4 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt4.place(x=750, y=230)

    lb5 = tk.Label(root, text="Enter serum cholestrol in mg/dl", width=22, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lb5.place(x=100, y=280)
    txt5 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt5.place(x=750, y=280)
    
    lb6 = tk.Label(root, text="Enter 0(false) or 1(true) (fasting blood sugar> 120 mg/dl)", width=40, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lb6.place(x=100, y=330)
    txt6 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt6.place(x=750, y=330)

    lb7 = tk.Label(root, text="Enter resting electrocardiographic results", width=30, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lb7.place(x=100, y=380)
    txt7 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt7.place(x=750, y=380)

    lb8 = tk.Label(root, text="Enter maximum heart rate achieved", width=26, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lb8.place(x=100, y=430)
    txt8 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt8.place(x=750, y=430)

    lb9 = tk.Label(root, text="Enter exercise induced angima(1=yes;0=no)", width=31, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lb9.place(x=100, y=480)
    txt9 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt9.place(x=750, y=480)

    lb10 = tk.Label(root, text="ST depression induced by exercise relative to rest", width=35, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lb10.place(x=100, y=530)
    txt10 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt10.place(x=750, y=530)

    lbl11 = tk.Label(root, text="Enter the slope of the peak exercise", width=26, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lbl11.place(x=100, y=580)
    txt11 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt11.place(x=750, y=580)

    lbl12 = tk.Label(root, text="Enter number of major vessels(0-3) colored by flouroscopy", width=41, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lbl12.place(x=100, y=630)
    txt12 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt12.place(x=750, y=630)

    lbl13 = tk.Label(root, text="Enter 3=normal,6=fixed defect,7=reversible defect", width=35, height=2, fg="black", bg="#ededed", font=('times', 15, ' bold '))
    lbl13.place(x=100, y=680)
    txt13 = tk.Entry(root, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt13.place(x=750, y=680)

    def map():
        mh.mapping()

    def register():
        age=txt.get()
        sex=txt2.get()
        cp=txt3.get()
        trestbps=txt4.get()
        chol=txt5.get()
        fbs=txt6.get()
        restcg=txt7.get()
        thalach=txt8.get()
        exang=txt9.get()
        oldpeak=txt10.get()
        slope=txt11.get()
        ca=txt12.get()
        thal=txt13.get()
        th.test(age,sex,cp,trestbps,chol,fbs,restcg,thalach,exang,oldpeak,slope,ca,thal)
        message = tk.Label(root, text=th.notif, bg="#ededed", fg="blue", width=40, height=2, activebackground="red",
                   font=('times', 15, ' bold '))
        message.place(x=600, y=400)
        
    trainImg = tk.Button(root, text="Ok", command=register, fg="black", bg="red", width=20, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
    trainImg.place(x=1200, y=100)
    map_button=tk.Button(root,text="Hospital Near Me",command=map,fg="black",bg="red",width=20,height=3,
                     activebackground="Red",font=('times',15,'bold'))
    map_button.place(x=1200, y=200)                
    back_button=tk.Button(root,text="Back",command=root.destroy,fg="black",bg="red",width=20,height=3,
                     activebackground="Red",font=('times',15,'bold'))
    back_button.place(x=1200,y=300)                     


def create_window2():
    root1=tk.Toplevel(window)
    root1.title("Dibetes")
    root1.state("zoomed")
    background_boy(root1)
    #root1.configure(background='white')
    message = tk.Label(root1, text="Diabetes Testing Center", bg="black", fg="white", width=43,
                   height=1, font=('times', 30, 'italic bold'))
    message.place(x=170, y=20)
    def map():
        md.mapping()
    def call():
        pregnancies=txt.get()
        glucose=txt2.get()
        bp=txt3.get()
        skinthickness=txt4.get()
        insulin=txt5.get()
        bmi=txt6.get()
        dpf=txt7.get()
        age=txt8.get()
        td.test(pregnancies,glucose,bp,skinthickness,insulin,bmi,dpf,age)
        message = tk.Label(root1, text=td.notif, bg="#ededed", fg="blue", width=35, height=2, activebackground="blue",
                   font=('times', 15, ' bold '))
        message.place(x=470,y=150)      
    trackImg = tk.Button(root1, text="Ok", command=call, fg="black", bg="red", width=20, height=3,
                activebackground="Red", font=('times', 15, ' bold '))
    trackImg.place(x=1200, y=200)
    map_button=tk.Button(root1,text="Hospitals near me",command=map,fg="black",bg="red",width=20,height=3,
                     activebackground="Red",font=('times',15,'bold'))
    map_button.place(x=1200, y=300)             
    back_button=tk.Button(root1,text="Back",command=root1.destroy,fg="black",bg="red",width=20,height=3,
                     activebackground="Red",font=('times',15,'bold'))
    back_button.place(x=1200, y=400)

    lbl = tk.Label(root1, text="Enter no. of times preganant ", width=20, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl.place(x=100, y=200)
    txt = tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt.place(x=750, y=200)

    lbl2 = tk.Label(root1, text="Enter plasma glucose concentration in a 2 hours oral glucose tolerance test ", width=53, fg="black", bg="white", height=2,
                font=('times', 15, ' bold'))
    lbl2.place(x=100, y=250)
    txt2 = tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt2.place(x=750, y=250)

    lbl3 = tk.Label(root1, text="Enter diastolic blood pressure(mm Hg)", width=27, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl3.place(x=100, y=300)
    txt3 = tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt3.place(x=750, y=300)

    lbl4 = tk.Label(root1, text="Enter tricep skinfold thickness(mm)", width=25, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl4.place(x=100, y=350)
    txt4 = tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt4.place(x=750, y=350)

    lbl5 = tk.Label(root1, text="Enter 2 hour serum insulin(muU/ml)", width=25, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl5.place(x=100, y=400)
    txt5 = tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt5.place(x=750, y=400)

    lbl6 = tk.Label(root1, text="Enter body mass index(weight in Kg/(height in m)^2", width=37, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl6.place(x=100, y=450)
    txt6= tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt6.place(x=750, y=450)

    lbl7= tk.Label(root1, text="Enter DiabetesPedigreeFunction", width=23, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl7.place(x=100, y=500)
    txt7 = tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt7.place(x=750, y=500)

    lbl8 = tk.Label(root1, text="Enter age", width=7, height=2, fg="black", bg="white", font=('times', 15, ' bold '))
    lbl8.place(x=100, y=550)
    txt8= tk.Entry(root1, width=20, bg="blue", fg="white", font=('times', 15, ' bold '))
    txt8.place(x=750, y=550)


window=tk.Tk()
window.title("Home")
window.configure(background="#832cd6")
window.state("zoomed")
background_label = tk.Label(window, background="#474747", width=165, height=34)
background_label.place(x=100, y=120)
image = Image.open("images.jpg")
background_image = ImageTk.PhotoImage(image)
def background_boy(nameofwindow):
    background_label = tk.Label(nameofwindow, image=background_image)
    background_label.place(x=0, y=0,relwidth=1,relheight=1)
background_boy(window)

head = tk.Label(window, text="Dr.Doctor",bg="green3", fg="white", width=30,
                   height=1, font=('Times New Roman',30,'italic'))
head.place(x=420, y=20)
admin = tk.Button(window, text="Diabetes", command=create_window2, fg="white", bg="blue", width=70, height=3,
                     activebackground="Red", font=('Helvetica', 15, ' bold '))
admin.place(x=350, y=190)                   
attendance_button= tk.Button(window, text="Cardiac Disease", command=create_window, fg="white", bg="blue", width=70, height=3,
                     activebackground="Red", font=('Helvetica', 15, ' bold '))
attendance_button.place(x=350, y=380)
Quit_button=tk.Button(window,text="Quit",command=window.destroy,fg="white",bg="blue", width=70, height=3,
                    activebackground="Red", font=('times',15,'bold'))
Quit_button.place(x=350,y=570)

window.mainloop()
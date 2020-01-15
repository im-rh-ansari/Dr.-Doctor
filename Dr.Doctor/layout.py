import testingheart as th
import testingdiabetes as tb

interest=int(input("For what diesease (diabetes:1; Cardiac:2): "))
if(interest==1):
    tb.test()
elif(interest==2):
    th.test()
else:
    print("Incorrect option!!!")            
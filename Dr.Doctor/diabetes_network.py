from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

data=pd.read_csv("pima-indians-diabetes.csv")
# split into input (X) and output (y) variables
print(data.describe(include='all'))
InputX= data.iloc[:,:8]
OutputY= data.iloc[:,8]


from keras import regularizers
model = Sequential()
model.add(Dense(18, input_dim=8, activation='relu',kernel_regularizer=regularizers.l2(l=0.1)))
model.add(Dense(10, activation='relu',kernel_regularizer=regularizers.l2(l=0.1)))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(InputX,OutputY, epochs=900, batch_size=10)
model.save("trainingD.h5")
print("Saved model to disk")
_, accuracy = model.evaluate(InputX,OutputY)
print('Accuracy: %.2f' % (accuracy*100))


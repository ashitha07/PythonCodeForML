 # Plot simple linear regression prediction model 
from matplotlib import pyplot as plt
import numpy as np

#This function computes f(x) = wx + b given values of x
def compute(x,w,b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w*x[i]+b
    return f_wb

# Input values - features 
x_train = np.array([1.0,2.0])
# Output values - target
y_train = np.array([300.0,500.0])
# Number of values
m = len(x_train)

#Plotting the prediction vs actual values
w = 200
b = 100
f_wb = compute(x_train,w,b)

plt.scatter(x_train,y_train,marker='x',c='r',label="Actual values")
plt.plot(x_train,f_wb,c='b',label='Prediction')
plt.title("Housing data")
plt.xlabel("Size")
plt.ylabel("Prize")
plt.show()

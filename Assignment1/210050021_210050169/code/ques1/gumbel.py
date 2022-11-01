import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
mu = 1 
b = 2


# this function takes a scalr value
def gumb(a):
    return math.exp(-math.exp(-(a-mu)/b))*math.exp(-(a-mu)/b)/b

def var():
    # this generates a array of 1000 elements consisting of equally spaced real numbers netween -10 and 10
    x = np.linspace(-100, 100, 10000)
    x = list(x)
    meanX = 0
    for i in x:
        meanX += i*gumb(i)*0.02
    meanX2 = 0
    for i in x:
        meanX2 += (i**2)*gumb(i)*0.02
    
    return meanX2 - meanX**2


# This function takes input as a numpy array and calculate the Reiman sum for all values in x->array
def integral(x, f):
    start = np.array([-1000.0 for i in range(1000)])
    res = np.array([0.0 for i in range(1000)])
    
    while np.any(start < x):
        a =  start < x
        y = f(start)
        for i, j in enumerate(a):
            if j:
                res[i] += y[i]*(0.05)
                start[i] += 0.05
    return res

# This function takes input as numpy array
def gumbelPDF(x):
    return np.exp(-np.exp(-(x-mu)/b))*np.exp(-(x-mu)/b)/b


# finding the variance, simply using the var function
print("Variance for Gumbel Distribution: ",var())

# plotting the graph
x = np.linspace(-10, 10, 1000)
plt.plot(x, gumbelPDF(x), color='red', label="PDF")
plt.legend()
plt.show()
plt.plot(x, integral(x, gumbelPDF), color='blue', label="CDF")
plt.legend()
plt.show()
import math
import numpy as np
from matplotlib import pyplot as plt

# this function takes a scalr value
def lap(a):
    return math.exp(-abs(a-mu)/b)/(2*b)

def var():
    # this generates a array of 1000 elements consisting of equally spaced real numbers netween -10 and 10
    x = np.linspace(-100, 100, 10000)
    x = list(x)
    meanX = 0
    for i in x:
        meanX += i*lap(i)*0.02
    meanX2 = 0
    for i in x:
        meanX2 += (i**2)*lap(i)*0.02
    
    return meanX2 - meanX**2

mu = 2
b = 2

# This function takes input as numpy array
def laplace(x):
   return np.exp(-np.abs(x-mu)/b)/(2*b)


# This function takes input as a numpy array and calculate the Reiman sum for all values in x->array
def integral(x, f):
    start = np.array([-1000.0 for i in range(1000)])
    res = np.array([0.0 for i in range(1000)])
    
    while np.any(start < x):
        a =  start < x
        lap = f(start)
        for i, j in enumerate(a):
            if j:
                res[i] += lap[i]*(0.02)
                start[i] += 0.02
    return res

# finding the variance, simply using the var function
print("Variance for Laplace Distribution: ",var())

x = np.linspace(-10, 10, 1000)

plt.plot(x, laplace(x), color='green', label="PDF")
plt.legend()
plt.show()

plt.plot(x, integral(x,laplace), color='red', label="CDF")
plt.legend()
plt.show()
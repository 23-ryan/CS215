import numpy as np
from matplotlib import pyplot as plt
import math


x_0 = 0
gama = 1

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
def cauchy(x):
    return 1/((math.pi)*gama*(1+((x-x_0)/gama)**2))

# this generates a array of 1000 elements consisting of equally spaced real numbers netween -10 and 10
x = np.linspace(-10, 10, 1000)

plt.plot(x, integral(x,cauchy), color='red', label="CDF")
plt.legend()
plt.show()
plt.plot(x, cauchy(x), color='blue', label="PDF")
plt.legend()
plt.show()
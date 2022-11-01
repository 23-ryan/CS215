import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc
import math

np.random.seed(23)

def M_Dist_CDF(x):
    x = list(x)
    Y = []
    for i in x:
        if(i<-1):
            Y.append(0)
        elif(i<0):
            Y.append((1-i**2)/2)
        elif(i<1):
            Y.append((1+i**2)/2)
        else:
            Y.append(1)
    Y = np.array(Y)
    return Y


def randomVarM_Shaped(n):
    U=sc.uniform.rvs(size=n) # generate uniform random numbers between 0 - 1
    U = list(U)
    X = []
    for i in U:
        if i < 0.5:
            X.append(-math.sqrt(1-2*i))
        elif i >  0.5:
            X.append(math.sqrt(2*i -1))
    X = np.array(X)
    return X


#plotting histogram for PDF
M_Distrib_DataSet=randomVarM_Shaped(100000)
plt.hist(M_Distrib_DataSet, bins=200, label="Generated r.v.")
plt.title("Histogram for M-Shaped")
plt.show()

# plotting CDF
x = np.linspace(-2, 2, num=1000, dtype=float)
plt.plot(x, M_Dist_CDF(x), "green")
plt.title("CDF for M-Shaped")

plt.show()
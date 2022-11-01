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


# this function generates the random variabels for the M-shaped distribution using the inverse method of calculating 
# random variables through probability.
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


# function which calcuates the dataset for average of "N" M-Shaped random variables
def avgM_Shaped(N):
    # generating N values of a random variables first <==> generating values of N - random variables (because independent)
    X = np.array([np.sum(randomVarM_Shaped(N))/N for i in range(10**4)])
    return X


# Histogram for Average M-Shaped for different N
# Give Data
plt.figure(figsize=(8,10))
for i in range(1, 7):
    avg_M_Shaped_Dataset = avgM_Shaped(2**i)
    plt.subplot(3,2,i)
    plt.hist(avg_M_Shaped_Dataset, bins=200, label="Generated r.v.")
    plt.title(f"N={2**i}")

plt.show()


#plottig avgM-Shaped distribution --> collectively
N_Values = [2**i for i in range(0, 7)]
for i in N_Values:
    avg_M_Shaped_Dataset = avgM_Shaped(i)
    unique, frequency = np.unique(avg_M_Shaped_Dataset, return_counts = True)
    probability = frequency/(10**4)
    plt.plot(unique, np.cumsum(probability)) # finding the cumulative using cumsum
    plt.title("CDF of Average M-Shaped")

plt.show()
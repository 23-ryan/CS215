import numpy as np
from matplotlib import pyplot as plt
import random
from tabulate import tabulate

np.random.seed(23)

steps = 10**3
stepSize = 10**(-3)
numSamples = 10**4
TRUE_VARIANCE = 10**(-3)
TRUE_MEAN = 0.0

color = ["red", "green", "black", "blue"]


# Function to plot the space time graphs for different random walkers
def randPosSpaceTime(k):
    a = np.random.randint(0, 2, (1,steps))
    posX = 0
    posY = 0
    if(k<1000):
        X = []
        Y = []
        for i in range(steps):
            if(a[0, i] == 0):
                posX -= stepSize
                posY += 1
                X.append(posX)
                Y.append(posY)
            elif(a[0, i] == 1):
                posX += stepSize
                posY += 1
                X.append(posX)
                Y.append(posY)
        plt.plot(X, Y, color[random.randint(0,3)])
        plt.title("Position Space Time")


# function to get the final location after 10^3 steps of a single random walker.
def randPos():
    a = np.random.randint(0, 2, (1,steps))
    pos = 0
    for i in range(steps):
        if(a[0, i] == 0):
            pos -= stepSize
        elif(a[0, i] == 1):
            pos += stepSize
    return pos

# mean random positions of different random Walkers
def meanRandPos(x):
    mean = 0
    for i in range(x.size):
        mean += x[i]
    return mean/x.size

# variance of positions of different random walkers
def varianceRandPos(x, mean):
    var = 0

    for i in range(x.size):
        var += (x[i]-mean)**2
    return var/x.size


# random paths plot
for i in range(steps):
    randPosSpaceTime(i)

plt.show()

# dataset for locations of different random walkers
x = np.array([randPos() for i in range(numSamples)])

# random location plot
n_bins = np.linspace(-1, 1, 500)
n_bins = list(n_bins)
plt.hist(x, bins=n_bins)
plt.title("Position Histogram")
plt.show()


# calculating the mean and variance
mean = meanRandPos(x)
variance = varianceRandPos(x, mean)

print(tabulate([['Mean', mean], ['Variance', variance]], headers=['Property', 'Value'], tablefmt='orgtbl'))
print("Mean: ",mean)
print("Variance: ",variance)

# ERROR in mean and variance
errorMean = ((mean - TRUE_MEAN))
errorVariance = ((variance - TRUE_VARIANCE))
print("Error in mean: ", errorMean)
print("Error in variance: ", errorVariance)






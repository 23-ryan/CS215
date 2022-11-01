# Interpret graph part has to be done

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

np.random.seed(23)

trueMean = 0.5

N_Array = [5, 10, 20, 40, 60, 80, 100, 500, 1000, 10000]


# generating the error data set to plot for Uniform Distribution over different sizes of datasets and 
# creating a boxplot for them.
plotData = []
for j in range(len(N_Array)):
    meanErrorArray = []
    for i in range(100):
        mean = np.sum(np.array([np.random.uniform(0, 1, size=N_Array[j])]))/N_Array[j]
        meanErrorArray.append(abs(mean-trueMean))
    meanErrorArray = np.array(meanErrorArray)
    plotData.append(meanErrorArray)


fig = plt.figure(figsize =(10, 7))
fig.suptitle('Uniform Distribution', fontsize=20)
plt.boxplot(plotData)

plt.show()


# generating the error data set to plot for Gaussian Distribution over different sizes of datasets and 
# creating a boxplot for them.
plotData = []
for j in range(len(N_Array)):
    meanErrorArray = []
    for i in range(100):
        mean = np.sum(np.array([np.random.normal(0.0, 1.0, size=N_Array[j])]))/N_Array[j]
        meanErrorArray.append(abs(mean-0.0))
    meanErrorArray = np.array(meanErrorArray)
    plotData.append(meanErrorArray)

fig = plt.figure(figsize =(10, 7))
fig.suptitle('Gaussian Distribution', fontsize=20)
plt.boxplot(plotData)
plt.show()

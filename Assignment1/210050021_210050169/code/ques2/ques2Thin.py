# CONFIRM
import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt
from functools import reduce
from tabulate import tabulate

np.random.seed(23)
mu1 = 3
mu2 = 4

samplePoints = 10**5
P = 0.8

r = sc.poisson.rvs(mu2, size=samplePoints)

unique, frequency = np.unique(r, return_counts = True)
frequencyNew = [0 for i in range(unique.size)]

for i in range(unique.size):
    if i in unique:
        b = sc.binom.rvs(unique[i], P, size=frequency[i])
        binomUnique, binomFrequency = np.unique(b, return_counts = True)
        for k,j in enumerate(binomUnique):
            frequencyNew[j] += binomFrequency[k]

frequencyNew = np.array(frequencyNew)
probability = frequencyNew/samplePoints

unique = np.array(unique)
probability = np.array(probability)


for i in range(26):
    if i not in unique:
        unique = np.append(unique, [i])
        probability = np.append(probability, [0])


# printint the generated dataset experimentally
print(tabulate([[unique[i], probability[i]] for i in range(26)], headers=['k', 'P(Z=k)'], tablefmt='orgtbl'))

plt.scatter(unique, probability, color='red', label="Experimental Plot")
plt.plot(unique, sc.poisson.pmf(unique, mu2*P), color='green', label="Actual plot")

plt.legend()
plt.show()
plt.savefig("ques2.png")

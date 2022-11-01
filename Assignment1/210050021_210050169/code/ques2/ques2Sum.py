# CONFIRM
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
from tabulate import tabulate

np.random.seed(23)

mu1 = 3
mu2 = 4

samplePoints = 10**6

r1 = poisson.rvs(mu1, size=samplePoints)
r2 = poisson.rvs(mu2, size=samplePoints)

r = r1 + r2

unique, frequency = np.unique(r, return_counts = True)

probability = frequency/samplePoints

unique = np.array(unique)
probability = np.array(probability)

for i in range(26):
    if i not in unique:
        unique = np.append(unique, [i])
        probability = np.append(probability, [0])


# printing the generated dataset experimentally
print(tabulate([[unique[i], probability[i]] for i in range(26)], headers=['k', 'P(Z=k)'], tablefmt='orgtbl'))

plt.scatter(unique, probability, color='red', label="Experimental Plot")
plt.plot(unique, poisson.pmf(unique, mu1+mu2), color='green', label="Actual Plot")

plt.legend()

plt.show()

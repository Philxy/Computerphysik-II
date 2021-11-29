from scipy.stats import poisson
from scipy import constants
import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2 a)

p = 1 / (50*np.power(10, 6))#
N = 135 * np.power(10, 6)
mean = N * p

k = np.arange(0, 10, 1)
poisson_dist = poisson.pmf(k, mean)

for i in range(4):
    print('Chance für', i, 'Mutationen:', poisson_dist[i])

plt.bar(k, poisson_dist)
plt.xlabel('Anzahl der Punktmutationen')
plt.title('Poissonverteilung der Punktmutationen')
plt.show()
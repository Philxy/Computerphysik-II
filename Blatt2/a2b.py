from scipy.stats import poisson
from scipy import constants
import numpy as np
import matplotlib.pyplot as plt

V = 1
dV = V  / 10
p = dV / V

N = 1000
n_mean = N * p


k = np.arange(0, N, 1)
plt.bar(k, poisson.pmf(k, n_mean))
plt.title('N = ' +  str(N) + ', V = 1 ' + ', $\Delta V$ = 1/10')
plt.xlabel('Anzahl Teilchen im Volumenelement $\Delta V$')
plt.savefig('2b ' + str(N)+'.png')
plt.grid(True)
plt.show()


x = np.arange(1, N, 1)
y = 1/np.sqrt(p*x)
plt.xlabel('Anzahl Teilchen')
plt.ylabel('Relative Breite $\sigma / \mu$')
plt.plot(x,y)
plt.show()


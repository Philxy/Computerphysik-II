from scipy.stats import binom, norm
import matplotlib.pyplot as plt
import numpy as np

N = [10,100,1000]
fig, axes = plt.subplots(nrows=1, ncols=len(N), figsize=(len(N)*5, 3))

i = 0

for n in N:
    k = np.arange(0, n + 1, 1)
    p = 0.5
    standard_derivation = np.sqrt(n*p*(1 - p))
    mean = n*p
    axes[i].bar(k, binom.pmf(k, n, p),  label=str(n), color='red')
    axes[i].plot(np.arange(0, n + 1, 0.01), norm.pdf(np.arange(0, n + 1, 0.01), mean, standard_derivation))
    axes[i].title.set_text('n = ' + str(n))
    i += 1


plt.show()



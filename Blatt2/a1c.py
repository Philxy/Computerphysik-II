from scipy.stats import norm, poisson
import matplotlib.pyplot as plt
import numpy as np


lambdas = [1, 3, 20]
n = 40


fig, axes = plt.subplots(nrows=1, ncols=len(lambdas),
                         figsize=(len(lambdas)*5, 5))

i = 0
for l in lambdas:
    p = l / n
    k = np.arange(0, n + 1, 1)
    mean = l
    standard_derivation = np.sqrt(l)
    axes[i].bar(k, poisson.pmf(k, l),  label='Poisson', alpha=0.5, color='r')
    axes[i].plot(np.arange(0, n + 1, 0.01), norm.pdf(np.arange(0,
                 n + 1, 0.01), mean, standard_derivation), label='Norm')
    axes[i].title.set_text('$\lambda = $ ' + str(l) + '  n = ' + str(n))
    i += 1

plt.legend()
plt.show()


# Man halte n konstant. Für größere Lambdas nähert sich die Poissonverteilund der 
# Binomialverteilung an.  
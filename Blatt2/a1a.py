from scipy.stats import binom, poisson
import matplotlib.pyplot as plt
import numpy as np


N = [10, 30, 100, 1000]
lam = 1


fig, axes = plt.subplots(nrows=1, ncols=len(N), figsize=(len(N)*5, 6))

i = 0
for n in N:
    p = lam / n
    k = np.arange(0, 10, 1)
    axes[i].bar(k, binom.pmf(k, n, p),  label='Binomial', alpha=0.5, color='b')
    axes[i].bar(k, poisson.pmf(k, lam),  label='Poisson', alpha=0.5, color='r')
    mean_difference = np.abs(lam - binom.mean(n, p))
    var_difference = np.abs(binom.var(n, p) - np.sqrt(lam))
    axes[i].title.set_text('n = ' + str(n) + '\n' + '$\mu_{Bin}-\mu_{Poss}$ = ' + str(
        mean_difference) + '\n' + '$\sigma_{Bin}-\sigma_{Poss}$ = ' + str(var_difference))

    i += 1

plt.legend()
plt.show()


# ==> Offenbar verschwindet die Abweichung zwischen der Binomial- und der Poissonverteilung für
# große N. Der Mittelwert der beiden Veteilungen unterscheidet sich nicht. Die Standartabweichungen
# nähern sich allerdings aneinander an.

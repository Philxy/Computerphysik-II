from scipy.stats import poisson
from scipy import constants
import numpy as np
import matplotlib.pyplot as plt

# Parameter des Volumens/Behältnis
V = 1
dV = V / 10
p = dV / V

# Teilchenzahl
N = 1000
n_mean = N * p

# Darstellung
k = np.arange(0, N, 1)
plt.bar(k, poisson.pmf(k, n_mean))
plt.title('N = ' + str(N) + ', V = 1 ' + ', $\Delta V$ = 1/10')
plt.xlabel('Anzahl Teilchen im Volumenelement $\Delta V$')
plt.savefig('2b ' + str(N)+'.png')
plt.grid(True)
plt.show()

# ==> Die verschiedenen angehängten Abbildungen zeigen, dass mit größerem n 
# die Breite im Verhältnis zu n abnimmt und somit die Schankung verschwindet 
# und das thermodynamische Mittel angenommen wird.  



# Relative Breite gegenüber der Teilchenzahl im Volumen
x = np.arange(1, N, 1)
y = 1/np.sqrt(p*x)
plt.xlabel('Anzahl Teilchen')
plt.ylabel('Relative Breite $\sigma / \mu$')
plt.plot(x, y)
plt.show()

# Die Asymptoten zeigen, dass die relative Breite für große n verschwindet und für kleine 
# n wächst. Der Zusammenhang ist proportional zu 1/sqrt(n*p).  


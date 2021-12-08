import utility as util
import matplotlib.pyplot as plt
import numpy as np


# Plotten der Hermitpolynome
for n in [0,1,2,3]:
    x_axis = np.arange(-3, 3, 0.1)
    y_axis = [(util.H_n(n))(x) for x in x_axis]
    plt.plot(x_axis, y_axis, label='n = ' + str(n))


plt.legend()
plt.show()


# Plotten der Wellenfunktionen
for n in [0,1,2,30]:
    x_axis = np.arange(-10, 10, 0.1)
    y_axis = [util.psi(n, x) for x in x_axis]
    plt.plot(x_axis, y_axis, label='n = ' + str(n))


# Berechnen der Unschärfe
print('Unschärfe mit n = 0:', util.uncertainty(0)**(.5))
print('Unschärfe mit n = 5:', util.uncertainty(5)**(.5))


plt.legend()
plt.show()



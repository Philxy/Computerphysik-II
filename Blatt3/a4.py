from scipy.special.orthogonal import hermitenorm
import utility as util
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, simplify


# Berechnung der Hermitpolynome mit Sympy
N = 30
x = symbols('x')
hermite_polynomials = [0] * N
hermite_polynomials[0] = 1
hermite_polynomials[1] = 2*x
for n in range(2, N):
    hermite_polynomials[n] = simplify(2*x*hermite_polynomials[n-1]-2*(n-1)*hermite_polynomials[n-2])

# Ausgabe der ersten 30 Hermitpolynome
for n, H in enumerate(hermite_polynomials):
    print('H_' + str(n) +'(x) =', H)


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



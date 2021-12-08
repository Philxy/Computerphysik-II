import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from sympy import hermite
from functools import partial

r_max = 20 
N = 1000
h = r_max/N 


# Integriert eine Beliebige Funktion f von im Intervall [a, b] mit der Trapezmethode (Mittelpunktsregel)
def integrate(f, a, b):
    integral = 0
    x = a
    while x <= b:
        integral += h * f((2 * x + h) / 2)
        x += h
    return integral


# Gibt den Wert der m-te Besselfunktion mit dem Argument r zurück
def bessel_func(r, m):
    def integrand(x):
        return np.cos(m * x - r * np.sin(x))

    return 1 / np.pi * integrate(integrand, 0, np.pi)


# Berechnet Hermit-Polynome mit der Rekursionsvorschrift
def hermite_polynomial(n,x):
    if n == 0:
        return 1.0
    elif n == 1:
        return 2 * x
    else:
        return 2*x*hermite_polynomial(n-1, x) - 2*(n-1)*hermite_polynomial(n-2, x)


# Gibt das n-te Hermitpolynom in Form eines Objekts bzw. Funktion zurück
def H_n(n):
    return partial(hermite, n)


# Wellenfunktion des harmon. Osz.
def psi(n, x):
    return 1/np.sqrt(np.power(2, n) * factorial(n) * np.sqrt(np.pi) ) * np.exp(- x*x/2 ) * hermite(n, x)


# Berechnet den Erwartungswert  <x*x> der Wellenfunktion. Das uneigentliche Integral kann durch 
# eine Substitution in ein Integral über ein endliches Intervall überführt werden. 
def uncertainty(n):


    # Integrand des Unbestimmten Integrals
    def f(x):
        return x*x*np.power(psi(n, x) , 2)


    # substituierter Integrand:
    def substitution(x):
        return f(np.tan(x))/np.cos(x)**2


    return integrate(substitution, -np.pi/2, np.pi/2)
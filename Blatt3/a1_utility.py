import numpy as np
import matplotlib.pyplot as plt

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
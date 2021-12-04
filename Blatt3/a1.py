import numpy as np
from scipy.special import j0, j1
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

x_axis = np.arange(0, r_max, r_max/100)
y_axis = np.empty(len(x_axis))

for m in [0, 1, 2]:
    for index, r in enumerate(x_axis):
        y_axis[index] = bessel_func(r, m)

    plt.plot(x_axis, y_axis, label='$J_' + str(m) + '$')
    
plt.plot(x_axis, j0(x_axis), '--' , label='$J_0$ ideal')
plt.plot(x_axis, j1(x_axis), '--' ,label='$J_1$ ideal')


plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from sympy import hermite


def hermite_polynomial(n,x):
    if not n:
        return 1.0
    elif n is 1:
        return 2 * x
    else:
        return 2*x*hermite_polynomial(n-1, x) - 2*(n-1)*hermite_polynomial(n-2, x)



def psi(n, x):
    return 1/np.sqrt(np.power(2, n) * factorial(n) * np.sqrt(np.pi) ) * np.exp(- x*x/2 ) * hermite(n, x)


for n in [0,1,2,3,4,5]:
    x_axis = np.arange(-10, 10, 0.1)
    y_axis = [hermite(n, x) for x in x_axis]
    plt.plot(x_axis, y_axis, label='n = ' + str(n))


plt.legend()
plt.show()




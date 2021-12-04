import numpy as np
from scipy.special import j0, j1
import matplotlib.pyplot as plt
import a1_utility as util



x_axis = np.arange(0, util.r_max, util.h)
y_axis = np.empty(len(x_axis))


for m in [0, 1, 2]:
    for index, r in enumerate(x_axis):
        y_axis[index] = util.bessel_func(r, m)

    plt.plot(x_axis, y_axis, label='$J_' + str(m) + '$')
    
plt.plot(x_axis, j0(x_axis), '--' , label='$J_0$ ideal')
plt.plot(x_axis, j1(x_axis), '--' ,label='$J_1$ ideal')


plt.legend()
plt.show()

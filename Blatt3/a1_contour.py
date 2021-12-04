from a1_utility import bessel_func
import numpy as np
import matplotlib.pyplot as plt

h = 0.01
r_max = 10
resolution = 1000
grid = np.empty([resolution, resolution])
wavelength = 1
k = 2 * np.pi / wavelength


def I(k, r):
    return (bessel_func(r, 1)/(k*r))**2



"""
for i in range(resolution):
    for j in range(resolution):
        r = np.sqrt((((i-resolution/2) * h)**2 + ((j-resolution/2) * h)**2))
        if r:
            grid[i][j] = I(k, r)
"""

x_range = np.arange(0, r_max, h)

plt.plot(x_range, I(k, x_range))
#plt.imshow(grid,  cmap='hot')
plt.gray()
plt.show()



from utility import bessel_func
import numpy as np
import matplotlib.pyplot as plt

# Berechnet das Beugungsbild und stellt es als Dichteplot dar.


r_max = 1
resolution = 80
h = 0.01
grid = np.empty([resolution, resolution])
wavelength = 1
k = 2 * np.pi / wavelength


# Berechnet Intensität I(r)
def I(k, r):
    if r==0:
        return 1/4  # Benutze analytischen Grenzwert bei r=0 um zero division zu umgehen
    else:
        return (bessel_func(k*r, 1)/(k*r))**2


# Berechnet Beugungsbild
for i in range(resolution):
    for j in range(resolution):
        r = np.sqrt(((i-resolution/2)/resolution*r_max )**2 + ((j-resolution/2)/resolution*r_max)**2)
        intensity = I(k, r)
        grid[i][j] = intensity


x_range = np.arange(0, r_max, h)
plt.imshow(grid,  cmap='hot')
plt.gray()
plt.show()


# Anmerkung: die Laufzeit wächst quadratisch mit der Auflösung des Plots. Weil das Beugungsbild 
# symmetrisch ist genügt eigentlich auch nur I(r) um den Ursprung zu ritieren in linearer Zeit. 


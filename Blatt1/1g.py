import numpy as np


vector = np.array([1,1,0])
zero_vec = np.array([0,0,0])

# Gibt einen normierten Vektor zurück. Falls Eingabe dem Nullvektor entspricht wird dieser Zurückgegeben. 
def norm_vector(vector):
	if not vector.any(0):
		print('Achtung Nullvektor')
		return vector
	norm = 0
	for v in vector:
		norm += v*v
	return vector/np.sqrt(norm)


print(zero_vec(vector))
print(norm_vector(vector))


import numpy as np


# Findet das Kreuzprodukt zweier (3 x 1)  Vektoren.
def cross_product(vector_1, vector_2):
	if vector_1.size != 3 or vector_2.size != 3:
		print('Falsche dimension')
		return 

	r_1 = vector_1[1]*vector_2[2]-vector_1[2]*vector_2[1]
	r_2 = vector_1[2]*vector_2[0]-vector_1[0]*vector_2[2]
	r_3 = vector_1[0]*vector_2[1]-vector_1[1]*vector_2[0]
	return np.array([ r_1, r_2, r_3])


vec_1 = np.array([1,2,3])
vec_2 = np.array([5,1,-2])


print(cross_product(vec_1, vec_2))
print(np.cross(vec_1, vec_2))

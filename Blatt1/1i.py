# 1. i.

import numpy as np

# Einige Beispielmatrizen
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,3,10],[4,5,6,-5],[7,8,-6,0],[1,1,3,1]])
C = np.array([[1,2],[3,4]])
I_4 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) # 4x4 Einheitsmatrix


# Gibt die Untermatrix an der 0 Zeile und j Spalte zurück
def minor(M, j):
    dim = M[0].size - 1 # Dimension der neuen Matrix
    new_Array = np.zeros((dim, dim))
    # Die Schleife geht über alle Einträge der Matrix außer der gestrichenen Zeile und Spalte
    for i in range(1, dim + 1):
        for k in range(j):
            new_Array[i-1][k] = M[i][k]
        for k in range(j+1, dim + 1):
            new_Array[i-1][k-1] = M[i][k]  
    return new_Array


# Findet die Determinante mit dem Laplacschen Entwicklungssatz einer n x n Matrix bzw. numpy array
def det(M):
    # gebe im Basis-Fall die Deteminante der 2x2 Matrix aus
    if M[0].size == 2:
        return M[0][0]*M[1][1] - M[1][0]*M[0][1]
    
    # Entwickle rekursiv nach der ersten Zeile
    determinante = 0
    for j in range(M[0].size):
        determinante += (-1)**j * M[0][j] * det(minor(M,j))

    return determinante

# Berechnet die Determinante einer NxN Matrix zufälliger Einträge
N = 7
print(det(np.random.random((N,N))))

# Fazit:
# Die Implementierung des  Laplace Algorithmus berechnet die Determinante einer 10x10 Matrix in etwa 33 Sekunden
# Die Lauzeit liegt in O(N!) und ist damit extrem indeffizient. 
#f

import string
import numpy as np
import matplotlib.pyplot as plt

f = open("beeMovie.txt", "r") # öffne zu untersuchende Datei

dict = dict.fromkeys(string.ascii_lowercase, 0) # erzeugt ein dictionary des ganzen Alphabets

line = f.readline()
while line:
    for s in line:
        if s.lower().isalpha(): # wenn Buchstabe gefunden, erhöhe Anzahl des Buchstaben im Dictionary
            dict[s.lower()] += 1
    line = f.readline()
f.close()   


# Stelle die Anzahlen mit der die einzelnen Buchstaben auftauchen in einem Histiogramm/BarChart dar
A = [i for i in dict.values()]
x = np.arange(0,26)
alphabet = [s for s in string.ascii_uppercase]
plt.bar(x, height=A)
plt.xticks(x, alphabet)
plt.show()
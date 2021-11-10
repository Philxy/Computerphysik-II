# g

from string import ascii_lowercase

input = open("beeMovie.txt", "r")       # input Datei
output = open("outputFile.txt", "w")    # output Datei

n = 4   # verschiebt Buchstaben um n

alphabet = [i for i in ascii_lowercase] 

# verschiebe zunächst die Elemente im Alphabet array um n
temp = [] 
for i in range(n):
    temp.append(alphabet.pop(0))
for t in temp:
    alphabet.append(t)


# Erzeuge ein Dict das einem Buchstaben den entsprechenden verschobenen Buchstaben zuordent

dict = dict.fromkeys(ascii_lowercase, '') # erzeugt ein dictionary des ganzen Alphabets
i = 0
for A in [j for j in ascii_lowercase]:
    dict[A] = alphabet[i]
    i += 1

# Lese Dateien ein und schreibe verschobene Buchstaben darin hinein 
line = input.readline()
while line:
    newLine = '' 
    for s in line:
        if s.lower().isalpha():
            newLine += dict[s.lower()]
        else:
            newLine += s
    line = input.readline()
    output.write(newLine)
input.close()   
output.close()

# t.b.c.
#encrypted = open('outputFile.txt' , 'r')
#decrypted = open('decrypted.txt', 'w')
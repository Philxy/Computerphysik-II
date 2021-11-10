#d

# i.

# gibt rekursiv das n-Glied der Fibonacci Folge zurück
def recursive_fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return recursive_fib(n-1) + recursive_fib(n-2)

# gibt iterativ das n-Glied der Fibonacci Folge zurück
def iterative_fib(n):
    j, m = 0, 1
    for i in range(0,n):
        j, m = m, j + m
    return j


# ii.

# Der rekursive Output zeigt, dass mindestens die ersten 28 Folgenglieder übereinstimmen.
# Jenseits davon wird die Rechendauer zu groß.

# Die untere iterative Implementierung überprüft die Übereinstimmung der ersten n
# Gleider. Bis n = 400 stimmen die Glieder in angemessener Zeit überein.
n = 400
for i in range(n):
    sum = 0
    for j in range(i+1):
        sum += iterative_fib(j)**2

    if sum != iterative_fib(i)*iterative_fib(i+1):
        print('Die Gleichung versagt ab dem' + str(n) + ' Glied')
        break
    
# iii.
N = 600
print('Der Grenzwert lautet in angemessener Laufzeit :', iterative_fib(N+1)/iterative_fib(N))

# iv.
depth = 1000
def func(n):
    if (n == 0):
        return 1
    return 1 + 1 / func(n-1)
print(func(depth))

# ==> Der Vergleich der beiden Grenzwerte liefert für die ersten 14 Nachkommastellen eine Übereinstimmung 

#a

def iterative_fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def recursive_fac(n):
    if n == 1  or n == 0:
        return 1
    return recursive_fac(n-1)*n


# Der rekursiven Implementierung geht der Speicher schnell aus. 
# Iterativ kann die Eingabe um Größenordungen größer sein. 

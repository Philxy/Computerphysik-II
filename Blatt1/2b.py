#b

# Gibt das Pascalsche Dreieck bis zur Tiefe n aus.
def pascal(n):
    result = []
    if n == 1:
        result.append(['1'])
    if n >= 2:
        result.append(['1'])
        result.append(['1', '1'])
        
    previous = [1,1]
    new = []
    
    # Erzeuge Array mit Einträgen des Dreiecks
    for i in range(n):
        new.append(1)
        for j in range(len(previous)-1):
            new.append(previous[j]+previous[j+1])
        new.append(1)
        previous = new
        result.append(list(map(str, new)))
        new = []
    
    size = len(max(result[-1], key=len)) # Anzahl Ziffern der größten Zahl 
    
    # print PascalDreieck
    for i in range(n):
        result_as_strings = map(str, result[i])
        s = ''
        for a in result_as_strings:
            s += a.center(size+1, ' ') 
        print(s.center(n*size+n, ' '))
        s = ''

pascal(14)
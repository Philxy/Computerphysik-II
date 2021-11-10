#c
import itertools as iter


# permutations(): findet alle möglichen Permutationen von einem iterable.

    # z.B. alle Permutationen der Bruchstaben A,B,C,D 
for s in iter.permutations('ABCD'):
    print(s)
   
    # z.B. alle Permutationen der Bruchstaben A,B,C,D in 3-er Tupeln. Damit kann 
    # also auch die Anzahl spezifiziert werden.
for s in iter.permutations('ABCD', 3):
    print(s)

    # z.B. alle Permutationen von 0,1,2 in Zweiertupeln
for i in iter.permutations(range(3), 2):
    print(i)


# combinations(): findet alle sortierten  Anordnungsmöglichkeiten von einem iterable. 
#   Unterscheidet sich von permutations(), da sortiert wird und mehrfach auftauchende
#   elemente ausgeschlossen werden

    # z.B. alle sortierten 2er Tupel der Zahlen von 0 bis einschließlich 2:
for i in iter.combinations(range(3), 2):
    print(i)

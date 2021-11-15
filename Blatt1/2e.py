
# Ich habe 'maximal' in der Aufgabenstellung durch minimal ersetzt. Für die maximale Zahl
# würde man natürlich immer 1ct nehmen;


# Der folgende Code findet die minimale Anzahl an Münzen um einen gewissen Betrag aus dem 
# gegebenen Satz an Münzen zu bilden. Bei den Münzen 50,20,10,5,2,1 funktioniert
# der Greedy-Algorithmus. Im Allgemeinen ist das aber nicht der Fall! Für einen beliebigen 
# Satz an Münzen kann das Problem effizient mit dynamischer Programmierung gelöst werden. 

from itertools import combinations


coins = [50,20,10,5,2,1]
minimal_number_of_coins = []

for value in range(1, 100):
	result = []
	current_sum = 0
	for coin in coins:
		if current_sum == value:
			break
		while current_sum + coin <= value:
			result.append(coin)
			current_sum += coin		
	minimal_number_of_coins.append(result)


for i in range(1, len(minimal_number_of_coins)+1):
	print('Man bracht minimal', len(minimal_number_of_coins[i-1]), 'Münzen um', i ,'ct zu bilden.' )

#----------------------------------------------------------------------------------------------------

coins = [1,2,5,10,20,50]

# Die Anzahl an Möglichkeiten ( anzahl_moeglichkeiten(N,k) ), um einen Betrag N zu bilden mit den ersten k Münzen ist die Anzahl
# an Möglichkeiten ohne die k-te Münze zu benutzen plus die Anzahl an Möglichkeiten  
# sie benutzen ( anzahl_moeglichkeiten(N - (k te Münze), k) ).
# Irgendwie ist es schwer die Rekursionsvorschrift in Worten zu beschreiben^^

# Die folgende rekursive Funktion findet die Anzahl der Möglichkeiten, um aus den ersten 
# 'k' Münzen des Münzsatzes (1,2,5,10,20,50) den Betrag 'N' zu bilden. 
def anzahl_moeglichkeiten(N, k):
	if N < 0 or k < 1:  # Keine Möglichkeiten für negative
		return 0
	elif N == 0 :		 # Eine Möglichkeit im Standardfall
		return 1
	else:
		return anzahl_moeglichkeiten(N, k-1) + anzahl_moeglichkeiten(N-coins[k-1], k)


for i in range(100):
	print('Der Betrag', i, 'kann mit', anzahl_moeglichkeiten(i, len(coins)), 'Möglichkeiten erzeugt werden.')


	

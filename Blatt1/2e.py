
# Der folgende Code findet die minimale Anzahl an Münzen um einen gewissen Betrag aus dem 
# gegebenen Satz an Münzen zu bilden. Bei den Münzen 50,20,10,5,2,1 funktioniert
# der Greedy-Algorithmus. Im Allgemeinen ist das aber nicht der Fall! Für einen beliebigen 
# Satz an Münzen kann das Problem effizient mit dynamischer Programmierung gelöst werden. 

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
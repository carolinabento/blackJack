import random

'''
Dictionary structure with the initial values for each card in the 52-card deck.

Since the player can choose the value of the ace to be 1 or 11,
the value of the ace is set to 1, by default.
'''
deck = {}


'''
Dictionary structure with the cards that were already played
'''
deckOut = {}







'''
Method to create a new card deck
'''

def newDeck():
	global deck

	deck = {"ace": [1,1,1,1],
			"two": [2,2,2,2],
			"three": [3,3,3,3],
			"four": [4,4,4,4],
			"five": [5,5,5,5],
			"six": [6,6,6,6],
			"seven": [7,7,7,7],
			"eight": [8,8,8,8],
			"nine": [9,9,9,9],
			"ten": [10,10,10,10],
			"jack": [10,10,10,10],
			"queen": [10,10,10,10],
			"king": [10,10,10,10]}


'''
Method to clear the deckOut
'''
def emptyDeckOut():
	global deckOut

	deckOut = {}



'''
Method to add the last card that was picked, to the deckOut structure
'''
def addToDeckOut(card,value):
	global deckOut

	if card not in deckOut.keys():
		items = []
		items.append(value)
		deckOut[card] = items
	else:
		deckOut[card].append(value)


'''
Method to pick a card at random from the cards that are available.
'''
def pickCard():
	global deck
	global deckOut

	card = random.sample(deck.keys(),1)[0]
	value = deck[card][0]

	if len(deck[card]) > 0:
		deck[card].remove(value)
		addToDeckOut(card,value)

		if len(deck[card]) == 0:
			del deck[card]
	else:
		del deck[card]
		card = random.sample(deck.keys(),1)[0]
		value = deck[card][0]
		addToDeckOut(card,value)

	return value
import random

class Deck:
	
	def __init__(self):
		'''
		Constructor of the deck class
		'''
		

		'''
		Dictionary structure with the initial values for each card in the 52-card deck.

		Since the player can choose the value of the ace to be 1 or 11,
		the value of the ace is set to 1, by default.
		'''
		self.deck = {}

		'''
		Dictionary structure with the cards that were already played in the game
		'''
		self.deckOut = {}

		self.deck = {"ace": [1,1,1,1],
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


		
	def emptyDeckOut(self):
		'''
		Method to clear the deckOut
		'''
		self.deckOut = {}



	def __addToDeckOut(self,card,value):
		'''
		Method to add the last card that was picked, to the deckOut structure
		'''
		if card not in self.deckOut.keys():
			items = []
			items.append(value)
			self.deckOut[card] = items
		else:
			self.deckOut[card].append(value)


	def pickCard(self):
		'''
		Method to pick a card at random from the cards that are available.
		'''
		card = random.sample(self.deck.keys(),1)[0]
		value = self.deck[card][0]

		if len(self.deck[card]) > 0:
			self.deck[card].remove(value)
			self.__addToDeckOut(card,value)

			if len(self.deck[card]) == 0:
				del self.deck[card]
		else:
			del self.deck[card]
			card = random.sample(self.deck.keys(),1)[0]
			value = self.deck[card][0]
			self.__addToDeckOut(card,value)

		return value
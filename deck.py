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

		'''
		Dictionary structure with the cards that were already played in the game
		'''
		self.playedCards = {}


		
	def emptyPlayedCards(self):
		'''
		Clears the playedCards structure
		'''
		self.playedCards = {}


	def pickCard(self):
		'''
		Picks a card at random from the cards that are available.
		'''
		card = random.choice(self.deck.keys())
		value = self.deck[card][0]

		if len(self.deck[card]) > 0:
			self.deck[card].remove(value)
			self.__addToPlayedCards(card,value)

			if len(self.deck[card]) == 0:
				del self.deck[card]
		else:
			del self.deck[card]
			card = random.choice(self.deck.keys())
			value = self.deck[card][0]
			self.__addToPlayedCards(card,value)

		return value

	def __addToPlayedCards(self,card,value):
		'''
		Adds the last card that was picked, to the playedCards structure
		'''
		if card not in self.playedCards.keys():
			items = []
			items.append(value)
			self.playedCards[card] = items
		else:
			self.playedCards[card].append(value)
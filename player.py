import random
from deck import Deck

class Player:

	def __init__(self):
		#keep the player's deck
		self.deck = []
		#keep the player's score (i.e., the total value of the cards in hand)
		self.hand = 0
		#keep the player's chips, with initial value of 100
		self.chips = 100

	
	def updateDeck(self,cardList):
		'''
		Update the player's deck
		'''

		for card in cardList:
			self.deck.append(card)


	def updateChips(self,winner,bet):
		'''
		Update the player's chips count
		'''

		if winner == 1:
			self.chips += bet*2
		elif winner == 2:
			self.chips += bet*1.5
		elif winner == 3:
			self.chips -= bet


	def makeMove(self,Deck):
		'''
		The player's possible moves
		The player choose which value the ace (card = 1) will be, given his current hand
		'''
		card = Deck.pickCard();

		print("\tThe card picked: " + str(card))

		if card == 1 and (self.hand + 11)  >= 21:
			self.hand += 1
		elif card == 1 and (self.hand + 11)  < 21:
			self.hand += 11
			card = 11
		elif (self.hand + card) > 21 and 11 in self.deck:
			self.deck.remove(11)
			self.deck.append(1)
			self.hand += card
		else:
			self.hand += card

		playerCards = []
		playerCards.append(card)
		
		self.updateDeck(playerCards)

		return self.hand
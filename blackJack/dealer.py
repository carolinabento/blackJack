from player import Player
from deck import Deck

class Dealer:
	"""
	The Dealer class represents the house dealer
	"""


	def __init__(self):
		#keep the dealer's deck
		self.deck = []
		#keep the dealer's score (i.e., the total value of the cards in hand)
		self.hand = 0
		
		#keep the dealer's number of cards, in order to decide if we only show the dealer's up card or the dealer's deck
		self.numberCards = 0
		#keep the dealer's up card
		self.upCard = 0


	def dealCards(self,player,deck):
		"""
		Deals the cards, to start the game
		For the 1st hand, gives the player and the dealer two cards

		:param player: Player class
		:type player: :class:'blackjack.player' class instance
		:param deck: Deck class
		:type deck: :class:'blackjack.deck' class instance

		"""

		card1 = deck.pickCard() 
		card2 = deck.pickCard() 
		card3 = deck.pickCard() 
		card4 = deck.pickCard()

		print("\tThe card picked: " + str(card1))
		print("\tThe card picked: " + str(card3))
		print("\tThe card picked: " + str(card4))

		player.hand = card1 + card3
		self.hand = card2 + card4

		self.upCard = card4

		playerCards = []
		playerCards.append(card1)
		playerCards.append(card3)
		player.updateDeck(playerCards)


		dealerCards = []
		dealerCards.append(card2)
		dealerCards.append(card4)

		self.__updateDeck(dealerCards)

		print("Player: The dealer's up card is " + str(self.upCard) + ".")

		self.numberCards = 2
		player.chips = player.chips


	
	def makeMove(self,deck,playerHand):
		"""
		The dealer's possible moves

		:param deck: Deck class
		:type deck: :class:'blackjack.deck' class instance

		:param playerHand: Player's current hand
		:type playerHand: int

		:rtype: int
		"""

		card = 0

		while self.hand < 17 or (self.hand >= 17 and playerHand > self.hand):
			print("Dealer's hand is " + str(self.hand) + ". Dealer's deck is " + str(self.deck) + "\nDealer hits.")
			card = deck.pickCard()

			print("\tThe card picked: " + str(card))

			self.__chooseCardValue(card)

			dealerCards = []
			dealerCards.append(card)

			self.__updateDeck(dealerCards)
		

		self.numberCards += self.numberCards

		if self.numberCards == 2:
			self.upCard = card

			print("Player: The dealer's up card is " + str(self.upCard))
		else:
			print("Dealer's hand is " + str(self.hand) + ". Dealer's deck is " + str(self.deck))

		return self.hand


	def __updateDeck(self,cardList):
		"""
		Updates the dealer's deck

		:param cardList: List of cards to add to the dealer's deck
		:type cardList: list
		"""

		for card in cardList:
			self.deck.append(card)


	def __chooseCardValue(self,card):
		"""
		Chooses the value of the picked card, according to the dealer's
		current hand. If he picks an ace (card = 1), he can choose its value
		to be either 1 or 11.

		:param card: Value of the picked card
		:type card: int
		"""	

		if card == 1 and (self.hand + 11)  >= 21:
			self.hand += 1
		elif card == 1 and (self.hand + 11) < 21:
			self.hand += 11
			card = 11
		elif (self.hand + card) > 21 and 11 in self.deck:
			self.deck.remove(11)
			self.deck.append(1)
			self.hand += card
		else:
			self.hand += card
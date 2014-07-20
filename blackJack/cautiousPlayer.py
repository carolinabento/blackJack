from player import Player

class CautiousPlayer(Player):
	"""
	The cautiousPlayer class represents a cautious BlackJack player: he always analyzes the probability
	of picking a card that wont make him bust.
	If he has a chance equal of greater than 0.60 to pick a card that will not make him bust,
	he hits, otherwise he stands. 
	"""


	def __init__(self):
		Player.__init__(self)
		self.threshold = 0.60



	def makeCautiousMove(self,deck):
		"""
		The cautious player's possible moves

		:param deck: Deck class
		:type deck: :class:'blackjack.deck' class instance

		:rtype: int 
		"""

		cautiousMove = self.__chooseMove(deck)

		while cautiousMove == "h":
			print("Player hits.")
			self.makeMove(deck)
			print("Player: Your deck is " + str(self.deck) + ". Your current hand is " +  str(self.hand) + ".")
			cautiousMove = self.__chooseMove(deck)

		return self.hand


	def __nonBustCards(self,deck):
		"""
		Checks in the deck for the cards which would not make the player bust
		if they were picked in the next move

		:param deck: Deck class
		:type deck: :class:'blackjack.deck' class instance

		:rtype: list 
		"""

		result = []

		for key in deck.deck.keys():
			if self.hand + deck.deck[key][0] <= 21:
				result.append(key)

		return result


	def __chooseMove(self,deck):
		'''
		Analyzes the chances the player has of picking a card that will not
		make him bust. If this probability is >= 0.6 the player hits, otherwise he stands.
		The cautious player always bets 1/2 of his total chips.

		:param deck: Deck class
		:type deck: :class:'blackjack.deck' class instance

		:rtype: string
		'''

		probabilityNonBust = 0.0
		nBustCards = self.__nonBustCards(deck)
		cardsLeft = deck.numbCardsLeft()

		for card in nBustCards:
			probabilityNonBust += float(len(deck.deck[card]))/cardsLeft


		if round(probabilityNonBust,3) >= self.threshold:
			return "h"
		else:
			return "s"
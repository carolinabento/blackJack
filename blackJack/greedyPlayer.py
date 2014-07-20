from player import Player


class GreedyPlayer(Player):
	"""
	The greedyPlayer class represents a greedy BlackJack player: he always bets half of his current chips,
	and always hits until his hand is greater or equal to 15.
	"""

	def __init__(self):
		Player.__init__(self)
		self.threshold = 15


	def makeGreedyMove(self,deck):
		"""
		The greedy player's possible moves

		:param deck: Deck class
		:type deck: :class:'blackjack.deck' class instance

		:rtype: int
		"""
		while self.hand <= self.threshold:
			print("Player hits.")
			self.makeMove(deck)
			print("Player: Your deck is " + str(self.deck) + ". Your current hand is " +  str(self.hand) + ".")

		return self.hand
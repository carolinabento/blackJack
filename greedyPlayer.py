from player import Player

'''
The greedyPlayer class represents a greedy BlackJack player: he always bets half of his current chips,
and always hits until his hand is greater or equal to 15.
'''
class GreedyPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.threshold = 15


	def makeGreedyMove(self,Deck):
		'''
		The greedy player's possible moves
		'''
		while self.hand <= self.threshold:
			print("Player: Hits.")
			self.makeMove(Deck)
			print("Player: Your deck is " + str(self.deck) + ". Your current hand is " +  str(self.hand) + ".")
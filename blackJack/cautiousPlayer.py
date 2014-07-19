from player import Player

'''
The cautiousPlayer class represents a cautious BlackJack player: he always analyzes the probability
of picking a card that wont make him bust.
If he has a chance equal of greater than 0.60 to pick a card that will not make him bust,
he hits, otherwise he stands. 
'''
class CautiousPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.threshold = 0.60


	def makeCautiousMove(self,Deck):
		'''
		The cautious player's possible moves
		'''

		cautiousMove = self.__chooseMove(Deck)

		while cautiousMove == "h":
			print("Player hits.")
			self.makeMove(Deck)
			print("Player: Your deck is " + str(self.deck) + ". Your current hand is " +  str(self.hand) + ".")
			cautiousMove = self.__chooseMove(Deck)

		return self.hand


	def __nonBustCards(self,Deck):
		'''
		Returns the list of cards which would not make the player bust
		if they were picked in the next move
		'''

		result = []

		for key in Deck.deck.keys():
			if self.hand + Deck.deck[key][0] <= 21:
				result.append(key)

		return result


	def __chooseMove(self,Deck):
		'''
		Analyzes the chances the player has of picking a card that will not
		make him bust. If this probability is >= 0.6 the player hits, otherwise he stands.
		The cautious player always bets 1/2 of his total chips.
		'''

		probabilityNonBust = 0.0
		nBustCards = self.__nonBustCards(Deck)
		cardsLeft = Deck.numbCardsLeft()

		for card in nBustCards:
			probabilityNonBust += float(len(Deck.deck[card]))/cardsLeft


		if round(probabilityNonBust,3) >= self.threshold:
			return "h"
		else:
			return "s"
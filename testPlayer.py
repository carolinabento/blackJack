from deck import Deck
from dealer import Dealer
from player import Player

class TestPlayer:

	def __init__(self):
		return


	'''
	Testing correct access to the player constructor
	'''
	@staticmethod
	def testConstructor():

		player = Player()

		assert player.deck == []
		assert player.hand == 0
		assert player.chips == 100

	'''
	Testing method updateChips
	'''
	@staticmethod
	def testUpdateChips():

		player = Player()
		assert player.chips == 100

		#player won
		player.updateChips(1,10)
		assert player.chips == 120



	'''
	Testing method makeMove
	'''
	@staticmethod
	def testMakeMove():
		deck = Deck()
		dealer = Dealer()
		player = Player()

		assert deck.deck["ace"][1] == 1
		assert deck.deck["two"][1] == 2
		assert deck.deck["king"][1] == 10
		assert deck.deckOut == {}


		assert dealer.deck == []
		assert dealer.hand == 0
		assert dealer.numberCards == 0
		assert dealer.upCard == 0

		dealer.dealCards(player,deck)

		assert deck.deckOut != {}
		assert len(deck.deckOut.values()) != 0
		assert len(deck.deck.values()) != 52	

		assert dealer.numberCards == 2
		assert dealer.hand != 0
		assert len(dealer.deck) == 2

		player.makeMove(deck)

		assert deck.deckOut != {}
		assert len(deck.deckOut.values()) != 0
		assert len(deck.deck.values()) != 52
		
		assert len(player.deck) == 3


	@staticmethod
	def main():
		TestPlayer.testConstructor()
		TestPlayer.testMakeMove()
		


TestPlayer.main()

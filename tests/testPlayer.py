from deck import Deck
from dealer import Dealer
from player import Player

class TestPlayer:

	def __init__(self):
		return

	@staticmethod
	def testConstructor():
		#Testing correct access to the player constructor

		player = Player()

		assert player.deck == []
		assert player.hand == 0
		assert player.chips == 100

	@staticmethod
	def testUpdateChips():
		#Testing method updateChips

		player = Player()
		assert player.chips == 100

		#player won
		player.updateChips(1,10)
		assert player.chips == 120


	@staticmethod
	def testMakeMove():
		#Testing method makeMove
		
		deck = Deck()
		dealer = Dealer()
		player = Player()

		assert deck.deck["ace"][1] == 1
		assert deck.deck["two"][1] == 2
		assert deck.deck["king"][1] == 10
		assert deck.playedCards == {}


		assert dealer.deck == []
		assert dealer.hand == 0
		assert dealer.numberCards == 0
		assert dealer.upCard == 0

		dealer.dealCards(player,deck)

		assert deck.playedCards != {}
		assert len(deck.playedCards.values()) != 0
		assert len(deck.deck.values()) != 52	

		assert dealer.numberCards == 2
		assert dealer.hand != 0
		assert len(dealer.deck) == 2

		player.makeMove(deck)

		assert deck.playedCards != {}
		assert len(deck.playedCards.values()) != 0
		assert len(deck.deck.values()) != 52
		
		assert len(player.deck) == 3


	@staticmethod
	def main():
		#Run the test suite

		TestPlayer.testConstructor()
		TestPlayer.testMakeMove()
		


TestPlayer.main()

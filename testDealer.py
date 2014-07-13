from deck import Deck
from dealer import Dealer
from player import Player

class TestDealer:

	def __init__(self):
		return

	'''
	Testing correct access to the dealer constructor
	'''
	@staticmethod
	def testConstructor():

		dealer = Dealer()

		assert dealer.deck == []
		assert dealer.hand == 0
		assert dealer.numberCards == 0
		assert dealer.upCard == 0


	'''
	Testing method dealCards
	'''
	@staticmethod
	def testDealCards():
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

		assert player.deck == []
		assert player.hand == 0
		assert player.chips == 100


		dealer.dealCards(player,deck)

		assert deck.deckOut != {}
		assert len(deck.deckOut.values()) != 0
		assert len(deck.deck.values()) != 52	

		assert dealer.numberCards == 2
		assert dealer.hand != 0
		assert len(dealer.deck) == 2

		assert dealer.hand != 0
		assert len(player.deck) == 2

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

		dealer.makeMove(deck)

		assert deck.deckOut != {}
		assert len(deck.deckOut.values()) != 0
		assert len(deck.deck.values()) != 52

		assert dealer.numberCards >= 2
		assert dealer.hand != 0
		assert len(dealer.deck) >= 2




	@staticmethod
	def main():
		TestDealer.testConstructor()
		TestDealer.testDealCards()
		TestDealer.testMakeMove()


TestDealer.main()
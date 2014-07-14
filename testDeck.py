from deck import Deck

class TestDeck:

	def __init__(self):
		return

	
	@staticmethod
	def testConstructor():
		#Testing correct access to the deck constructor

		deck = Deck()

		assert deck.deck["ace"][1] == 1
		assert deck.deck["two"][1] == 2
		assert deck.deck["king"][1] == 10
		assert deck.playedCards == {}

	@staticmethod
	def testEmptyPlayedCards():
		#Testing the method emptyPlayedCards

		deck = Deck()

		assert deck.deck["ace"][1] == 1
		assert deck.deck["two"][1] == 2
		assert deck.deck["king"][1] == 10
		assert deck.playedCards == {}

		deck.playedCards["three"] = [3]
		deck.playedCards["five"] = [5]

		assert len(deck.playedCards) == 2
		assert deck.playedCards["three"] == [3]
		
		deck.emptyPlayedCards()

		assert deck.playedCards == {}
		assert len(deck.playedCards) == 0

	@staticmethod
	def testPickCard():
		#Testing method pickCard
		
		deck = Deck()

		for index in range(0, 52):
			assert deck.deck != {}
			deck.pickCard()
			assert len(deck.playedCards.keys()) >= 1

		assert deck.deck == {}
		assert len(deck.playedCards.keys()) == 13


	@staticmethod
	def main():
		#Run the test suite

		TestDeck.testConstructor()
		TestDeck.testEmptyPlayedCards()
		TestDeck.testPickCard()



TestDeck.main()



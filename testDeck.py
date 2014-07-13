from deck import Deck

class TestDeck:

	def __init__(self):
		return

	'''
	Testing correct access to the deck constructor
	'''
	@staticmethod
	def testConstructor():
		

		deck = Deck()

		assert deck.deck["ace"][1] == 1
		assert deck.deck["two"][1] == 2
		assert deck.deck["king"][1] == 10
		assert deck.deckOut == {}

	'''
	Testing the method emptyDeckOut
	'''
	@staticmethod
	def testEmptyDeckOut():

		deck = Deck()

		assert deck.deck["ace"][1] == 1
		assert deck.deck["two"][1] == 2
		assert deck.deck["king"][1] == 10
		assert deck.deckOut == {}

		deck.deckOut["three"] = [3]
		deck.deckOut["five"] = [5]

		assert len(deck.deckOut) == 2
		assert deck.deckOut["three"] == [3]
		
		deck.emptyDeckOut()

		assert deck.deckOut == {}
		assert len(deck.deckOut) == 0

	'''
	Testing method pickCard
	'''
	@staticmethod
	def testPickCard():
		
		deck = Deck()

		for index in range(0, 52):
			assert deck.deck != {}
			deck.pickCard()
			assert len(deck.deckOut.keys()) >= 1

		assert deck.deck == {}
		assert len(deck.deckOut.keys()) == 13


	@staticmethod
	def main():

		TestDeck.testConstructor()
		TestDeck.testEmptyDeckOut()
		TestDeck.testPickCard()



TestDeck.main()



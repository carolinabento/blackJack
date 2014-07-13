import deck as d

'''
Testing correct access to the deck structure
'''
def testDeck():
	global deck

	assert d.deck == {}
	assert d.deckOut == {}

	d.newDeck()

	assert d.deck["ace"][1] == 1
	assert d.deck["two"][1] == 2
	assert d.deck["king"][1] == 10


'''
Testing picking a card at random.
'''
def testPickCard():
	
	for index in range(0, 52):
		assert d.deck != {}
		d.pickCard()
		assert len(d.deckOut.keys()) >= 1

	assert d.deck == {}
	assert len(d.deckOut.keys()) == 13


'''
Testing initializing a new game
using the individual methods newDeck() and emptyDeckOut()
'''

def testInit():

	d.newDeck()

	assert len(d.deck.keys()) == 13

	d.pickCard()
	d.pickCard()

	assert len(d.deckOut.keys()) >= 1

	# a deck without 2 cards
	oldDeck = d.deck

	d.emptyDeckOut()

	assert d.deckOut == {}

	# a new full deck
	d.newDeck()
	newDeck = d.deck

	assert newDeck != oldDeck

	

testDeck()
testPickCard()
testInit()
import deck as deck
import player as player
import dealer as dealer
import blackJack as bj

'''
Testing initializing a new game
using the method initGame()
'''

def testInitGame():

	bj.initGame()

	assert dealer.numberCards == 0
	assert dealer.dealerHand == 0
	assert player.playerHand == 0

	assert len(deck.deck.keys()) == 13

	deck.pickCard()
	deck.pickCard()

	assert deck.deckOut != {}
	assert len(deck.deckOut.keys()) >= 1

	# a deck without 2 cards
	oldDeck = deck.deck


	bj.initGame()

	assert deck.deckOut == {}

	# the new, full deck
	newDeck = deck.deck

	assert newDeck != oldDeck

	assert dealer.numberCards == 0
	assert dealer.dealerHand == 0
	assert player.playerHand == 0





testInitGame()
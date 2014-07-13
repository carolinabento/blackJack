import random
import deck as d

#keep the player's deck
deck = []

#keep the player's score (i.e., the total value of the cards in hand)
hand = 0;

#keep the player's chips, with initial value of 100
chips = 100;

'''
Method to update the player's deck
'''
def updateDeck(cardList):
	global deck

	for card in cardList:
		deck.append(card)

	#return deck

'''
Method to update the player's chips count
'''
def updateChips(winner,bet):
	global chips

	if winner == 1:
		chips += bet
	else:
		chips -= bet



'''
Simulate the player's possible moves
'''
def makeMove():
	global hand

	card = d.pickCard();
	

	#print("card " + str(card))

	'''
	The player choose which value the ace (card = 1) will be,
	given his current hand
	'''
	if card == 1 and (hand + 11)  >= 21:
		hand += 1
	elif card == 1 and (hand + 11)  < 21:
		hand += 11
		card = 11
	elif (hand + card) > 21 and 11 in deck:
		deck.remove(11)
		deck.append(1)
		hand += card
	else:
		hand += card

	playerCards = []
	playerCards.append(card)
	
	updateDeck(playerCards)

	return hand
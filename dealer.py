import deck as d
import player

#keep the dealer's deck
deck = []

#keep the dealer's score (i.e., the total value of the cards in hand)
hand = 0

'''
keep the dealer's number of cards, in order to decide if we only show
the dealer's up card or the dealer's deck
'''
numberCards = 0

#keep the dealer's up card
upCard = 0


'''
Method to update the dealer's deck
'''
def updateDeck(cardList):
	global deck

	for card in cardList:
		deck.append(card)

	return deck



'''
Method to deal the cards at the beginning of the game
For the 1st hand, gives the player and the dealer two cards
'''
def dealCards():
	global hand
	global numberCards
	global upCard

	card1 = d.pickCard() 
	card2 = d.pickCard() 
	card3 = d.pickCard() 
	card4 = d.pickCard()

	player.hand = card1 + card3
	hand = card2 + card4

	upCard = card4

	playerCards = []
	playerCards.append(card1)
	playerCards.append(card3)
	player.updateDeck(playerCards)


	dealerCards = []
	dealerCards.append(card2)
	dealerCards.append(card4)

	updateDeck(dealerCards)

	print("Player: The dealer's up card is " + str(upCard))

	numberCards = 2
	player.chips = player.chips






'''
Simulate the dealer's possible moves
'''
def makeMove():
	global hand
	global deck
	global numberCards

	card = 0

	while hand < 17:
		print("Dealer's hand is " + str(hand) + ". Dealer's deck is " + str(deck) + "\nDealer hits.")
		card = d.pickCard()

		'''
		The player choose which value the ace (card = 1) will be,
		given his current hand
		'''
		if card == 1 and (hand + 11)  > 21:
			hand += card
		elif card == 1 and (hand + 11) < 21:
			card = 11
			hand += card
		elif (hand + card) > 21 and 11 in deck:
			hand.remove(11)
			hand.append(1)
			hand += card
		else:
			hand += card

		dealerCards = []
		dealerCards.append(card)

		updateDeck(dealerCards)
	
	if hand > 21:
		return

	numberCards += numberCards

	if numberCards == 2:
		upCard = card

		print("Player: The dealer's up card is " + str(upCard))
	else:
		print("Dealer's hand is " + str(hand) + ". Dealer's deck is " + str(deck))

	return hand
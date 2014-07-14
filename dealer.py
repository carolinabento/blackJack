from player import Player

class Dealer:

	def __init__(self):
		#keep the dealer's deck
		self.deck = []
		#keep the dealer's score (i.e., the total value of the cards in hand)
		self.hand = 0
		
		#keep the dealer's number of cards, in order to decide if we only show the dealer's up card or the dealer's deck
		self.numberCards = 0
		#keep the dealer's up card
		self.upCard = 0


	def dealCards(self,Player,Deck):
		'''
		Deals the cards, to start the game
		For the 1st hand, gives the player and the dealer two cards
		'''

		card1 = Deck.pickCard() 
		card2 = Deck.pickCard() 
		card3 = Deck.pickCard() 
		card4 = Deck.pickCard()

		print("\tThe card picked: " + str(card1))
		print("\tThe card picked: " + str(card3))
		print("\tThe card picked: " + str(card4))

		Player.hand = card1 + card3
		self.hand = card2 + card4

		self.upCard = card4

		playerCards = []
		playerCards.append(card1)
		playerCards.append(card3)
		Player.updateDeck(playerCards)


		dealerCards = []
		dealerCards.append(card2)
		dealerCards.append(card4)

		self.__updateDeck(dealerCards)

		print("Player: The dealer's up card is " + str(self.upCard))

		self.numberCards = 2
		Player.chips = Player.chips


	
	def makeMove(self,Deck):
		'''
		The dealer's possible moves
		'''

		card = 0

		while self.hand < 17:
			print("Dealer's hand is " + str(self.hand) + ". Dealer's deck is " + str(self.deck) + "\nDealer hits.")
			card = Deck.pickCard()

			print("\tThe card picked: " + str(card))

			'''
			The dealer chooses which value the ace (card = 1) will be,
			given his current hand
			'''
			if card == 1 and (self.hand + 11)  > 21:
				self.hand += card
			elif card == 1 and (self.hand + 11) < 21:
				card = 11
				self.hand += card
			elif (self.hand + card) > 21 and 11 in self.deck:
				self.hand.remove(11)
				self.hand.append(1)
				self.hand += card
			else:
				self.hand += card

			dealerCards = []
			dealerCards.append(card)

			self.__updateDeck(dealerCards)
		
		if self.hand > 21:
			return

		self.numberCards += self.numberCards

		if self.numberCards == 2:
			self.upCard = card

			print("Player: The dealer's up card is " + str(self.upCard))
		else:
			print("Dealer's hand is " + str(self.hand) + ". Dealer's deck is " + str(self.deck))

		return self.hand
	
	def __updateDeck(self,cardList):
		'''
		Updates the dealer's deck
		'''

		for card in cardList:
			self.deck.append(card)
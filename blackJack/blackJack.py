from deck import Deck
from dealer import Dealer
from player import Player



class BlackJack:
	"""
	The BlackJack class represents the BlackJack table: it has a dealer,and a deck and a player
	"""
	
	def __init__(self,player):
		"""
		Constructor of the BlackJack class, initializing the deck, the dealer's number of cards,
		and both the player and the dealer's hands and decks.

		:param player: Player class
		:type player: :class:'blackjack.player' class instance
		"""

		#keep the number of moves in the game
		self.moves = 0
		#keep the bet the player made for the game
		self.bet = 0

		#keep the possible user moves 
		self.possibleMoves = ["h","hit","s","stand","d","doubledown","double down"]

		#keep the keywords that indicate that the user wants to quit
		self.exitMoves = ["q","quit","n","no","exit"]

		#keep the move the player chose: h - hit, s - stand, d - doubleDown
		self.action = ""

		self.deck = Deck()
		self.deck.emptyPlayedCards()

		self.dealer = Dealer()

		self.player = player
		self.player.hand = 0		
		self.player.deck = []

	
	def placeBet(self,mode):
		'''
		Place the player's bet
		
		:param int mode: game mode (1: input mode, 2: bot mode (with the greedy/cautious player), 3: double down)
		:rtype: int
		'''

		if int(mode) == 1:
			self.bet = raw_input("Player: You have " + str(self.player.chips) + " chips. What is your bet?\n")

			if self.bet.isalpha() and self.bet in self.exitMoves:
				self.bet = 0.0
			else:
				while self.bet.isalpha() or int(self.bet) <= int(0):
					print("Your bet was invalid!")
					self.bet = raw_input("Player: Your bet has to bet at least 1 chip!\n")
				
				if self.bet < 1:
					self.bet = int(raw_input("Player: Your bet has to bet at least 1 chip!\n"))

				if int(self.bet) >= 1 and int(self.bet) > self.player.chips:
					self.bet = raw_input("Player: Player: You don't have enough chips for this bet!\n")

		elif int(mode) == 2:
			if self.moves == 1 and round(float(self.player.chips)/2.0,0) >= 1:
				self.bet = round(float(self.player.chips)/2.0,0)
			else:
				self.bet = self.player.chips
		elif int(mode) == 3:
			if self.player.chips >= self.bet*2:
				self.bet = self.bet*2
			else:
				print("Player: You don't have enough chips for this bet!")

		elif self.player.chips <= 0.0:
			print("Player: You have no more chips to bet!")
			self.bet = 0.0


		return int(self.bet)




	def checkWinner(self):
		"""
		Checks if there is a winner for the given hand, and if the player
		wants to continue playing
		"""
		result = self.winner()

		if result > 0:

			print("Player: Your deck is " + str(self.player.deck) + ". Dealer's deck is " + str(self.dealer.deck))
			cont = raw_input("Player: Try Again?\n")
			self.__init__(self.player)

			if cont == "y" :
				self.action = "h"
			else:
				self.action = "q"



	def winner(self):
		'''
		Check if the player meets all the conditions to win the game


		In the case of the 2 first cards the player and dealer receive,
		there is no bet involved but, we still want to check if the player
		has blackjack

		:rtype: int 
				0 - no winner yet
				1 - player wins
				2 - player has blackjack
				3 - dealer wins
				4 - push
		'''

		if self.player.hand > 21:
			self.player.updateChips(3,self.bet)
			print("Player busts: Player Loses!")
			return 3

		elif self.moves == 1 and self.player.hand == 21:
			self.player.updateChips(2,self.bet)
			print("BlackJack: Player Wins!")
			return 2
		elif self.bet != 0 and self.action == "s" and self.player.hand == self.dealer.hand:
			#Push: dealer and player have the same points
			print("Push!")
			return 4

		elif self.action == "s":
			if (self.player.hand <= 21 and self.player.hand > self.dealer.hand) or (self.dealer.hand < 21 and self.player.hand > self.dealer.hand):
				self.player.updateChips(1,self.bet)
				print("Player Wins!")
				return 1
			elif self.player.hand < 21 and (self.dealer.hand == 21 or (self.dealer.hand <= 21 and self.player.hand < self.dealer.hand)):
				self.player.updateChips(3,self.bet)
				print("Player Loses!")
				return 3

			elif self.dealer.hand > 21:
				self.player.updateChips(1,self.bet)
				print("Dealer busts: Player Wins!")
				return 1
		elif self.player.hand == 21:
				self.action = "s"
				return self.winner()
		else:
			return 0
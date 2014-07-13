from deck import Deck
from dealer import Dealer
from player import Player

class BlackJack:
	
	def __init__(self):
		'''
		Constructor of the BlackJack class, initializing the deck, the dealer's number of cards,
		and both the player and the dealer's hands and decks (i.e., the cards they have).
		'''
		#keep the number of moves in the game
		self.moves = 0
		#keep the bet the player made for the game
		self.bet = 0

		'''
		keep the move the player chose:
			h - hit
			s - stand
		'''
		self.action = ""

		self.deck = Deck()
		self.deck.emptyDeckOut()

		self.dealer = Dealer()

		Player.hand = 0		
		Player.deck = []


	def restartGame(self,Player):
		'''
		Method to restart the game
		'''
		self.moves = 0
		self.bet = 0
		self.action = ""

		self.deck = Deck()
		self.deck.emptyDeckOut()

		self.dealer = Dealer()

		Player.hand = 0		
		Player.deck = []




	
	def placeBet(self,Player):
		'''
		Method to place the player's bet
		Output - the bet the player has made
		'''
		self.bet = int(raw_input("Player: You have " + str(Player.chips) + " chips. What is your bet?\n"))

		if self.bet < 1:
			self.bet = int(raw_input("Player: Your bet has to bet at least 1 chip!\n"))

		return self.bet

	
	def winner(self,bet,action,deck,player,dealer):
		'''
		Check if the player meets all the conditions to win the game

		Input: 	bet - he player's bet
				action - The player's move (s: stand, h: hit)
		Output: 0 - no winner yet
				1 - player wins
				2 - player has blackjack
				3 - dealer wins
				4 - push
		'''
		

		'''
		In the case of the 2 first cards the player and dealer receive,
		there is no bet involved but, we still want to check if any of them
		has blackjack
		'''

		#print("\t [blackjack] hand " + str(player.hand))
		#print("\t [blackjack] hand " + str(dealer.hand))

		if player.hand > 21:
			player.updateChips(3,bet)
			print("Player busts: Player Loses!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
			return 3

		elif self.moves == 1 and player.hand == 21:
			player.updateChips(2,bet)
			print("BlackJack: Player Wins!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
			return 2
		elif bet != 0 and action == "s" and player.hand == dealer.hand:
			#Push: dealer and player have the same points
			print("Push!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
			return 4

		elif action == "s" and ((player.hand == 21 and dealer.hand < 21) or (player.hand > dealer.hand and dealer.hand < 21)  or  player.hand == 21):
			player.updateChips(1,bet)
			print("Player Wins!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
			return 1

		elif action == "s" and ( (player.hand < 21 and dealer.hand == 21) or (player.hand < dealer.hand and dealer.hand < 21)):
			player.updateChips(3,bet)
			print("Player Loses!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
			return 3

		elif action == "s" and dealer.hand > 21:
			player.updateChips(1,bet)
			print("Dealer busts: Player Wins!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
			return 1
		else:
			return 0

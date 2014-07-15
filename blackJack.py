#!/usr/bin/env python

from deck import Deck
from dealer import Dealer
from player import Player

'''
The BlackJack class represents the BlackJack table: it has a dealer,and a deck
'''
class BlackJack:
	
	def __init__(self,player):
		'''
		Constructor of the BlackJack class, initializing the deck, the dealer's number of cards,
		and both the player and the dealer's hands and decks (i.e., the cards they have).
		'''
		#keep the number of moves in the game
		self.moves = 0
		#keep the bet the player made for the game
		self.bet = 0

		
		#keep the move the player chose: h - hit, s - stand
		self.action = ""

		self.deck = Deck()
		self.deck.emptyPlayedCards()

		self.dealer = Dealer()

		player.hand = 0		
		player.deck = []

	
	def placeBet(self,player,mode,moves):
		'''
		Place the player's bet
		Input 	player - the player object
				mode - the game mode (1: input mode, 2: bot mode with the greedy player, 3: bot mode with the cautious player)
				moves - the number of moves of the game
		Output - the bet the player has made
		'''

		if int(mode) == 1:
			self.bet = raw_input("Player: You have " + str(player.chips) + " chips. What is your bet?\n")

			while self.bet.isalpha() or int(self.bet) <= int(0):
				print("Your bet was invalid!")
				self.bet = raw_input("Player: Your bet has to bet at least 1 chip!\n")
			
			if self.bet < 1:
				self.bet = int(raw_input("Player: Your bet has to bet at least 1 chip!\n"))
		elif int(mode) == 2:
			if moves == 1 and round(float(player.chips)/2.0,0) >= 1:
				self.bet = round(float(player.chips)/2.0,0)
			else:
				self.bet = player.chips
		elif player.chips <= 0.0:
			print("Player: You have no more chips to bet!")
			self.bet = 0.0

		return int(self.bet)

	
	def winner(self,bet,action,deck,player,dealer):
		'''
		Check if the player meets all the conditions to win the game


		In the case of the 2 first cards the player and dealer receive,
		there is no bet involved but, we still want to check if any of them
		has blackjack


		Input: 	bet - The player's bet
				action - The player's move (s: stand, h: hit)
				deck - The deck object
				player - The player object
				dealer - The dealer object

		Output: 0 - no winner yet
				1 - player wins
				2 - player has blackjack
				3 - dealer wins
				4 - push
		'''

		if player.hand > 21:
			player.updateChips(3,bet)
			print("Player busts: Player Loses!")
			return 3

		elif self.moves == 1 and player.hand == 21:
			player.updateChips(2,bet)
			print("BlackJack: Player Wins!")
			return 2
		elif bet != 0 and action == "s" and player.hand == dealer.hand: #action == "s"
			#Push: dealer and player have the same points
			print("Push!")
			return 4

		elif action == "s":
			if (player.hand <= 21 and player.hand > dealer.hand) or (dealer.hand < 21 and player.hand > dealer.hand):
				player.updateChips(1,bet)
				print("Player Wins!")
				return 1
			elif player.hand < 21 and (dealer.hand == 21 or (dealer.hand <= 21 and player.hand < dealer.hand)):
				player.updateChips(3,bet)
				print("Player Loses!")
				return 3

			elif dealer.hand > 21:
				player.updateChips(1,bet)
				print("Dealer busts: Player Wins!")
				return 1
		elif player.hand == 21:
				self.action = "s"
				winner(self,bet,action,deck,player,dealer)
		else:
			return 0

import deck
import player
import dealer

#keep the number of moves in the game
moves = 0

'''
Method to restart the game, initializing the deck, the dealer's number of cards,
and both the player and the dealer's hands.
'''
def initGame():
	
	deck.newDeck()
	deck.emptyDeckOut()
	dealer.numberCards = 0
	dealer.hand = 0
	player.hand = 0
	dealer.deck = []
	player.deck = []



'''
Method to place the player's bet
Output - the bet the player has made
'''
def placeBet():
	bet = int(raw_input("Player: You have " + str(player.chips) + " chips. What is your bet?\n"))

	if bet < 1:
		bet = int(raw_input("Player: Your bet has to bet at least 1 chip!\n"))

	return bet

'''
Check if the player meets all the conditions to win the game

Input: 	bet - he player's bet
		command - The player's move (s: stand, h: hit)
Output: 0 - no winner yet
		1 - player wins
		2 - dealer wins
		3 - push
'''
def winner(bet,command):
	global moves
	'''
	In the case of the 2 first cards the player and dealer receive,
	there is no bet involved but, we still want to check if any of them
	has blackjack
	'''

	#print("\t [blackjack] hand " + str(player.hand))
	#print("\t [blackjack] hand " + str(dealer.hand))

	if player.hand > 21:
		player.chips -= bet
		print("Player busts: Player Loses!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 2

	elif moves == 1 and player.hand == 1:
		player.chips += bet*1.5
		print("BlackJack: Player Wins!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 1
	elif bet != 0 and command == "s" and player.hand == dealer.hand:
		#Push: dealer and player have the same points
		print("Push!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 3

	elif (command == "s" and player.hand == 21 and dealer.hand < 21) or  player.hand == 21:
		player.chips += bet*2
		print("Player Wins!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 1

	elif command == "s" and player.hand < 21 and dealer.hand == 21:
		player.chips -= bet
		print("Player Loses!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 2

	elif command == "s" and dealer.hand > 21:
		player.chips += bet*2
		print("Dealer busts: Player Wins!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 1
	elif command == "s" and player.hand > dealer.hand and dealer.hand < 21:
		player.chips += bet*2
		print("Player Wins!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 1
	elif command == "s" and player.hand < dealer.hand and dealer.hand < 21:
		player.chips -= bet
		print("Player Loses!\nPlayer: Your deck is " + str(player.deck) + "\nDealer's deck is " + str(dealer.deck) + "\nPlayer: You have " + str(player.chips) + " chips.")
		return 2
	else:
		return 0

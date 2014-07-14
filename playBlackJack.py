from blackJack import BlackJack
from player import Player
from greedyPlayer import GreedyPlayer

def textBlackJack():
	'''
	A BlackJack game with user input
	'''

	print("---------------------------------------------------")
	print("*** BlackJack ***\n\nTo Hit type \"h\", to stand type \"s\", to Quit type \"q\" \n")
	print("---------------------------------------------------\n")

	blackJack = BlackJack()
	player = Player()

	while player.chips > 0:

		if blackJack.dealer.numberCards == 0:
			blackJack.bet = blackJack.placeBet(player,0,blackJack.moves)
			blackJack.dealer.dealCards(player,blackJack.deck)
			blackJack.moves += 1

		print("\t [][][] bet " + str(blackJack.bet))

		
		blackJack.action = raw_input("Player: Your deck is " + str(player.deck) + ". Your current hand is " +  str(player.hand) + ". What is your move?\n")

		if blackJack.action == "h" or blackJack.action.lower() == "hit":
			blackJack.moves += 1

			player.hand = player.makeMove(blackJack.deck)

			result = blackJack.winner(blackJack.bet,blackJack.action,blackJack.deck,player,blackJack.dealer)

			if result == 1 or result == 2 or result == 3:

				#cont = raw_input("Player: Try Again?\n")

				#if cont == "y" :
					blackJack.restartGame(player)
					continue
				#else:
				#	print("Player: You left the game with " + str(player.chips) + " chips.")
				#	return;
		elif blackJack.action == "s" or blackJack.action.lower() == "stand":

			blackJack.dealer.makeMove(blackJack.deck)

			result = blackJack.winner(blackJack.bet,blackJack.action,blackJack.deck,player,blackJack.dealer)

			if result == 1 or result == 2 or result == 3:

				#cont = raw_input("Player: Try Again?\n")

				#if cont == "y":
					blackJack.restartGame(player)
				#	continue
				#else:
				#print("Player: You left the game with " + str(player.chips) + " chips.")			
				#	return;

		elif blackJack.action == "q" or blackJack.action.lower() == "quit" :
			print("Player: You left the game with " + str(player.chips) + " chips.")
			return;
		else:
			print("This is an invalid play!\nTo Hit type \"h\", to stand type \"s\", to Quit type \"q\" \n")

	if player.chips == 0:
		print("Game Over!")


def playGreedyBlackJack():
	'''
	An automatic BlackJack game with with a greedy player
	'''

	print("---------------------------------------------------")
	print("*** BlackJack ***")
	print("---------------------------------------------------\n")

	blackJack = BlackJack()
	player = GreedyPlayer()

	print("Player: You have " + str(player.chips) + " chips.")

	while player.chips > 0:
		blackJack.moves += 1

		if blackJack.dealer.numberCards == 0:
			blackJack.bet = blackJack.placeBet(player,1,blackJack.moves)
			blackJack.dealer.dealCards(player,blackJack.deck)
			

		print("Player: Your bet was " + str(blackJack.bet) + " chips.")

		
		print("Player: Your deck is " + str(player.deck) + ". Your current hand is " +  str(player.hand) + ".")

		
		'''
		Player makes his greedy moves until his hand is >= 15
		and then is up to the dealer to make his moves
		'''
		player.hand = player.makeGreedyMove(blackJack.deck)

		if player.hand < 21:

			print("Player: Stands.")
			blackJack.dealer.makeMove(blackJack.deck)
			
			blackJack.action = "s"

		result = blackJack.winner(blackJack.bet,blackJack.action,blackJack.deck,player,blackJack.dealer)

		if result == 1 or result == 2 or result == 3:

			cont = raw_input("Player: Try Again?\n")

			if cont == "y":
				print("\n\n")
				blackJack.restartGame(player)
				continue
			else:
				print("Player: You left the game with " + str(player.chips) + " chips.")
				return;


def selectGameMode():
	'''
	Selects the BlackJack game that is going to be played
	Options: 1 - Users types the commands
			 2 - Automatic BlackJack game with a greedy player
			 3 - Automatic BlackJack game with a cautious player
	'''
	mode = raw_input("\nChoose how you want to play:\n\t1 - You type the commands\n\t2 - Let the greedy player play (always hits until his hand is >= 15, and always bets half his total chips\n\t3 - Let the cautious player play (analyzes every move and the odds of getting a good hand)\n")

	while mode.isalpha():
			print("This is an invalid choice!")
			mode = raw_input("\nChoose how you want to play:\n\t1 - You type the commands\n\t2 - Let the greedy player play (always hits until his hand is >= 15, and always bets half his total chips\n\t3 - Let the cautious player play (analyzes every move and the odds of getting a good hand)\n")
		

	if mode.isdigit():
		if int(mode) == 1:
			textBlackJack()
		elif int(mode) == 2:
			playGreedyBlackJack()
		elif int(mode) == 3:
			playCautiousBlackJack()
		else:
			print("This is an invalid choice!")
			selectGameMode()

def main():
	'''
	The BlackJack game initial screen, where the user can choose the kind of game he wants to play
	'''

	print("---------------------------------------------------")
	print("*** BlackJack ***\n")
	print("---------------------------------------------------\n")


	selectGameMode()
			

main()
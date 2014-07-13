from blackJack import BlackJack
from player import Player

def textBlackJack():
	'''
	Simulates a BlackJack game with user input
	'''

	print("---------------------------------------------------")
	print("*** BlackJack ***\n\nTo Hit type \"h\", to stand type \"s\", to Quit type \"q\" \n")
	print("---------------------------------------------------\n")

	blackJack = BlackJack()
	player = Player()

	while player.chips > 0:

		if blackJack.dealer.numberCards == 0:
			blackJack.bet = blackJack.placeBet(player)
			blackJack.dealer.dealCards(player,blackJack.deck)
			blackJack.moves += 1

		print("\t [][][] bet " + str(blackJack.bet))

		
		blackJack.action = raw_input("Player: Your deck is " + str(player.deck) + ". Your current hand is " +  str(player.hand) + ". What is your move?\n")

		if blackJack.action == "h":
			blackJack.moves += 1

			player.hand = player.makeMove(blackJack.deck)

			result = blackJack.winner(blackJack.bet,blackJack.action,blackJack.deck,player,blackJack.dealer)

			if result == 1 or result == 2 or result == 3:

				cont = raw_input("Player: Try Again?\n")

				if cont == "y":
					blackJack.restartGame(player)
					continue
				else:
					print("Player: You left the game with " + str(player.chips) + " chips.")
					return;
		elif blackJack.action == "s":

			blackJack.dealer.makeMove(blackJack.deck)

			result = blackJack.winner(blackJack.bet,blackJack.action,blackJack.deck,player,blackJack.dealer)

			if result == 1 or result == 2 or result == 3:

				cont = raw_input("Player: Try Again?\n")

				if cont == "y":
					blackJack.restartGame(player)
					continue
				else:
					print("Player: You left the game with " + str(player.chips) + " chips.")			
					return;

		elif blackJack.action == "q":
			print("Player: You left the game with " + str(player.chips) + " chips.")
			return;
		else:
			print("This is an invalid play")



textBlackJack()
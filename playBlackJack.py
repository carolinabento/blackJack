import deck
import player
import dealer
import blackJack


'''
Simulates a BlackJack game
'''

def playBlackJack():

	print("---------------------------------------------------")
	print("*** BlackJack ***\n\nTo Hit type \"h\", to stand type \"s\", to Quit type \"q\" \n")
	print("---------------------------------------------------\n")

	#print("\t [begining] dealer.hand " + str(dealer.hand) + " player.hand " + str(player.hand))

	blackJack.initGame()

	#print("\t deck.deckOut   "  + str(deck.deckOut))

	'''
	In the case of the 2 first cards the player and dealer receive,
	there is no bet involved, so this is a dummy value
	But we still want to check if the player has blackJack
	'''
	bet = 0
	action = ""
	#blackJack.winner(bet,action)

	while player.chips > 0:

		if dealer.numberCards == 0:
			bet = blackJack.placeBet()
			dealer.dealCards()
			blackJack.moves += 1

		#print("\t [][][] hand " + str(dealer.hand))

		
		action = raw_input("Player: Your deck is " + str(player.deck) + ". Your current hand is " +  str(player.hand) + ". What is your move?\n")

		if action == "h":
			blackJack.moves += 1

			player.hand = player.makeMove()



			#print("\t [][][] hand " + str(dealer.hand))

			#print("\t > deck.deckOut   "  + str(deck.deckOut))

			#print("\t hand " + str(player.hand))
			result = blackJack.winner(bet,action)

			#print("\t Winner? " + str(result))

			if result == 1 or result == 2 or result == 3:

				cont = raw_input("Player: Try Again?\n")

				if cont == "y":
					blackJack.initGame()
					bet = 0

					continue
				else:
					print("Player: You left the game with " + str(player.chips) + " chips.")
					return;
		elif action == "s":

			dealer.makeMove()

			result = blackJack.winner(bet,action)

			if result == 1 or result == 2 or result == 3:

				cont = raw_input("Player: Try Again?\n")

				if cont == "y":
					blackJack.initGame()
					bet = 0
					continue
				else:
					print("Player: You left the game with " + str(player.chips) + " chips.")			
					return;

		elif action == "q":
			print("Player: You left the game with " + str(player.chips) + " chips.")
			return;
		else:
			print("This is an invalid play")

		

playBlackJack()
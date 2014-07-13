from deck import Deck
from dealer import Dealer
from player import Player
from blackJack import BlackJack

class TestBlackJack:

	def __init__(self):
		return

	@staticmethod
	def testConstructor():

		bj = BlackJack()

		assert bj.moves == 0
		assert bj.bet == 0
		assert bj.action == ""

		assert bj.deck.deck["ace"][1] == 1
		assert bj.deck.deck["two"][1] == 2
		assert bj.deck.deck["king"][1] == 10
		assert bj.deck.deckOut == {}

	@staticmethod
	def testPlaceBet():

		bj = BlackJack()
		player = Player()

		assert bj.moves == 0
		assert bj.bet == 0
		assert bj.action == ""

		bj.placeBet(player)


	@staticmethod
	def testRestartGame():

		bj = BlackJack()
		player = Player()

		#players initial hand is blackjack
		bj.bet = 10
		bj.moves = 1
		action = ""
	
		bj.dealer.deck = [2,5]
		bj.dealer.hand = 7
		bj.dealer.upCard = 5

		player.hand = 21
		player.deck = [11,10]

		assert bj.bet == 10	
		assert bj.moves == 1		
		assert bj.winner(bj.bet,action,bj.deck,player,bj.dealer) == 2
		assert player.chips == 115

		bj.restartGame(player)

		assert bj.moves == 0
		assert bj.bet == 0
		assert bj.action == ""
		assert player.chips == 115

		assert player.hand == 0		
		assert player.deck == []

		assert bj.dealer.deck == []
		assert bj.dealer.hand == 0

	@staticmethod
	def testWinner():

	#def winner(self,bet,action,deck,player,dealer):

		bj = BlackJack()
		player = Player()

		#players initial hand is blackjack
		bj.bet = 10
		bj.moves = 1
		action = ""
	
		bj.dealer.deck = [2,5]
		bj.dealer.hand = 7
		bj.dealer.upCard = 5

		player.hand = 21
		player.deck = [11,10]

		assert bj.bet == 10	
		assert bj.moves == 1		
		assert bj.winner(bj.bet,action,bj.deck,player,bj.dealer) == 2
		assert player.chips == 115

		#players wins with a hand higher than the dealer's
		bj.bet = 10
		bj.moves = 3
		action = "s"
	
		bj.dealer.deck = [2,5,3]
		bj.dealer.hand = 10
		bj.dealer.upCard = 5

		player.hand = 14
		player.deck = [7,7]

		assert bj.bet == 10	
		assert bj.moves == 3		
		assert bj.winner(bj.bet,action,bj.deck,player,bj.dealer) == 1
		assert player.chips == 135

		#players wins because dealer busts
		bj.bet = 10
		bj.moves = 3
		action = "s"
	
		bj.dealer.deck = [2,5,5,10]
		bj.dealer.hand = 22
		bj.dealer.upCard = 5

		player.hand = 14
		player.deck = [7,7]

		assert bj.bet == 10	
		assert bj.moves == 3		
		assert bj.winner(bj.bet,action,bj.deck,player,bj.dealer) == 1
		assert player.chips == 155


		#players and dealer push: they have the same score
		bj.bet = 10
		bj.moves = 3
		action = "s"
	
		bj.dealer.deck = [2,5,5,6]
		bj.dealer.hand = 18
		bj.dealer.upCard = 5

		player.hand = 18
		player.deck = [7,7,4]

		assert bj.bet == 10	
		assert bj.moves == 3		
		assert bj.winner(bj.bet,action,bj.deck,player,bj.dealer) == 4
		assert player.chips == 155

		#players busts
		bj.bet = 10
		bj.moves = 3
		action = "s"
	
		bj.dealer.deck = [2,7]
		bj.dealer.hand = 9
		bj.dealer.upCard = 7

		player.hand = 22
		player.deck = [10,2,10]

		assert bj.bet == 10	
		assert bj.moves == 3		
		assert bj.winner(bj.bet,action,bj.deck,player,bj.dealer) == 3
		assert player.chips == 145

		#players loses because is hand is lower than the dealer's
		bj.bet = 10
		bj.moves = 3
		action = "s"
	
		bj.dealer.deck = [2,7,8]
		bj.dealer.hand = 17
		bj.dealer.upCard = 7

		player.hand = 16
		player.deck = [7,9]

		assert bj.bet == 10	
		assert bj.moves == 3		
		assert bj.winner(bj.bet,action,bj.deck,player,bj.dealer) == 3
		assert player.chips == 135



	@staticmethod
	def main():
		TestBlackJack.testConstructor()
		TestBlackJack.testPlaceBet()
		TestBlackJack.testRestartGame()
		TestBlackJack.testWinner()


TestBlackJack.main()
	
blackJack
=========

This repository contains the code for the classic BlackJack card game.

This BlackJack game contains a limited set of moves/actions:
* place a bet
* hit
* stand
* quit

You can play the **regular version**, where you type the command correspoding to each possible move, or your can **let a bot be the player**.

This bot can be two different players:
* **Greedy Player** - always hits until his hand is greater or equal to 15,
* **Cautious Player** - only hits if the probability of picking a card that will not make him bust (and lose the game) is greater or equal to 0.6, i.e., he has 60% of chance of not busting

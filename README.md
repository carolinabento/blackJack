BlackJack Card Game
=========

This repository contains the code for the classic BlackJack card game.

Table Of Contents
-----------------

* [Play BlackJack](#play)
* [Documentation](#docs)
* [Project Architecture](#architecture)



### <a name="play"></a>Play BlackJack

To play this text-based BlackJack download the project's source code, open a terminal shell in project root directory and type:

<code>./blackJack/playBlackJach.py</code>


### <a name="docs"></a>Documentation

This BlackJack game contains a limited set of [moves/actions]:
* place bet
* hit
* stand
* double down
* quit

You can play a **input-based version**, where you type the command correspoding to each possible move, or your can **let a bot be the player**.

This bot can be two different players:
* **Greedy Player** - always hits until his hand is greater or equal to 15,
* **Cautious Player** - only hits if the probability of picking a card that will not make him bust (and lose the game) is greater or equal to 0.6, i.e., he has 60% of chance of not busting

I


### <a name="architecture"></a>Project Architecture

Here is the UML class diagram for the BlackJack card game:

![][id]


[id]: https://github.com/carolinabento/blackJack/blob/master/imgs/blackJackUML.png  "Optional title attribute"
[moves/actions]: http://en.wikipedia.org/wiki/Blackjack#Player_decisions

BlackJack Card Game
=========

This repository contains the code for the classic BlackJack card game.

Table Of Contents
-----------------

* [Play BlackJack](#play)
* [Documentation](#docs)
* [Project Architecture](#architecture)



### <a name="play"></a>Play BlackJack

To play this text-based BlackJack download the project's source code, open your terminal in project root directory and type:

<code>./bin/playBlackJach.sh</code>


### <a name="docs"></a>Documentation

This BlackJack game contains a limited set of [moves/actions]:
* place bet
* hit
* stand
* double down
* quit

You can play a **input-based version**, where you type the command correspoding to each possible move, or your can **let a bot be the player**.

This bot can have two different strategies:
* **Greedy Player** - always hits until his hand is greater or equal to 15,
* **Cautious Player** - only hits if he has 60% chance of not busting

Here is a screenshot of the initial screen, where you can choose your game mode:

![][mode]
	


### <a name="architecture"></a>Project Architecture

Here is the UML class diagram for the BlackJack card game:

![][id]


[id]: https://github.com/carolinabento/blackJack/blob/master/imgs/blackJackUML.png
[mode]: https://github.com/carolinabento/blackJack/blob/master/imgs/chooseMode.png

[moves/actions]: http://en.wikipedia.org/wiki/Blackjack#Player_decisions

'''
Card Game: WAR
Objective
Build a simple card game between a player and the computer
The goal is to be the first to reach 10 points

Game Rules
The player gets one random card

The computer gets one random card

Card values:

A (Ace) → highest
K (King)
Q (Queen)
J (Jack)
10, 9, 8, .... 2
Use this code to generate random cards: click here

Scoring Rules
Player card > Computer card → Player gets +1 point
Computer card > Player card → Computer gets +1 point
Draw (same value) → 0 points to both
Game Flow
Start both scores at 0

Repeat rounds:

Deal one card to the player
Deal one card to the computer
Show both cards and their values
Update scores according to the rules
The game ends when:

Player score reaches 10 → Player wins
Computer score reaches 10 → Computer wins
Example Round
Player card: K ♠️
Computer card: 7 ♦️

Player wins the round (+1 point)
Score:
Player: 4
Computer: 3
Example Draw
Player card: 9 ❤️
Computer card: 9 ♣️

Draw – no points awarded
'''


'''
⭐⭐ Bonus: ⭐⭐
Card Game: 21 Boom 🃏
Objective
Build a simple two-player card game. The goal is to get as close as possible to 21 without going over

Card Rules
Number cards → value is the number
J / Q / K → value is 10
A (Ace) → value is 1
Use this code to generate random cards: click here
Game Setup
There are 2 players: Player 1 and Player 2
Each player starts with 2 random cards
Each player plays one at a time
Player Turn Rules
During a player turn:

Show the current cards and total value
Ask the player to choose:
0 = STOP
1 = CONTINUE
If the player chooses CONTINUE (1) → give one more card
If the player chooses STOP (0) → end the turn
If total equals 21 → instant win
If total is greater than 21 → player is disqualified
Game Flow
Player 1 plays first
Player 1 keeps choosing STOP or CONTINUE until:

they stop
reach 21
or are disqualified
Player 2 plays second
Player 2 plays only after Player 1 finishes
Same rules apply
Winner Decision
If one player is disqualified → the other player wins

If both players are valid:

the player closer to 21 wins
If both totals are equal → draw

Example – Game Flow (Single Player)
Initial state:

Player 1 cards:
7 ♦️  8 ♣️
Total: 15

Choose:
0 = STOP
1 = CONTINUE
Player chooses: 1 (CONTINUE)

Player 1 cards:
7 ♦️  8 ♣️  A ❤️
Total: 16

Choose:
0 = STOP
1 = CONTINUE
Player chooses: 1 (CONTINUE)

Player 1 cards:
7 ♦️  8 ♣️  A ❤️  K ♠️
Total: 26

❌ Player 1 is disqualified
Example – Stopping in Time
Player 1 cards:
10 ♠️  9 ♦️
Total: 19

Choose:
0 = STOP
1 = CONTINUE
Player chooses: 0 (STOP)

Player 1 stops with total: 19
Example – Player 2
Player 1 cards:
10 ❤️  10 ♠️
Total: 20 
20 > 19  🎯 WINNER OF THIS ROUND
'''
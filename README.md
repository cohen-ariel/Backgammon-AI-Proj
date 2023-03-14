# Backgammon-AI-Proj
Backgammon implementation where a user can play against an "AI strategy" opponent.

The final strategy is received as a heuristic which was advanced over rounds, as follows: 
Multiple heuristics are initialized randomly. And then, in each round, the current optional heuristics play each other and the "winner" 
heuristic proceeds to the next round.
Finally, the computer plays according to the Expecti-MiniMax algorithm, using the final heuristic received.

*(Game interface implemented using the PyGame library)

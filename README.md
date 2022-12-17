# COMP_257-Final_Project

## Problem 3
You are playing a game with a friend: There are some number of coins lined up in front
of you from left to right. On your turn, you can remove either the left-most coin or the
right-most coin and add it to your collection. You go first, and after that you and your
friend alternate turns. After all the coins are removed, each of your scores is the sum of
the values of the coins in your pile. Given the order of the coins, if you go first and play
optimally, how much money are you guaranteed to win? Meaning, even if your friend
plays optimally, how much will you win?

**Inputs**      
coins: The list containing the values for the coins that are generated      
player: Int value for the player that is playing first, used for Brute Force Algorithm

**Outputs**     
player_One_Score: The result for player one's score     
player_Two_Score: The result for player two's score
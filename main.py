import random

# Big O Notation: O(2^n)
def bruteForceAlgo(coins, player):
    # base case: if there are no more coins, return 0
    if not coins:
        return 0
  
    # recursive case: try taking the left-most coin and the right-most coin
    if player == 1:
        # player 1's turn: maximize score
        return max(
            coins[0] + bruteForceAlgo(coins[1:], (player + 1) % 2),
            coins[-1] + bruteForceAlgo(coins[:-1], (player + 1) % 2))
    else:
        # player 2's turn: minimize score
        return min(
            bruteForceAlgo(coins[1:], (player + 1) % 2),
            bruteForceAlgo(coins[:-1], (player + 1) % 2))

# Big O Notation: O(n)
def greedyAlgo(coins):
    player_One_Score = 0
    player_Two_Score = 0

    # keep track of which player's turn it is
    player = 1
  
    while coins:
        # take the maximum value coin
        if coins[0] > coins[-1]:
            coin = coins.pop(0)
        else:
            coin = coins.pop(-1)
        
        # add the coin to the appropriate player's score
        if player == 1:
            player_One_Score += coin
        else:
            player_Two_Score += coin
        
        # switch to the other player's turn
        player = (player + 1) % 2
  
    return player_One_Score, player_Two_Score

# Big O Notation: O(n^2)
def dynamic_Programming_Algo(coins):
    player_One_Score = 0
    player_Two_Score = 0
    # keep track of which player's turn it is
    player = 1
  
    while coins:
        # take the maximum value coin
        if coins[0] > coins[-1]:
            coin = coins.pop(0)
        else:
            coin = coins.pop(-1)
        
        # add the coin to the appropriate player's score
        if player == 1:
            player_1_score += coin
        else:
            player_2_score += coin
        
        # switch to the other player's turn
        player = (player + 1) % 2
  
    return player_One_Score, player_Two_Score

def main():
    pennies = 1
    nickels = 5
    dimes = 10
    quarters = 25
    half_dollars = 50

    # Create a randomly generated list that holds 100 coins.
    coins = random.choices([pennies, nickels, dimes, quarters, half_dollars], k=10)

    print(f"Here is the list of coins: {coins}")
    print("--------------------------\n")

    print("Brute Force")
    print("--------------------------")
    player_One_Brute_Force_Score = bruteForceAlgo(coins, 1)
    player_Two_Brute_Force_Score = sum(coins) - player_One_Brute_Force_Score
    print(f"Player 1's Score: {player_One_Brute_Force_Score} and Player 2's Score: {player_Two_Brute_Force_Score}\n")

    print("Greedy Algorithm")
    print("--------------------------")
    player_One_Greedy_Score, player_Two_Greedy_Score = greedyAlgo(coins)
    print(f"Player 1's Score: {player_One_Greedy_Score} and Player 2's Score: {player_Two_Greedy_Score}\n")

    print("Dynamic Programming Algorithm")
    print("--------------------------")
    player_One_DP_Score, player_Two_DP_Score = dynamic_Programming_Algo(coins)
    print(f"Player 1's Score: {player_One_Greedy_Score} and Player 2's Score: {player_Two_Greedy_Score}\n")


if __name__ == '__main__':
    main()
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
    # create a dictionary to store the results of subproblems
    memo = {}
    
    # define the recursive function to find the maximum score for a given range of coins
    def find_max_score(start, end):
        # base case: if there are no more coins, the maximum score is 0
        if start > end:
            return 0
        
        # check if the maximum score for this range of coins has already been calculated
        if (start, end) in memo:
            return memo[(start, end)]
        
        # calculate the maximum score for this range of coins by considering both options for the current player's move
        score1 = coins[start] + min(find_max_score(start+2, end), find_max_score(start+1, end-1))
        score2 = coins[end] + min(find_max_score(start+1, end-1), find_max_score(start, end-2))
        max_score = max(score1, score2)
        
        # store the result in the dictionary for future reference
        memo[(start, end)] = max_score
        
        return max_score
    
    # call the recursive function to find the maximum score for the entire range of coins
    player_One_Score = find_max_score(0, len(coins)-1)
    
    # player one's score is the maximum score, so player two's score is the sum of all the coins minus player one's score
    player_Two_Score = sum(coins) - player_One_Score
    
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
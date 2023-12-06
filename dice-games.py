import random

# Create a function that roll the dice
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

# Create a while loop to input a numbers of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("Invalid type of numbers! Try Again")

# Setup the maximum scores and the score list for each player
max_score = 10
players_score = [0 for _ in range(players)]

# Create a while loop to play the games and input the scores
while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer Number,", player_idx + 1, "turn just started!")
        print("Your total score is: ", players_score[player_idx], "\n")
        current_score = 0
        
        while True:
            should_role = input("Would you like to roll (y)? ")
            if should_role.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done! ")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            
            print("Your current score is: ", current_score)
        
        players_score[player_idx] += current_score
        print("Your total score is: ", players_score[player_idx])
        
# decides the winners
max_scores = max(players_score)
winning_idx = players_score.index(max_score)
print("Player number,", winning_idx +1, "is the winner with a score of: ",max_score)
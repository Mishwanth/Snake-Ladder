
                
            import random

# Snakes and Ladders positions
snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 22, 5: 8, 11: 26, 20: 29, 27: 84, 21: 82}

# Function to simulate dice roll
def roll_dice():
    return random.randint(1, 6)

# Function to handle snake or ladder
def check_snake_ladder(position):
    if position in snakes:
        print(f"Oops! Bitten by a snake, move down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder, move up to {ladders[position]}")
        return ladders[position]
    return position

# Function to play the game
def play_game(players):
    positions = {player: 0 for player in players}
    winner = None
    
    while not winner:
        for player in players:
            print(f"\n{player}'s turn.")
            dice = roll_dice()
            print(f"{player} rolled a {dice}.")
            positions[player] += dice
            
            if positions[player] > 100:
                positions[player] -= dice
                print(f"{player} can't move, stays at {positions[player]}.")
                continue
            
            positions[player] = check_snake_ladder(positions[player])
            print(f"{player} is now at position {positions[player]}.")

            if positions[player] == 100:
                winner = player
                print(f"\nCongratulations! {player} wins the game!")
                break

# Driver code
if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter player {i + 1} name: ") for i in range(num_players)]
    
    print("\nStarting the Snake and Ladder game!")
    play_game(players)

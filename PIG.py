import random

def roll_die():
    return random.randint(1, 6)

def take_turn(player_score):
    """Simulate a player's turn."""
    turn_total = 0
    while True:
        roll = roll_die()
        print(f"Roll: {roll}")
        if roll == 1:
            print("You rolled a 1, no points will be added")
            return 0
        else:
            turn_total += roll
            print(f"So far turn total is: {turn_total}")
            choice = input("Enter 'r' to roll again, 'p' to pass: ")
            if choice == 'p':
                return turn_total

def save_game(player1_score, player2_score):
    with open("save_game.txt", "w") as f:
        f.write(f"{player1_score},{player2_score}\n")

def load_game():
    try:
        with open("save_game.txt", "r") as f:
            scores = f.readline().split(',')
            return int(scores[0]), int(scores[1])
    except FileNotFoundError:
        return 0, 0

def pig_game():
    player1_score, player2_score = load_game()
    winning_score = int(input("Enter the winning score: "))

    while player1_score < winning_score and player2_score < winning_score:
        print("\nPlayer 1's turn:")
        player1_score += take_turn(player1_score)
        print(f"Player 1's total score: {player1_score}")
        save_game(player1_score, player2_score)
        if player1_score >= winning_score:
            print("Player 1 wins!")
            break

        print("\nPlayer 2's turn:")
        player2_score += take_turn(player2_score)
        print(f"Player 2's total score: {player2_score}")
        save_game(player1_score, player2_score)
        if player2_score >= winning_score:
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    pig_game()

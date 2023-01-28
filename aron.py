import random

player_score = 0 
computer_score = 0 
draw_game = 0
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        draw_game += 1
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            player_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            player_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            player_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

# Print the score of the game
print( f"Games Played: {player_score + computer_score + draw_game}" )

print( f"Your Score: {player_score}" )

print( f"Computer Score: {computer_score}" )

print( f"Draws: {draw_game}" )

"""
Name : Aron Tadesse
Id : 1369/12
"""

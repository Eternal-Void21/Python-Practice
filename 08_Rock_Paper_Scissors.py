import random
import sys

# Function for the game
def game():
    user_played = int(input("Choose: 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
    # To display user's choice
    while user_played>=0:
        if user_played>2:
            sys.exit("Wrong value entered.")
        elif user_played == 0:
            print("You chose: Rock")
            break
        elif user_played == 1:
            print("You chose: Paper")
            break
        else:
            print("You chose: Scissor")
            break
    # To generate computer's choice
    computer_played = random.randint(0,2)  # 0 for Rock, 1 for paper, 2 for Scissor
    while computer_played>=0:
        if computer_played == 0:
            print("Computer chose: Rock")
            break
        elif computer_played == 1:
            print("Computer chose: Paper")
            break
        else:
            print("Computer chose: Scissor")
            break

    # Rules to determine win, loss, or draw
    while True:
        if user_played == computer_played:   # Same choice
            print("It's a draw.")
            break
        else:
            if user_played == 0 and computer_played == 1:
                print("You lost.")
                break
            elif user_played == 0 and computer_played == 2:
                print("You win!")
                break
            elif user_played == 1 and computer_played == 0:
                print("You win!")
                break
            elif user_played == 1 and computer_played == 2:
                print("You lost.")
                break
            elif user_played == 2 and computer_played == 0:
                print("You lost.")
                break
            elif user_played == 2 and computer_played == 1:
                print("You win!")
                break

    # To play another game or not
    answer = input("Do you want to start another game? Y/N\n")
    if answer == "Y" or answer == "y":
        game()   # Calling the function to play the game again
    else:
        sys.exit("Thanks for playing!")

game()


# Import the random module to generate random choices
from random import randint

# todo: Function returns computer and user choice
# FUNCTION CHOICES: set of instructions for player to input choice and computer to randomly choose choice
# No parameters within the parenthesis as objects are returned as local references are changed in the function
# return objects of references user_choice and computer_choice as they are altered by user and computer
def choices():
    # list with assigned items r, p, s for computer random choice and user choice
    choice_list = ["Rock", "Paper", "Scissors"]
    # Prompt the user to enter their choice
    user_choice = input("Enter your choice (Rock, Paper or Scissors): ").capitalize()
    # Generate a random choice for the computer
    computer_number = randint(0, 2)
    # slices list from the outcome of random integer to return string value from list
    computer_choice = choice_list[computer_number]
    # Print the choices made by the user and the computer
    print(f"You choose: {user_choice}\nComputer chose: {computer_choice}.")
    # Return the choices made by the user and the computer
    return user_choice, computer_choice


# Function to determine the winner of a single game
# else
# todo: create a function that allows user to play out of 3 and ends game
# Function to determine the winner in a best of three games scenario

def determine_winner(user_choice, computer_choice, computer_score, user_score):
    if user_choice == computer_choice:
        print(f"It's a draw!\n{'-' * 35}")
    elif (
            user_choice == "Rock" and computer_choice == "Scissors" or user_choice == "Paper" and computer_choice ==
            "Rock" or user_choice == "Scissors" and computer_choice == "Paper"):
        print(f"You win!\n{'-' * 35}")
        user_score += 1
         # adds 1 to the user score board

    else:
        print(f"Computer wins, better luck next time!\n{'-' * 35}")
        computer_score += 1
    # Return the updated scores
    return user_score, computer_score


# or statement to be able to lge
# Function to display the score board
def score_board(user_score, computer_score, number_of_rounds):
    print(f"{"~" * 30}\n Num of Rounds: {number_of_rounds}")
    print(f"{"-" * 5} Score Board {"-" * 5}")
    print(f"Your Score: {user_score} | Computer: {computer_score}")
    print(f"{"~" * 30}")
    # Return the number of rounds and the scores
    return number_of_rounds, user_score, computer_score


# def final_score(user_score, computer_score):
#     if user_score == computer_score:
#         print("Draw!!")
#     elif user_score > computer_score:
#         print(f"Congrats, You won the game!!")
#     else:
#         print(f"Computer won the game!! Better luck next time!")


if __name__ == "__main__":
        user_choice, computer_choice = choices()
        user_score, computer_score = determine_winner(user_choice, computer_choice, computer_score=0, user_score=0)
        score_board(user_score, computer_score, number_of_rounds=0)


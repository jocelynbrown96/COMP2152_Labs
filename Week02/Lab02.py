import random
# COMP2152 Open Source Development Lab 2: Friday January 23rd, 2026
# Jocelyn Brown, Student Number: 101597391

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Select a number from the following list: 1 - Rock, 2 - Paper, 3 - Scissors: ")

playerChoice = int(playerChoice)

# User Input Check:
if playerChoice < 1 or playerChoice > 3:
    print("Error: You should choose a number between 1 and 3!")
else:
    # Develop the game logic through if/elif/else
    computerChoice = random.randint(1, 3)
    print(playerChoice, computerChoice)

    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")
    else:
        print("You lose!")
import random

# **********************************************
# Written by: YOUR NAME
# For: COP 1000
# Where: FSW Computer Science Program www.fsw.edu
# Professor: Rebecca Gubitti
# FINAL EXAMINATION 
# ***********************************************


def play_dice_game():
    win = 0
    loss = 0
    tie = 0

    print("Hello! Welcome To The Dice Game!")
    rules = """
This is a dice game where you roll two dice.
Here are the rules:
- If you get a 7 or 11, you win!
- If you get a 2, 3, or 12, you lose.
- Any other sum is a tie!
"""
    print(rules)

    while True:
        answer = input("Do you want to roll the dice? (Yes/No): ").lower()
        if answer == "no":
            break
        elif answer != "yes":
            print("Please answer 'Yes' or 'No'.")
            continue

        print("\nYou answered Yes!")

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total_roll = die1 + die2

        print(f"Your two dice rolled as a {die1} and a {die2}.")
        print(f"This equals {total_roll}.")

        if total_roll in (7, 11):
            print("Congrats, you won!")
            win += 1
        elif total_roll in (2, 3, 12):
            print("You lost! Better luck next time!")
            loss += 1
        else:
            print("You tied!")
            tie += 1

        print(f"\n--- Current Score ---")
        print(f"Wins: {win}")
        print(f"Losses: {loss}")
        print(f"Ties: {tie}")
        print(f"---------------------")

    print("\nThanks for playing!")
    print(f"Final Score:")
    print(f"You won {win} times!")
    print(f"You lost {loss} times!")
    print(f"You tied {tie} times!")
    input("Press Enter to exit.")

# Start the game
play_dice_game()
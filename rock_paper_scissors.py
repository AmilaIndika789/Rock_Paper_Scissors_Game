import random
from ascii_art import rock, paper, scissors

print("Welcome to the Rock Paper Scissor's Game!")


game_images = [rock, paper, scissors]

is_rock = lambda choice: choice == 0
is_paper = lambda choice: choice == 1
is_scissors = lambda choice: choice == 2
is_equal = lambda users_choice, computers_choice: users_choice == computers_choice
is_invalid = lambda choice: choice not in [0, 1, 2]

# User's Choice
prompt = "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
users_choice = int(input(prompt))
if is_invalid(users_choice):
    print("You typed an invalid input. You lose")
    exit()

print("You chose:")
print(game_images[users_choice])

# Computer's Choice
computers_choice = random.randint(0, 2)
print("Computer Chose:")
print(game_images[computers_choice])


if is_equal(users_choice, computers_choice):
    print("It's a draw")
else:
    if is_rock(users_choice):
        if is_paper(computers_choice):
            print("You lose")
        else:
            print("You win!")
    elif is_paper(users_choice):
        if is_rock(computers_choice):
            print("You win!")
        else:
            print("You lose")
    elif is_scissors(users_choice):
        if is_rock(computers_choice):
            print("You lose")
        else:
            print("You win!")
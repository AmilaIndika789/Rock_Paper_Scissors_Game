import secrets
from src.pkg.ascii_art import rock, paper, scissors

print("Welcome to the Rock Paper Scissor's Game!")


game_images = [rock, paper, scissors]


def is_rock(choice):
    return choice == 0


def is_paper(choice):
    return choice == 1


def is_scissors(choice):
    return choice == 2


def is_equal(first_choice, second_choice):
    return first_choice == second_choice


def is_invalid(choice):
    return choice not in [0, 1, 2]


def get_user_choice():
    prompt = "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
    choice = int(input(prompt))
    if is_invalid(choice):
        print("You typed an invalid input. You lose")
    return choice


def find_winner(users_choice, computers_choice):
    if is_equal(users_choice, computers_choice):
        print("It's a draw")
    else:
        if is_rock(users_choice):
            if is_paper(computers_choice):  # User = Rock, Computer = Paper
                print("You lose")
            else:  # User = Rock, Computer = Scissors
                print("You win!")
        elif is_paper(users_choice):
            if is_rock(computers_choice):  # User = Paper, Computer = Rock
                print("You win!")
            else:  # User = Paper, Computer = Scissors
                print("You lose")
        elif is_scissors(users_choice):
            if is_rock(computers_choice):  # User = Scissors, Computer = Rock
                print("You lose")
            else:  # User = Scissors, Computer = Paper
                print("You win!")


def main():
    # User's Choice
    users_choice = get_user_choice()

    print(f"You chose: {users_choice}")
    print(game_images[users_choice])

    # Computer's Choice
    computers_choice = secrets.randbelow(3)
    print(f"Computer Chose: {computers_choice}")
    print(game_images[computers_choice])

    find_winner(users_choice, computers_choice)


if __name__ == "__main__":
    main()

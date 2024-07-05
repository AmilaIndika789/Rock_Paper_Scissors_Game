import random
# from ascii_art import rock, paper, scissors

print("Welcome to the Rock Paper Scissor's Game!")


# game_images = [rock, paper, scissors]

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

def main():
    # User's Choice
    users_choice = get_user_choice()

    print(f"You chose: {users_choice}")
    # print(game_images[users_choice])

    # Computer's Choice
    computers_choice = random.randint(0, 2)
    print(f"Computer Chose: {computers_choice}")
    # print(game_images[computers_choice])


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

if __name__ == "__main__":
    main()
import random


def match_random_and_guess(guess, to):
    to = random.randint(0,to)
    if guess==to:
        return True
    else:
        return False

    


def main():
    print("Enter the range:")
    to = input()
    to = int(to)
    print("Enter your guess:")
    guess = input()
    guess = int(guess)

    result = match_random_and_guess(guess, to)

    if result:
        print("You guessed correctly.")
    else:
        print("You were wrong.")


    
game = True

while game:
    main()

    print("Do you want to play again y/n")
    
    while True:
        choice = input()
        if choice == "y":
            game = True
            break
        elif choice == "n":
            game = False
            break
        else:
            print("Please enter y or n.")
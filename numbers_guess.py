## https://gitlab.oit.duke.edu/colab/colab_summer_software_2021/-/blob/master/practice/NUMBER_GUESS.md

from random import randint


# Random integer user needs to guess
val = randint(1, 100)
print(val)


# guess counter and loop breaker bool checking for correct guess
loseCount = 0
noGuess = True

# behavior variables - read prompt for more info
# checks if guess by user was useless

lowUser = 0
highUser = 100


while noGuess:

    # if the user has guessed 5 times, kick them out
    if loseCount == 5:
        print("You reached the max number of guesses, you lose!")
        print(f"The correct number was {val}.")
        break

    user_input = input("Please guess a number: ")
    user_input = int(user_input)

    # checking user_input against random value
    if user_input == val:
        print(f"You got it! The value was {val}.")
        noGuess = False
        break
    elif user_input < val:
        print("You're guess was too low!")
        if(user_input < lowUser):
            print("That guess was useless.")
        else:
            lowUser = user_input
    else:
        print("You're guess was too high!")
        if(user_input > highUser):
            print("That guess was useless.")
        else:
            highUser = user_input


    loseCount += 1
    remainder = 5 - loseCount
    print(f"Guess count: {loseCount}, you have only {remainder} guesses left." )
    print("\n")


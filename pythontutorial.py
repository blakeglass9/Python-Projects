#
# Python: 3.11.7
#
# Author: Blake Glass
#
# Purpose: The Tech Academy - Python Course, Creating our first program together.
#

def start(nice=0, mean=0, name=""):
    # Get the user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
    Check if this is a new game or not.
    If it is new, get the user's name.
    If it is not a new game, thank the player for playing again and continue with the game.
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
            if name != "":
                print("\nWelcome, {}!".format(name))
                print("\nIn this game, you will be greeted by several different people.")
                print("You can choose to be nice or mean, but at the end of the game, your fate will be sealed by your actions.")
                stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a conversation. Will you be nice or mean (N/M)? \n>>> ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice += 1
            stop = False
        elif pick == "m":
            print("\nThe stranger glares at you menacingly and storms off...")
            mean += 1
            stop = False
        else:
            print("Invalid input. Please choose 'N' for nice or 'M' for mean.")
    score(nice, mean, name)  # Pass the 3 variables to the score function.

def show_score(nice, mean, name):
    print("\n{}, your current total: \n({} Nice) and ({} Mean)".format(name, nice, mean))

def score(nice, mean, name):
    # Score function is being passed the values stored within the 3 variables
    if nice > 2:  # If condition is valid, call win function passing in the variables so it can use them
        win(nice, mean, name)
    elif mean > 2:  # If condition is valid, call lose function passing in the variables so it can use them
        lose(nice, mean, name)
    else:  # Else, call nice_mean function passing in the variables so it can use them.
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job, {}! You win! \nEveryone loves you and you've made lots of friends along the way!".format(name))
    # Call again function and pass in our variables
    again(nice, mean, name)

def lose(nice, mean, name):
    # Substitute the {} wildcards with our variable values
    print("\nOh no, {}. You lose. You've been too mean, and everyone is upset with you.".format(name))
    # Call again function and pass in our variables
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        elif choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter 'y' for 'YES' or 'n' for 'NO':\n>>> ")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name as the user has elected to play again
    start(nice, mean, name)

if __name__ == "__main__":
    start()

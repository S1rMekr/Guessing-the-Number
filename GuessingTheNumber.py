# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
from art import tprint

a = random.randint(1, 9)
attemts = 0
sum = 0

tprint("WELCOME")
print("""
Rules:
-Guess the number in a range 0-9
-Write 'exit' to leave the game
""")


def restart():
    inp2 = input('Do you want to try again?\n').lower()
    global sum
    if inp2 == 'yes':
        sum = 0
        print("Try to guess the number:")
        return True
    elif inp2 == 'no':
        tprint('HAVE  A  NICE  DAY')
        return False


print("Try to guess the number:")
while True:
    inp = input().lower()
    if inp.isdigit():
        inp = int(inp)
        if inp == a:
            sum += 1
            print(f"You've made it!!!\nIt took {sum} tries to guess")
            restart()
        elif inp > a and inp < 10:
            sum += 1
            print("You're wrong, try lower")
        elif inp < a and inp > 0:
            sum += 1
            print("You're wrong, try higher")
        else:
            sum += 1
            print("Enter the number in the range 0-9")
    else:
        if inp == "exit":
            tprint('HAVE  A  NICE  DAY')
            sum = 0
            break
        elif inp == "higher":
            print('Not literally ^_^')
        elif inp == "lower":
            print('Not literally ^_^')
        else:
            print("Enter number in a range 0-9 or 'exit' to finish the game")

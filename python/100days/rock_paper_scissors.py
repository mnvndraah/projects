# Rock Paper Scissors Game | Day 4 of 100 Days Of Code
# A very simple version of the game... I did'nt want to waste much time on this.

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : "))

comp_ch = random.randint(0,2)

if comp_ch == 0:
    print("Computer chose rock")
    if choice == 0:
        print("You had a draw")
    elif choice == 1:
        print("User won")
    else:
        print("Computer won")
elif comp_ch == 1:
    print("Computer chose paper")
    if choice == 0:
        print("Computer won")
    elif choice == 1:
        print("Draw")
    else:
        print("User won")
elif comp_ch == 2:
    print("Computer chose Scissors")
    if choice == 0:
        print("User won")
    elif choice == 1:
        print("Computer won")
    else:
        print("Draw")
else:
    print("Invalid Input")
    exit()

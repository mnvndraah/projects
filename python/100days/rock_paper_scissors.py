import random

# Get user choice and validate input
try:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if choice not in [0, 1, 2]:
        raise ValueError
except ValueError:
    print("Invalid Input. Please enter 0, 1, or 2.")
    exit()

# Generate computer choice
comp_ch = random.randint(0, 2)

# Define choices
choices = ["Rock", "Paper", "Scissors"]

# Print choices
print(f"You chose {choices[choice]}")
print(f"Computer chose {choices[comp_ch]}")

# Determine winner
if comp_ch == choice:
    print("It's a draw!")
elif (choice == 0 and comp_ch == 2) or (choice == 1 and comp_ch == 0) or (choice == 2 and comp_ch == 1):
    print("You won!")
else:
    print("Computer won!")

# Treasure Hunt | Day 3 of 100 Days Of Code

print("Welcome to the Treasure Hunt!\nYour mission is to find the treasure...")

direct = input("You are currently at a crossroad... Where would you like to go? \nType 'left' or 'right': ")

if direct.lower() == 'left':
    swim = input("You have now reached a river... Type 'wait' to wait for a boat or 'swim' to swim: ")
    if swim == 'wait':
        door = input("You have now reached to a room, there are 3 doors. Type 'red' or 'yellow' or blue' to choose your door: ")
        if door == 'yellow':
            print("You reached a strange chest. \nYou open it, you find the treasure. \nYOU WIN!!!")
        elif door == 'red':
            print("The room was burning. You died to fire. \nYOU LOSE")
        elif door == 'blue':
            print("You were eaten by beasts. \nYOU LOSE")
        else:
            print("Invalid Input. \nYOU LOSE")
    else:
        print("You were attacked by a trout. \nYOU LOSE")
else:
    print("You had a great fall and you died. \nYOU LOSE")    

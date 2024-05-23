# Tip Calculator | Day 2 Of 100 Days Of Code

print("Welcome to the Tip Calculator")

bill = float(input("How much was the bill? $"))
tip = int(input("What percentage to give as tip? %"))
split = int(input("How many people to split the bill into? "))

total = (bill + bill*(tip/100))/split

print(f"Each person should pay: ${total}")


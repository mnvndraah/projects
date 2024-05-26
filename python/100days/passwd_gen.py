from string import ascii_letters
import random

print("Welcome to the PyPassword Generator")
letters = list(ascii_letters)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

letter = int(input("How many characters would you like?\n"))
number = int(input("How many numbers would you like?\n"))
symbol = int(input("How many symbols would you like?\n"))

passwd_list = []
passwd = ""

for i in range(letter):
    passwd_list += random.choice(letters)

for j in range(number):
    passwd_list += random.choice(numbers)

for k in range(symbol):
    passwd_list += random.choice(symbols)

random.shuffle(passwd_list)

for _ in passwd_list:
    passwd += _

print(f"Your password is {passwd}")

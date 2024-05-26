from string import ascii_letters
import random

letters = list(ascii_letters)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

letter = int(input("How many characters would you like?\n"))
number = int(input("How many numbers would you like?\n"))
symbol = int(input("How many symbols would you like?\n"))

passwd = ""

for i in range(letter):
    passwd += random.choice(letters)

for j in range(number):
    passwd += random.choice(letters)

for k in range(symbol):
    passwd += random.choice(symbols)

print(passwd)

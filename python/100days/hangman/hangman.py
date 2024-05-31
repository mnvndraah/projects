from random import choice
from styles import stages, logo
from time import sleep
from sys import exit
import words

print(logo)

word = (choice(words.word)).lower()
display = []
length = len(word)
lives = 6
game_end = False

for _ in word:
    display.append("_")

# Creating a while loop which runs till the game has not ended
while not game_end:

    guess = input("\n[+] Guess a letter: ")

    if guess in word:
        print("\n[!] You have already guessed that word. Please try again.")

    for position in range(length):
        if word[position] == guess:
            display[position] = guess # Replaces "_" at that index with the letter guessed


    if guess not in word: # When incorrect 
        lives -= 1
        print(f"\nThe letter you guessed was incorrect. You now have {lives} out of 6 lives")
    
    if "_" not in display:
        print("\n[~] You win!!!")
        game_end = True
    
    if lives == 0:
        print("\n[~] You lose!!!")
        game_end = True
    
    print("\n" + " ".join(display))
    print(stages[lives])

    if game_end == True:
        print("[!] Exitting in 10 seconds. Thank You for playing.")
        sleep(10)
        exit() # Using sys because after compiling to .exe the simple exit() command throws an error

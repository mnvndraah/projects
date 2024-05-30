from random import choice
from time import sleep
from art import stages, logo
import words
from sys import exit

print(logo)
word = choice(words.word)
len_word = len(word)
display = []
running = True
lives = 6

for _ in word:
    display.append("_")
while running:
    
    guess = input("[+] Guess a letter: ")

    if guess in display:
        print("[!] You already guessed that.")

    for letter in word:
        if guess == letter:
            ind = word.index(letter)
            display[ind] = guess
    
    if guess not in word:
        lives = lives -1
        print(f"[!] You guessed an incorrect letter. You lose a life. {lives} left")

    if "_" not in display:
        print("[~] You win.")
        running = False

    if lives == 0:
        running == False
        print(f" ".join(display))
        print(stages[lives])
        print(f"[~] You lose. The word was \"{word}\"")
        print(f"[-] Exitting in 10 seconds. ")
        sleep(10)
        exit(0)
    
        
    print(f" ".join(display))
    print(stages[lives])

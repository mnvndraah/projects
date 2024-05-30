from random import choice
from time import sleep
from art import stages, logo
import words

print(logo)
word = choice(words.word)
len_word = len(word)
display = ["_" for _ in word]
running = True
lives = 6

while running:
    guess = input("[+] Guess a letter: ").lower()

    if guess in display:
        print("[!] You already guessed that.")

    if guess in word:
        for index in range(len_word):
            if word[index] == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"[!] You guessed an incorrect letter. You lose a life. {lives} left")

    if "_" not in display:
        print(" ".join(display))
        print(stages[lives])
        print("[~] You win.")
        running = False

    if lives == 0:
        print(" ".join(display))
        print(stages[lives])
        print(f"[~] You lose. The word was \"{word}\".")
        running = False
    
    print(" ".join(display))
    print(stages[lives])

if not running:
    print("[-] Exiting in 10 seconds.")
    sleep(10)

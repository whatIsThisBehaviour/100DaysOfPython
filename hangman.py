from hangman_art import logo, stages
from hangman_words import word_list
import random
lives = 6
score = 0
display = []
game_is_over = False
print(logo)
print("Welcome to the hangman game. You have 6 lives to guess the correct word. Good Luck.")
chosen_word = random.choice(word_list)
# print(f"Psssst, the solution is {chosen_word}")
word_length = len(chosen_word)
for _ in range(0, word_length):
    display += "_"

while not game_is_over:
    guess_word = input("Type a letter : ").lower()
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess_word:
            display[position] = letter

    if "_" not in display:
        game_is_over = True
        print("You Win!")

    if guess_word not in chosen_word:
        lives -= 1
        if lives == 0:
            game_is_over = True
            print("You Lose !")

    print(f"{' '.join(display)}")
    print(stages[lives])



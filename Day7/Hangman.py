# Step 4

import random
import Hangman_art as art
import Hangman_words as words

end_of_game = False
chosen_word = random.choice(words.word_list).lower()
word_length = len(chosen_word)
lives = 6
stage_position = -1
# Testing code
# print(f'The solution is {chosen_word}.')
display = ["_"] * word_length

while not end_of_game:
    if lives != 0:
        guess = input("Guess a letter: ").lower()
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if guess in chosen_word:
                if letter == guess:
                    display[position] = letter
            else:
                lives -= 1
                print(f"You only have {lives + 1} lives")
                print(art.stages[stage_position])
                stage_position += -1
                break
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You won.")
    else:
        print("You have no more lives.\n", art.stages[0])
        print("You lost.")
        break

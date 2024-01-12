# Wordle Group Project - Team 2.7
# Seth Pobanz, Madison Hutchings, Teigen Burrows, Martin Villar

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    gw = WordleGWindow()

    def enter_action(s):
        word = ""
        for col in range(N_COLS):
            word += gw.get_square_letter(0, col)

        if word.lower() in FIVE_LETTER_WORDS:
            gw.show_message("The word you entered is a word!")
        else:
            gw.show_message("Not in word list")

    # Milestone #1: Display a random word in the first row
    random_word = random.choice(FIVE_LETTER_WORDS)
    
    # Display the random word in the first row
    for col in range(N_COLS):
        gw.set_square_letter(0, col, random_word[col])

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()

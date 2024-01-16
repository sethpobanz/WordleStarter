# Wordle Group Project - Team 2.7
# Seth Pobanz, Madison Hutchings, Teigen Burrows, Martin Villar

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR

def wordle():
    gw = WordleGWindow()

    def enter_action(s):
        word = ""
        for col in range(N_COLS):
            word += gw.get_square_letter(0, col)

        if word.lower() in FIVE_LETTER_WORDS:
            for col in range(N_COLS):
                if s[col] == word[col]:
                    gw.set_square_color(0, col, CORRECT_COLOR)
                elif s[col] in word:
                    gw.set_square_color(0, col, PRESENT_COLOR)
                else:
                    gw.set_square_color(0, col, MISSING_COLOR)

            # Check if the user guessed the entire word correctly
            if s.lower() == word.lower():
                gw.show_message("Congratulations! You guessed the word!")

            # Move on to the next row
            gw.set_current_row(gw.get_current_row() + 1)
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

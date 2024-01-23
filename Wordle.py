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
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                elif s[col] in word:
                    gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)

            # Check if the user guessed the entire word correctly
            if s.lower() == word.lower():
                gw.show_message("Congratulations! You guessed the word!")

            # Move on to the next row
            next_row = gw.get_current_row() + 1
            if next_row < N_ROWS:
                gw.set_current_row(next_row)
                
            else:
                gw.show_message("Game Over: You reached the last row!")

        else:
            gw.show_message("Not in word list")

    
    random_word = random.choice(FIVE_LETTER_WORDS)

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()


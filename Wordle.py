# Wordle Group Project - Team 2.7
# Seth Pobanz, Madison Hutchings, Teigen Burrows, Martin Villar

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR

def wordle():
    gw = WordleGWindow()
    toggle_button = gw.create_toggle_button()


    # occurs only when user presses/selects "Enter"
    def enter_action(s, random_word): 

        gw.show_message(random_word)

        # set variable to the selected randomized word (now it should stay for the whole
        # game until new game is played)
        word = random_word
        
        # first if statement checks to see if user entered valid word, then assigns all chars
        # with a color that shows if it matches in some way with the randomized word

        # MAKE SURE THAT LETTER IS NOT DONE 2x when it already was used
        numPresent = 0
        # Initialize a set to keep track of used letters
        used_letters = set()

        if s.lower() in FIVE_LETTER_WORDS:
            for col, char in enumerate(random_word):
                if s[col].lower() == char.lower():
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                    # Mark the letter as used
                    used_letters.add(s[col].lower())
                elif s[col].lower() in random_word.lower() and s[col].lower() not in used_letters:
                    gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                    # Mark the letter as used
                    used_letters.add(s[col].lower())
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

    # used the lambda feature that allows the s value AND the random_word variable into the method 
    gw.add_enter_listener(lambda s: enter_action(s, random_word))

    # Initialize colorblind_mode variable
    gw._colorblind_mode = False

# Startup code
if __name__ == "__main__":
    wordle()







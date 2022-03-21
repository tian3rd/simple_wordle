"""
Wordle
Assignment 1
Semester 1, 2022
CSSE1001/CSSE7030
"""

from re import S
from string import ascii_lowercase
from typing import Optional

from a1_support import (
    load_words,
    choose_word,
    VOCAB_FILE,
    ANSWERS_FILE,
    CORRECT,
    MISPLACED,
    INCORRECT,
    UNSEEN,
)

MAX_GUESSES = 6

# Replace these <strings> with your name, student number and email address.
__author__ = "<Your Name>, <Your Student Number>"
__email__ = "<Your Student Email>"

def has_won(guess: str, answer: str) -> bool:
    """ Returns True if the guess is correct, False otherwise.

    Parameters:
        guess (str): The current guess.
        answer (str): The correct answer.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    assert len(guess) == 6 and len(answer) == 6
    return guess == answer

def has_lost(guess_number: int) -> bool:
    """ Returns True if the number of guesses that have occurred is equal to or greater than the maximum number of guesses, False otherwise.

    Parameters:
        guess_number (int): The number of guesses that have occurred.

    Returns:
        bool: True if the number of guesses that have occurred is equal to or greater than the maximum number of guesses, False otherwise.
    """
    return guess_number >= MAX_GUESSES
    
def remove_word(words: tuple[str, ...], word: str) -> tuple[str, ...]:
    """ Removes the given word from the given words.
    
    Parameters:
        words (tuple[str]): The words to remove the given word from.
        word (str): The word to remove from the given words.
    """
    return tuple(w for w in words if w != word)

def prompt_user(guess_number: int, words: tuple[str, ...]) -> str:
    """ Prompts the user for the next guess, reprompting until either a valid guess is entered, or a selection for help, keyboard, or quit is made.

    Parameters:
        guess_number (int): The number of guesses that have occurred.
        words (tuple[str]): The words that the user has not yet guessed.

    Returns:
        str: first valid guess or request for help, keyboard, or quit.
    """
    user_input = input(f"Enter guess {guess_number}: ")




# Add your functions here

def main():
    print("Implement your solution and run this file")


if __name__ == "__main__":
    main()

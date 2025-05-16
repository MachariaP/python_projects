#!/usr/bin/env python3

import random

word_list = ["python", "developer", "programming", "algorithm", "function",
             "variable", "debugging", "compiler", "codechef", "machine",
             "bitcoin", "operation"]

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_game():
    original_word = random.choice(word_list)
    scrambled = scramble_word(original_word)

    print("\nWelcome to the Word Scramble Game!")
    print(f"Scrambled word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input(
                f"\nYou have {attempts} attempts left. Enter your guess: ").lower().strip()

        if guess == original_word:
            print("Congratulations! You unscrambled the word correctly!")
            return
        else:
            print("Incorrect guess. Try again!")
            attempts -= 1

    print(f"\nGame Over! The correct word was: {original_word}")


if __name__ == "__main__":
    play_game()

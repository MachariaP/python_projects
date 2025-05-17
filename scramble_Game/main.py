#!/usr/bin/env python3

import random
import time
import json
import os

def load_words():
    with open("words.json", "r") as f:
        return json.load(f)

def load_leaderboard():
    if os.path.exists("leaderboard.json"):
        with open("leaderbaord.json", "r") as f:
            return json.load(f)
    return []

def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f, indent=2)

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_game():
    word_categories = load_words()
    print("Categories:", ", ".join(word_categories.keys()))
    category = input("Choose a category (or press Enter for random: ").lower().strip()
    if not category or category not in word_categories:
        category = random.choice(list(word_categories.keys()))
    words = word_categories[category]

    print("Difficulty levels: easy, medium, hard")
    difficulty = input("Choice difficulty (easy/medium/hard): ").lower().strip()
    if difficulty not in ["easy", "medium", "hard"]:
        difficulty = "medium"

    if difficulty == "easy":
        candidates = [w for w in words if len(w) < 6]
    elif difficulty == "medium":
        candidates = [w for w in words if 6 <= len(w) <= 8]
    else:  # hard
        candidates = [w for w in words if len(w) > 8]
    if not candidates:
        candidates = words
    original_word = random.choice(candidates)
    scrambled = scramble_word(original_word)

    print(f"\nCategory: {category}, Difficulty: {difficulty}")
    print(f"Scrambled word: {scrambled}")

    attempts = 5 if difficulty == "easy" else 4 if difficulty == "medium" else 3
    start_time = time.time()

    while attempts > 0:
        guess = input(f"\nYou have {attempts} attempts left. Enter your guess: ").lower().strip()

        if guess == original_word:
            time_taken = time.time() - start_time
            score = max(1000 - int(time_taken * 10) - (5 - attempts) * 100, 0)
            print(f"\nCongratulations! You unscrambled the word in {time_taken:.1f} swconds!")
            print(f"Score: {score}")
            player_name = input("Enter your name for the leaderboard: ").strip() or "Anonymous"
            leaderboard = load_leaderboard()
            leaderboard.append({"name": player_name, "score": score, "difficulty": difficulty})
            leaderboard.sort(key=lambda x: x["score"], reverse=True)
            save_leaderboard(leaderboard[:5])
            return True
        else:
            print("Incorrect guess. Try again!")
            attempts -= 1

    print(f"\nGame Over! The correct word was: {original_word}")
    return False

def main():
    while True:
        if play_game():
            print("\nYou Won!")
        else:
            print("\nBetter luck next time!")

        play_again = input("\nPlay again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

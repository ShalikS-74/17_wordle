import random
from words import WORDS
from feedback import evaluate

SUPPORTED_LENGTHS = (4, 5, 6)


class WordleGame:
    def __init__(self, length=5):
        if length not in SUPPORTED_LENGTHS:
            raise ValueError(f"Choose a word length from: {SUPPORTED_LENGTHS}")
        self.length = length
        self.max_guesses = 6
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def run(self):
        print(f"Wordle — {self.length} letters, {self.max_guesses} guesses.")
        while len(self.history) < self.max_guesses:
            guess = input("> ").strip().lower()
            if guess == "q":
                print("Game ended.")
                return
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            print(" ".join(feedback))
            if guess == self.target:
                print("Solved!")
                return
        print(f"Out of guesses. The word was: {self.target}")

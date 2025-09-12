import random

# Hangman stages (6 tries total)
HANGMAN = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Word bank with hints
WORDS = {
    "python": "A programming language that’s named after a comedy group.",
    "elephant": "The largest land animal.",
    "guitar": "A musical instrument with strings.",
    "pizza": "A popular Italian dish.",
    "venus": "The second planet from the Sun."
}

def choose_word():
    word, hint = random.choice(list(WORDS.items()))
    return word, hint

def play():
    word, hint = choose_word()
    guessed = set()
    tries = 6
    print("Welcome to Hangman!")
    print("Type 'hint' if you need help (costs 1 try).")
    
    while tries >= 0:
        # Show state
        print(HANGMAN[6 - tries])
        display = " ".join([c if c in guessed else "_" for c in word])
        print("Word:", display)
        print("Tries left:", tries)
        print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "(none)")
        
        if all(c in guessed for c in word):
            print("🎉 You won! The word was:", word)
            break
        
        if tries == 0:
            print("💀 You lost! The word was:", word)
            break
        
        guess = input("Enter a letter or word: ").lower().strip()
        
        if not guess:
            print("Please enter something.")
            continue
        if guess == "hint":
            print("Hint:", hint)
            tries -= 1
            continue
        if len(guess) == 1:  # letter
            if guess in guessed:
                print("You already guessed that.")
            elif guess in word:
                print("✅ Good guess!")
                guessed.add(guess)
            else:
                print("❌ Wrong guess.")
                guessed.add(guess)
                tries -= 1
        else:  # word guess
            if guess == word:
                print("🎉 Correct! The word was:", word)
                break
            else:
                print("❌ Wrong word guess.")
                tries -= 1

if __name__ == "__main__":
    play()

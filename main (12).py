import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "game", "code", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)

            if guess not in word:
                attempts -= 1
                print("Incorrect guess. Attempts left:", attempts)
                if attempts == 0:
                    print("You've run out of attempts. The word was:", word)
                    break

        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
            break

if __name__ == "__main__":
    hangman() 
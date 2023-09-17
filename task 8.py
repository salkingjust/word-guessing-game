import random

# List of words
word_list = [
    "apple", "banana", "cherry", "dog", "elephant", "flower", "giraffe", "hamburger", "icecream", "jacket",
    "kangaroo", "lemon", "mountain", "narwhal", "octopus", "penguin", "quokka", "rainbow", "strawberry",
    "tiger", "umbrella", "volcano", "watermelon", "xylophone", "zebra"
]

def choose_word():
    return random.choice(word_list)

def display_word(word):
    displayed_word = word[0] + "_" * (len(word) - 2) + word[-1]
    return displayed_word

def main():
    print("Welcome to the Word Guessing Game!")
    while True:
        target_word = choose_word()

        displayed_word = display_word(target_word)

        print(f"Guess the word: {displayed_word}")

        user_guess = input("Your guess: ").lower()

        if user_guess == target_word:
            print("Congratulations! You guessed the word correctly.")
        else:
            print(f"Sorry, the correct word was: {target_word}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

main()

import random
words = ["python", "rocket", "diamond", "captain", "library"]
secret_word = random.choice(words)
hidden_word = ""
for i in secret_word:
    hidden_word += "_"
chance = 6
guessed_letters = []
print("=== Hangman Game ===")
while chance > 0:
    print("\nWord :", hidden_word)
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("Already guessed!")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        new_word = ""
        for i in range(len(secret_word)):
            if secret_word[i] == guess or secret_word[i] in guessed_letters:
                new_word += secret_word[i]
            else:
                new_word += "_"
        hidden_word = new_word
        print("Correct Guess!")
    else:
        chance -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", chance)
    if "_" not in hidden_word:
        print("\nCongratulations! You Won")
        print("The word was:", secret_word)
        break
if "_" in hidden_word:
    print("\nYou Lost!")
    print("The word was:", secret_word)
from wordguessinggame import WordGuessingGame

guess = WordGuessingGame()

print("Welcome to WORD GUESSING GAME.", end="\n\n")

guess.random_word = guess.randomWordSelector()
print(f"Random Word has been generated. The size of the word is {len(guess.random_word)}.")
print("You have 12 no.of tries to select an alphabet. Best of luck.", end="\n\n")

guess.intialize_string()

while(guess.tries and (not guess.checkString())):
    print(f"{13-guess.tries} TRY. Enter the alphabet:", end=" ")
    guess.guessed_alphabet = input()

    guess.checkRandomAlphabet()
    print(guess.string, end="\n\n")

    guess.tries -= 1

if guess.checkString():
    print(f"Successfully guessed the word: \"{guess.random_word}\"")
else:
    print(f"Unsuccessful attempt. The word was \"{guess.random_word}\"")
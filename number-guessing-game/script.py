from NumberGuessingGame import NumberGuessingGame

guess = NumberGuessingGame()

print("Welcome to Number Guessing Game. ", end="\n\n")

print("Enter the first number that will be the starting of the range:", end=" ")
guess.range_first = int(input())

print("Enter the second number that will be the ending of the range:", end=" ")
guess.range_second = int(input())

guess.max_tries = guess.generateNumOfGuesses()
generated_num = guess.randomNumber()

while(not guess.checkCondition(generated_num, guess.user_defined_number, guess.count)):
    print(f"Guess a number within the range {guess.range_first} to {guess.range_second}: ", end = " ")
    guess.user_defined_number = int(input())

    guess.checkSmallHigh(generated_num,guess.user_defined_number)

result = f"SUCCESSFUL in {guess.count} attempt." if not guess.checkCount() else f"UNSUCCESSFUL attempt."

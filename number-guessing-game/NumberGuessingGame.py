import random
import math

class NumberGuessingGame:
    def __init__ (self):
        self._range_first = -1
        self._range_second = -1
        self._user_defined_number = -1
        self._count = 0
        self._max_tries = -1
    
    @property
    def range_first(self):
        return self._range_first

    @range_first.setter
    def range_first(self, range_first):
        self._range_first = range_first

    @property
    def range_second(self):
        return self._range_second

    @range_second.setter
    def range_second(self, range_second):
        self._range_second = range_second

    @property
    def user_defined_number(self):
        return self._user_defined_number

    @user_defined_number.setter
    def user_defined_number(self, user_defined_number):
        self._user_defined_number = user_defined_number
        self._count += 1

    @property
    def max_tries(self):
        return self._max_tries

    @max_tries.setter
    def max_tries(self, max_tries):
        self._max_tries = max_tries

    @property
    def count(self):
        return self._count

    def randomNumber(self):
        return random.randint(self.range_first, self.range_second)

    def generateNumOfGuesses(self):
        return round(math.log((self.range_second-self.range_first+1), 2))

    def checkGuessedNumber(self, generated_num, user_num):
        if generated_num == user_num :
            return True
        else:
            return False

    def checkCount(self):
        if self.count>self.max_tries:
            return True
        else:
            return False

    def checkCondition(self,generated_num, user_num, count):
        if self.checkCount() or self.checkGuessedNumber(generated_num, user_num):
            return True
        else:
            return False

    def checkSmallHigh(self, guessed_num, user_num):
        if user_num>guessed_num:
            print("You guessed too high", end="\n\n")
        elif user_num<guessed_num:
            print("You guessed too low", end="\n\n")
        else:
            exit

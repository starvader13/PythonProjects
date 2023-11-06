import random

class WordGuessingGame:
    def __init__(self):
        self._random_word = ""
        self._guessed_alphabet = ""
        self._string =  ""
        self.__tries = 12
        self.list_word = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']


    @property
    def guessed_alphabet(self):
        return self._guessed_alphabet

    @guessed_alphabet.setter
    def guessed_alphabet(self, guessed_alphabet):
        self._guessed_alphabet = guessed_alphabet

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    @property
    def random_word(self):
        return self._random_word

    @random_word.setter
    def random_word(self, random_word):
        self._random_word = random_word

    @property
    def tries(self):
        return self.__tries

    @tries.setter
    def tries(self,tries):
        self.__tries = tries


    def randomIndexGenerator(self):
        return random.randint(0,len(self.list_word)-1)

    def randomWordSelector(self):
        return (self.list_word[self.randomIndexGenerator()])

    def intialize_string(self):
        self.string = "_" * len(self.random_word) 

    def stringToList(self):
        return list(self.string)

    def listToString(self, temp_list):
        return "".join(temp_list)

    def checkRandomAlphabet(self):
        temp_list = self.stringToList()
        for index, char in enumerate(self.random_word):
            if self.guessed_alphabet == char:
                temp_list[index] = self.guessed_alphabet    
        self.string = self.listToString(temp_list)

    def checkString(self):
        if self.string == self.random_word:
            return True
        else:
            return False

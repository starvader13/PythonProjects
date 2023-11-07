import random

class TwentyPLusOneGame:
    def __init__(self):
        self._start = None
        self._count_list = []
        self._user_playing_position = None
        self._itr=0
        self._user_input = None

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        if(start!="Yes" and start!="No"):
            raise Exception("The enetered string should either be \"Yes\" or \"No\"")
        elif(start=="Yes"):
            self._start = True
        else:
            self._start = False

    @property
    def count_list(self):
        return self._count_list

    @count_list.setter
    def count_list(self, count):
        if not isinstance(count, int):
            raise Exception("The entered value is not an integer")
        self._count_list.append(count)

    @property
    def user_playing_position(self):
        return self._user_playing_position

    @user_playing_position.setter
    def user_playing_position(self, first_second):
        if(first_second!="F" and first_second!="S"):
            raise Exception("The enetered string should either be \"F\" or \"s\"")
        
        if(first_second=="F"):
            self._user_playing_position = True
        else:
            self._user_playing_position= False

    @property
    def itr(self):
        return self._itr

    @itr.setter
    def itr(self, itr):
        if not isinstance(itr, int):
            raise Exception("Enter a valid integer number.")

        self._itr = itr

    @property
    def user_input(self):
        return self._user_input

    def user_input(self, user_input):
        if not isinstance(user_input, int):
            raise Exception("Enter a valid integer number.")

        self._user_input = user_input

    def checkStart(self):
        if self.start != True:
            print("\nExitting the game ....")
            exit()

    def checkIteration(self):
        if self.itr >= 4:
            print("You have been disqualified from the game for entering the count of number greater than pr equal to 4")
            exit()

    def checkListContinuity(self):
        if  (self.count_list)==0:
            pass
        elif self.user_input - self.count_list[-1] == 1:
            pass
        else:
            print("The continuity of the list element is not maintained.")
            exit()

    def userChance(self):
        print("\nEnter the count of number you want to enter.")
        print("> ", end="")
        self.itr = int(input())

        self.checkIteration()

        while self.itr:
            print("\nEnter the number you want to enter:")
            print("> ", end="")
            self.user_input = int(input())
            self.checkListContinuity()
            itr -= 1

    def computerChance(self):
        self.itr = random.randint(1,3)
        while self.itr:
            self.count_list = len(self.count_list)
            self.itr -= 1
    
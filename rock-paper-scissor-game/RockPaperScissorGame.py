import random

class RockPaperScissorGame:
    def __init__(self):
        self._game_element = ["Rock", "Paper", "Scissor"]
        self._username = None
        self._user_input = None
        self._computer_input = None
        self._winner_output = None
        self._next_turn = True

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not isinstance(username, str) or len(username)<=1:
            raise Exception("The Name of the user should be a valid string")
        self._username = username

    @property
    def game_element(self):
        return self._game_element

    @property
    def user_input(self):
        return self._user_input

    @user_input.setter
    def user_input(self, user_input):
        if not isinstance(user_input, int) and (user_input>=1 and user_input<=3):
            raise Exception("The entered user input should only be a integer")
        self._user_input = self.game_element[user_input-1]

    @property
    def computer_input(self):
        return self._computer_input

    @computer_input.setter
    def computer_input(self, computer_input):
        if not isinstance(computer_input, str):
            raise Exception("The computer input should only be a string")
        self._computer_input = computer_input

    @property
    def winner_output(self):
        return self._winner_output

    @winner_output.setter
    def winner_output(self, winner_output):
        if not isinstance(winner_output, bool):
            raise Exception("The assigned value to the winner output should only be a boolean value")
        self._winner_output = winner_output
    
    @property
    def next_turn(self):
        return self._next_turn

    @next_turn.setter
    def next_turn(self, next_turn):
        next_turn = next_turn.lower()
        if next_turn != "y" and next_turn != "n" and next_turn != "yes" and next_turn != "no":
            raise Exception("The entered valued can either be Yes OR Y / NO or N")

        self._next_turn = True if (next_turn == "yes" or next_turn == "y") else False

    def popElementFromList(self, index = None):
        if self.game_element:
            if index is None:
                self._game_element.pop()
            elif index>=0 and index<len(self.game_element):
                self._game_element.pop(index)
            else:
                raise Exception("List Index Out Of Bond")
        else:
            raise Exception("List is not empty")

    def randomIndex(self):
        return random.randint(0, len(self.game_element)-1)
    
    def intializeComputerInput(self):
        game_element_temp = self.game_element
        self.popElementFromList(self.game_element.index(self.user_input))
        return game_element_temp[self.randomIndex()]

    def chooseWinner(self):
        if (self.user_input=="Rock" and self.computer_input=="scissor") or (self.user_input=="Scissor" and self.computer_input=="Paper") or (self.user_input=="Paper" and self.computer_input=="Rock"):
            print(f"{self.username} wins the game:", end = "\n\n")
        else:
            print("Computer wins the game.", end = "\n\n")

    def setValueForNextTurn(self):
        print("Do you wanna play one more chance? Yes/No[Y/N]: ",end="")
        self.next_turn = str(input())

    def computerTurn(self):
        print("\nComputer's Turn ... ")
        self.computer_input = self.intializeComputerInput()
        print(f"Computer Choice is: {self.computer_input}", end = "\n\n")

    def userTurn(self):
        self.user_input = int(input())
        print(f"User Choice is: {self.user_input}")

    def gameDetails(self):
        print(f"Game: {self.user_input} vs {self.computer_input}", end = "\n\n")
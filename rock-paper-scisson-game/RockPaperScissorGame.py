class RockPaperScissorGame:
    def __init__(self):
        self._game_element = ["Rock", "Paper", "Scissor"]
        self._user_input = None
        self._computer_input = None
        self._winner_output = None

    @property
    def game_element(self):
        return self._game_element

    @property
    def user_input(self):
        return self._user_input

    @user_input.setter
    def user_input(self, user_input):
        if not isinstance(user_input, str):
            raise Exception("The entered user input should only be a string")
        self._user_input = user_input

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
        self._winner_output = winner_outputx
    
import random

class CowsAndBullsGame:
    def __init__(self):
        self._user_name = None
        self._secret_code = None
        self._user_code = None
        self._num_bulls = None
        self._num_cows = None

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        if not isinstance(user_name, str):
            raise Exception("The name of the user should be a String only")
        if len(user_name)<3:
            raise Exception("Please enter a valid name whose length should be greater than or equal to 3")
        self._user_name = user_name

    @property
    def secret_code(self):
        return self._secret_code

    @secret_code.setter
    def secret_code(self, secret_code):
        if not isinstance(secret_code, int) and (secret_code<1000 and secret_code>9999):
            raise Exception("The secret code should be a valid 4 digit integer.")
        self._secret_code = secret_code

    @property
    def user_code(self):
        return self._user_code

    @user_code.setter
    def user_code(self, user_code):
        if not isinstance(user_code, int) and (user_code<1000 and user_code>9999):
            raise Exception("The user code should be a valid 4 digit integer.")
        self._user_code = user_code

    @property
    def num_bulls(self):
        return self._num_bulls

    @num_bulls.setter
    def num_bulls(self, num_bulls):
        if num_bulls>len(self.secret_code):
            raise Exception("The bulls assigned value has crossed the max length of the secret code")
        self._num_bulls = num_bulls

    @property
    def num_cows(self):
        return self._num_cows

    @num_cows.setter
    def num_cows(self, num_cows):
        if num_bulls>len(self.secret_code):
            raise Exception("The cows assigned value has crossed the max length of the secret code")
        self._num_cows = num_cows

    
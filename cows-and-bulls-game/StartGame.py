from datetime import date

class StartGame:
    def __init__(self):
        self._user_name = None
    
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

    def welcomeMessage(self):
        print(f"Welcome to the Cows And Bulls Game.")
    
    def rules(self):
        print("Rules of the Game are:")
        print("1. Number of Bulls denote the exact matches of digit")
        print("2. Number of Cows denote the matches of digit but on the wrong place")

    def getUsername(self):
        return str(input()).capitalize()

    def setUsername(self):
        print("Please enter the name of the user: ",end="")
        self.user_name = self.getUsername()

    def greet(self):
        print(f"Time:#{date.today()}: Hello #{self.user_name}, The game is starting at #{date.today()}")
        
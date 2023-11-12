class PokemonTrainingGame:
    def __init__(self):
        self._powers = []
        self._user_choice = None
        self._min_power = 0
        self._max_power = 0
        self._itr = 0

    @property
    def powers(self):
        return self._powers

    @powers.setter
    def powers(self, power):
        if not isinstance(power, int):
            raise Exception("The entered power should only be an integer.")
        self.powers.append(power)

    @property
    def user_choice(self):
        return self._user_choice

    @user_choice.setter
    def user_choice(self, user_choice):
        if user_choice != "C" and user_choice != "E":
            raise Exception("The user_choice can only be either 'C' or 'E'")

        if user_choice == "C":
            self._user_choice = True
        else:
            self._user_choice = False

    @property
    def min_power(self):
        return self._min_power

    @min_power.setter
    def min_power(self, min_power):
        if not isinstance(min_power, int):
            raise Exception("The Minimum power being assigned is not an integer.")

        self._min_power = min_power

    @property
    def max_power(self):
        return self._max_power

    @max_power.setter
    def max_power(self, max_power):
        if not isinstance(max_power, int):
            raise Exception("The Minimum power being assigned is not an integer.")

        self._max_power = max_power

    @property
    def itr(self):
        return self._itr

    @itr.setter
    def itr(self, itr):
        self._itr = itr

    def calculateMinimumMaximumPower(self):        
        if self.min_power==0 and self.max_power==0 and len(self.powers)==1:
            self.min_power = self.powers[0]
            self.max_power = self.powers[0]
        else:
            print(self.itr)
            self.min_power= min(self.min_power, self.powers[self.itr])
            self.max_power= max(self.max_power, self.powers[self.itr])
        
        self.itr += 1

class PokemonTrainingGame:
    def __init__(self):
        self._powers = []
        self._min_power = None
        self._max_power = None

    @property
    def powers(self):
        return self._powers

    @powers.setter
    def powers(self, power):
        if not isinstance(power, int):
            raise Exception("The entered power should only be an integer.")
        self.powers.append(power)

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
        
class Flames:
    def __init__(self):
        self._first_user = None
        self._second_user = None
        self._flames_list = ["F","L","A","M","E","S"]
        self._count = 0

    @property
    def first_user(self):
        return self._first_user

    @first_user.setter
    def first_user(self, first_user):
        if not isinstance(first_user, str):
            raise Exception("The entered value should only be a string")

        self._first_user = first_user.lower()

    @property
    def second_user(self):
        return self._second_user

    @second_user.setter
    def second_user(self, second_user):
        if not isinstance(second_user, str):
            raise Exception("The entered value should only be a string")

        self._second_user = second_user.lower()
    
    @property
    def flames_list(self):
        return self._flames_list

    @flames_list.setter
    def flames_list(self, flames_list):
        if not isinstance(flames_list, list):
            return Exception("The assgining variable is not a list.")
        self._flames_list = flames_list    

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    def calculateCount(self):
        second_user_list = list(self.second_user)
        for element in self.first_user:
            if element in second_user_list:
                self.count += 2
                second_user_list.pop(second_user_list.index(element))
        self.count = len(self.first_user) + len(self.second_user) - self.count

    def mapListElementWithString(self):
        if self.flames_list[0] == "F":
            print("Friends")
        if self.flames_list[0] == "L":
            print("Lovers")
        if self.flames_list[0] == "A":
            print("Affectionate")
        if self.flames_list[0] == "M":
            print("Marriage")
        if self.flames_list[0] == "E":
            print("Enemies")
        if self.flames_list[0] == "S":
            print("Siblings")

    def calculateFlames(self):
        self.calculateCount()

        while not len(self.flames_list)==1:
            self.flames_list.pop(int(self.count%len(self.flames_list)))

        self.mapListElementWithString()
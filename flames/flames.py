class Flames:
    def __init__(self):
        self._first_user = None
        self._second_user = None
        self._flames_list = ["F","L","A","M","E"]

    @property
    def first_user(self):
        return self._first_user

    @first_user.setter
    def first_user(self, first_user):
        if not isinstance(first_user, str):
            raise Exception("The entered value should only be a string")

        self._first_user = first_user

    @property
    def second_user(self):
        return self._second_user

    @second_user.setter
    def second_user(self, second_user):
        if not isinstance(second_user, str):
            raise Exception("The entered value should only be a string")

        self._second_user = second_user
    
    @property
    def flames_list(self):
        return self._flames_list

    @flames_list.setter
    def flames_list(self, flames_list):
        if not isinstance(flames_list, list):
            return Exception("The assgining variable is not a list.")
        self._flames_list = flames_list    

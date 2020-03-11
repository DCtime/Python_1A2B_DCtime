from Entity import Entity


class Player(Entity):

    def __init__(self, name):
        # __name : str
        # the players name
        self.__name = name

        # __ans : str
        # stores the answer player inputs
        self.__ans = None

        print(self.__name, "Entered the game")

    def guess(self):
        """ player guessing , returns the player input(str) """
        self.__ans = input()
        return self.__ans

    # getter and setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

from Entity import Entity


class Player(Entity):

    def __init__(self, name):
        self.__name = name
        self.__ans = None
        print(self.__name, "Entered the game")

    def guess(self):
        self.__ans = input()
        return self.__ans


    # getter and setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

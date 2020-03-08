from Entity import Entity
import random


class Robot(Entity):
    def __init__(self, name):
        self.__name = name
        self.__ans = None

    def guess(self):
        """ return a random num with correct format """
        while 1:
            self.__ans = random.randint(1000, 9999)
            self.__ans = str(self.__ans)
            if len(set(self.__ans)) == 4:
                if self.__ans[0] != 0:
                    break
        return self.__ans

    # getter and setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

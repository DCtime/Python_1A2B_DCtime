from Entity import Entity
import random
import time


class Robot(Entity):
    def __init__(self, name):
        # __name : str
        # the robots name
        self.__name = name

        # __ans : str
        # stores the answer robot summons
        self.__ans = None

        print("Robot:", self.__name, "Entered the game")

    def guess(self):
        """ return a random num with correct format """
        while 1:
            self.__ans = random.randint(1000, 9999)
            self.__ans = str(self.__ans)
            if len(set(self.__ans)) == 4:
                if self.__ans[0] != 0:
                    break
        time.sleep(random.randint(1, 2))
        print(self.__ans)
        time.sleep(random.randint(1, 2))
        return self.__ans

    # getter and setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

import random
import time


class GuessNumber:
    def __init__(self):
        # __question : str
        # store the question which make_question makes
        self.__question = None

        # __a : int
        # store the current players a's
        self.__a = None

        # __b : int
        # store the current players b's
        self.__b = None

        # __history_dict : str & list : int ([A ,B])
        # stores player guessing history
        self.__history_dict = {}

    def make_question(self):
        """ return a question for 1A2B """
        # check the question if its the right format:
        # the numbers can not repeat, and the first number can not be zero
        while 1:
            self.__question = random.randint(1000, 9999)
            self.__question = str(self.__question)
            if len(set(self.__question)) == 4:
                if self.__question[0] != 0:
                    break
        print("Question Ready")
        print("del:", self.__question)   # for debug, show the answer of the round
        return self.__question

    def check_ans(self, ans):
        """ print things, and change the __a's and __b's value """
        # when tap 'h', show guess history
        if ans == 'h':
            self.show_history()
            return 0

        # check format
        if len(set(ans)) != 4 or ans[0] == '0':
            print("Format Wrong")
            time.sleep(random.randint(1, 2))
            return 0

        # set A,B to 0
        self.__a = 0
        self.__b = 0

        # check A's
        for i in range(0, 3 + 1):
            if ans[i] == str(self.__question[i]):
                self.__a += 1
                self.__b -= 1  # when A, B doesnt count

        # check B's
        for i in set(ans):
            if i in set(self.__question):
                self.__b += 1

        print("----- [", self.__a, "A", self.__b, "B", "] -----")
        print()

        # place it into history dic
        self.__history_dict[ans] = [self.__a, self.__b]

        time.sleep(random.randint(1, 2))

    def show_history(self):
        print()
        print(">>>>> Guess history <<<<<")
        for key, value in self.__history_dict.items():
            print("      ", end='')
            print(key, " -> ", value[0], "A", value[1], "B", sep='')
        print()
        time.sleep(random.randint(1, 2))

    # getter and setter
    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

    def get_b(self):
        return self.__b

    def set_b(self, b):
        self.__b = b




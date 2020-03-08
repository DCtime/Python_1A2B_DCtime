import random


class GuessNumber:
    def __init__(self):
        self.__question = None
        self.__a = None
        self.__b = None

    def make_question(self):
        while 1:
            self.__question = random.randint(1000, 9999)
            self.__question = str(self.__question)
            if len(set(self.__question)) == 4:
                if self.__question[0] != 0:
                    break
        print("Question Ready")
        print("del:", self.__question)
        return self.__question

    def check_ans(self, ans):

        # check format
        if len(set(ans)) != 4 or ans[0] == 0:
            print("Format Wrong")
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

        print("format: Okay")
        print("----- [", self.__a, "A", self.__b, "B", "] -----")

    # getter and setter
    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

    def get_b(self):
        return self.__b

    def set_b(self, b):
        self.__b = b




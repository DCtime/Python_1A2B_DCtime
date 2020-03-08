from GuessNumber import GuessNumber
import random


class Game:

    def __init__(self, *players):
        self.guess = GuessNumber()
        self.__players = []
        self.__current = None

        for i in players:
            self.__players.append(i)
            print(i.get_name(), "Joined the Game")

    def start(self):
        # make question
        print("making question...")
        self.guess.make_question()

        # start
        while 1:
            # switch player
            self.next_player()
            print("Now Guessing")
            print(self.__players[self.__current].get_name())

            # guessing, check_ans
            print("Enter your answer:", end='')
            while self.guess.check_ans(self.__players[self.__current].guess()) == 0:  # if the format is wrong, None
                print("Enter your answer:", end='')

            # check win
            if self.guess.get_a() == 4:
                self.end()
                break

    def next_player(self):
        if self.__current is None:
            random.shuffle(self.__players)
            self.__current = random.randint(0, len(self.__players) - 1)  # start at 0

        else:
            self.__current += 1
            if self.__current == len(self.__players):
                self.__current = 0

    def end(self):
        print(self.__players[self.__current].get_name(), "Wins")
        print("Game Over")

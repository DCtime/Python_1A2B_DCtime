from GuessNumber import GuessNumber
import random
import time


class Game:
    show_join_counter = 0

    def __init__(self, players):
        self.guess = GuessNumber()
        self.__players = []
        self.__current = None
        self.__players = players

        for i in self.__players:
            print(i.get_name(), end='')

            Game.show_join_counter += 1

            if Game.show_join_counter != len(self.__players):
                print(", ", end='')

        print()

        print("Joined the game")
        print()
        time.sleep(random.randint(1, 2))

    def start(self):
        # make question
        print("making question...")
        self.guess.make_question()
        print()
        time.sleep(random.randint(1, 2))

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
        time.sleep(random.randint(1, 2))
        print("The Game will shut down in 5 sec")
        time.sleep(5)

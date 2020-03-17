from GuessNumber import GuessNumber
import random
import time


class Game:
    # show_join_counter : int (class method)
    # a variable to help adding commas
    show_join_counter = 0

    def __init__(self, players, robots):
        # guess : obj
        # a object for using methods in GuessNumber class
        self.guess = GuessNumber()

        # __players : list
        # store players object
        self.__players = players

        # __robots : list
        # store robots object
        self.__robots = robots

        # __entities : list
        # store players and robots object
        self.__entities = players
        self.__entities.extend(robots)

        # __current : int
        # the index of __players list, stores the current guessing object
        self.__current = None

        # show players that joined the game
        for i in self.__entities:
            print(i.get_name(), end='')

            Game.show_join_counter += 1

            if Game.show_join_counter != len(self.__entities):
                print(", ", end='')

        print()
        print("Joined the game")
        print()

        # zeroing show_join_counter
        Game.show_join_counter = 0
        time.sleep(random.randint(1, 2))

    def start(self):
        """ return a question """
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
            print(self.__entities[self.__current].get_name())

            # guessing, check_ans
            print("Enter your answer (tap 'h' to show guessing history): ", end='')
            while self.guess.check_ans(self.__entities[self.__current].guess()) == 0:  # if the format is wrong, None
                print("Enter your answer (tap 'h' to show guessing history): ", end='')

            # check win
            if self.guess.get_a() == 4:
                self.end()
                break

    def next_player(self):
        """ switch player, changes the __current value """
        if self.__current is None:
            random.shuffle(self.__entities)
            self.__current = random.randint(0, len(self.__entities) - 1)  # start at 0

        else:
            self.__current += 1
            if self.__current == len(self.__entities):
                self.__current = 0

    def end(self):
        """ run this method when someone get 4A0B """
        print(self.__entities[self.__current].get_name(), "Wins")
        print("Game Over")
        time.sleep(random.randint(1, 2))


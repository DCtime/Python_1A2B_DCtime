from Game import Game
from Player import Player
from Robot import Robot
# INFINITE : int, final
# this number is so big that you can imagine
INFINITE = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# player_obj_list
# stores player objects
player_obj_list = []
# player_obj_list
# stores player objects
robot_obj_list = []
# game : object list
# store the game objects which program made during runtime
game = []
for j in range(0, INFINITE):
    print("Welcome playing")

    # player_quantity : int
    # the quantity of players
    player_quantity = int(input("How many players? "))
    print()

    # adding players
    print("Enter Names")

    for i in range(player_quantity):
        print(i+1, ".", sep='', end='')
        name = input()  # name : str, temporarily stores the name that user inputs
        obj = Player(name)  # obj : Player, temporarily stores the objects, ready to append to player_obj_list
        player_obj_list.append(obj)
    print()

    # deleting temporarily variables
    del name, obj

    # ask if wanna add robots into the game
    # ask_robot : str, temporarily
    # stores the answer of adding robot into this game
    ask_robot = input("Wanna add robot into this game? Enter 'y' to add, others no")

    if ask_robot == 'y':
        # robot_quantity : int
        # the quantity of robots
        robot_quantity = int(input("How many robots? "))
        print()

        # adding robots
        print("Enter Names")

        for i in range(player_quantity):
            print("Robot", i + 1, ".", sep='', end='')
            name = input()  # name : str, temporarily stores the name that user inputs
            obj = Robot(name)  # obj : Robot, temporarily stores the objects, ready to append to player_obj_list
            robot_obj_list.append(obj)
        print()

    # start the game
    game.append(Game(player_obj_list))
    game[j].start()

    print("Restart? Enter 'y' to restart, others to quit")
    # restart_decision : str, temporarily
    # if wanna restart, it will store y
    restart_decision = input()
    if restart_decision != 'y':
        break

    # start zeroing
    player_obj_list = []

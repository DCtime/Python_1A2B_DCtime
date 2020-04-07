from Game import Game
from Player import Player
from Robot import Robot

# player_obj_list
# stores player objects
player_obj_list = []
# player_obj_list
# stores player objects
robot_obj_list = []
# game : object list
# store the game objects which program made during runtime
game = []
# times : int
# stores how many times the game runs
times = 0

while 1:
    print("Welcome playing")

    while 1:
        try:
            # player_quantity : int
            # the quantity of players
            player_quantity = int(input("How many players? "))
        except ValueError:
            print("Don't Enter things that isn't an number, please enter it again.")
        else:
            break
    print()

    # adding players
    print("Enter Names")

    for i in range(player_quantity):
        print(i+1, ": ", sep='', end='')
        name = input()  # name : str, temporarily stores the name that user inputs
        obj = Player(name)  # obj : Player, temporarily stores the objects, ready to append to player_obj_list
        player_obj_list.append(obj)
    print()

    # deleting temporarily variables
    del name, obj

    # ask if wanna add robots into the game
    # ask_robot : str, temporarily
    # stores the answer of adding robot into this game
    ask_robot = input("Wanna add robot into this game? Enter 'y' to add, others no : ")

    if ask_robot == 'y':
        # robot_quantity : int
        # the quantity of robots
        while 1:
            try:
                robot_quantity = int(input("How many robots? "))
            except ValueError:
                print("Don't Enter things that isn't an number, please enter it again.")
            else:
                break
        print()

        # adding robots
        print("Enter Names")

        for i in range(robot_quantity):
            print("Robot ", i + 1, ": ", sep='', end='')
            name = input()  # name : str, temporarily stores the name that user inputs
            obj = Robot(name)  # obj : Robot, temporarily stores the objects, ready to append to player_obj_list
            robot_obj_list.append(obj)
        print()

    # start the game
    game.append(Game(player_obj_list, robot_obj_list))
    game[times].start()

    print("Restart? Enter 'y' to restart, others to quit")
    # restart_decision : str, temporarily
    # if wanna restart, it will store y
    restart_decision = input()
    if restart_decision != 'y':
        break

    # start zeroing
    player_obj_list = []
    robot_obj_list = []

    # add one to times because of starting a new game
    times += 1

from Game import Game
from Player import Player
# INFINITE : int, final
# this number is so big that you can imagine
INFINITE = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# player_obj_list
# stores player objects
player_obj_list = []
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

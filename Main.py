from Game import Game
from Player import Player

# player_obj_list
# stores player objects
player_obj_list = []


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

game = Game(player_obj_list)
game.start()

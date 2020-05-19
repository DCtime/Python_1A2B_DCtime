from Game import Game
from Player import Player
from Robot import Robot
import tkinter as tk
import tkinter.ttk as ttk
# players : tuple (global)
# stores the playing players
players = []
# robots : tuple (global)
# stores the playing robots
robots = []
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


def open_welcome_window():
    def close_welcome_window():
        welcome_window.destroy()
        open_enter_name_window()

    # FOR DEBUG: we are now opening welcome window
    print("Open : Opening Welcome window")

    """ Welcome window """
    # the start of the welcome window
    welcome_window = tk.Tk()
    welcome_window.title("Welcome")
    welcome_window.geometry("400x200")
    welcome_window.resizable(0, 0)  # can not modify the screen

    # making widgets for welcome window

    # label_game : Label object
    # shows "1A2B Game made by DCtime"
    label_game = tk.Label(
        welcome_window,
        text="1A2B Game",
        font="Helvetica 40 bold"
    )

    # label_author : Label object
    # shows "Made by DCtime"
    label_author = tk.Label(
        welcome_window,
        text="Made by DCtime",
        font="Helvetica 20",
    )

    # button_start
    # when pressed, close the welcome window and opens the add player window
    button_start = tk.Button(
        welcome_window,
        text="Start",
        font="Helvetica 15",
        command=close_welcome_window
    )

    # setting the location of the widgets
    label_game.pack()
    label_author.pack()
    button_start.pack(
        side="bottom",
        pady=30
    )

    # keep the window
    welcome_window.mainloop()


def open_enter_name_window():
    def close_enter_name_window():
        """ close the enter name window and store the players and the robots """
        list_players.selection_set(0, tk.END)
        global players
        players = list(list_players.get(0, tk.END))
        list_robots.selection_set(0, tk.END)
        global robots
        robots = list(list_robots.get(0, tk.END))
        enter_name_window.destroy()

    def add_player_name():
        player = entry_player_name.get()
        if len(player.strip()) == 0:
            return
        list_players.insert(tk.END, player)
        entry_player_name.delete(0, tk.END)

    def add_robot_name():
        robot = entry_robot_name.get()
        if len(robot.strip()) == 0:
            return
        list_robots.insert(tk.END, robot)
        entry_robot_name.delete(0, tk.END)

    def delete_player():
        player_index = list_players.curselection()
        if len(player_index) == 0:
            return
        list_players.delete(player_index)

    def delete_robot():
        robot_index = list_robots.curselection()
        if len(robot_index) == 0:
            return
        list_robots.delete(robot_index)

    # FOR DEBUG: we are now opening enter name window
    print("Open : Opening Enter name window")

    """ Enter name window """
    # the start of the enter name window
    enter_name_window = tk.Tk()
    enter_name_window.title("Enter names")
    enter_name_window.geometry("890x550")
    enter_name_window.resizable(0, 0)

    # ---- making widgets for open enter name window ----

    # label_player_name
    # shows "Adding players name"
    label_player_name = tk.Label(
        enter_name_window,
        text='Adding players name',
        font="Helvetica 20 bold"
    )

    # entry_player_name
    # enters player's name
    entry_player_name = tk.Entry(
        enter_name_window,
        font="Helvetica 20"
    )

    # button_add_player
    # adds player's name to the list
    button_add_player = tk.Button(
        enter_name_window,
        text="Add",
        font="Helvetica 20",
        command=add_player_name
    )

    # list_players
    # show the players
    list_players = tk.Listbox(
        enter_name_window,
        font="Helvetica 20"
    )

    # button_delete_player
    # delete selected player
    button_delete_player = tk.Button(
        enter_name_window,
        text="Delete Player",
        font="Helvetica 20",
        command=delete_player
    )

    # label_robot_name
    # shows "Adding robots name"
    label_robot_name = tk.Label(
        enter_name_window,
        text='Adding robots name',
        font="Helvetica 20 bold"
    )

    # entry_robot_name
    # enters robot's name
    entry_robot_name = tk.Entry(
        enter_name_window,
        font="Helvetica 20"
    )

    # button_add_robot
    # adds robot's name to the list
    button_add_robot = tk.Button(
        enter_name_window,
        text="Add",
        font="Helvetica 20",
        command=add_robot_name
    )

    # list_robots
    # show the robots
    list_robots = tk.Listbox(
        enter_name_window,
        font="Helvetica 20"
    )

    # button_delete_robot
    # delete selected robot
    button_delete_robot = tk.Button(
        enter_name_window,
        text="Delete Robot",
        font="Helvetica 20",
        command=delete_robot
    )

    # label_separate
    # separate the two entries
    separater_list = ttk.Separator(
        enter_name_window
    )

    # button_next
    # go to next page
    button_next = tk.Button(
        enter_name_window,
        text="Next",
        font="Helvetica 20",
        command=close_enter_name_window
    )

    # ---- setting locations ----
    label_player_name.grid(row=0, column=0, columnspan=2, padx=5)
    entry_player_name.grid(row=1, column=0, sticky='w', padx=10)
    button_add_player.grid(row=1, column=1, padx=5)
    list_players.grid(row=2, column=0, columnspan=2, sticky='w' + 'e' + 's', padx=10)
    button_delete_player.grid(row=3, column=0, columnspan=2)
    label_robot_name.grid(row=0, column=3, columnspan=2)
    entry_robot_name.grid(row=1, column=3, sticky='w')
    button_add_robot.grid(row=1, column=4, padx=5)
    list_robots.grid(row=2, column=3, columnspan=2, sticky='w' + 'e' + 's')
    button_delete_robot.grid(row=3, column=2, columnspan=2, sticky='e')
    separater_list.grid(row=0, column=2, rowspan=4, padx=5)
    button_next.grid(row=4, column=2)


def open_playing_window():
    def close_enter_name_window():
        pass

    # FOR DEBUG: we are now opening enter name window
    print("Open : Opening Playing Window")

    """ Playing window """
    # the start of the enter name window
    playing_window = tk.Tk()
    playing_window.title("1A2B Game")
    playing_window.geometry("890x550")
    playing_window.resizable(0, 0)

    # ---- making widgets for open enter name window ----


while 1:
    open_welcome_window()
    print(players, robots)
    # making player obj
    for name in players:
        obj = Player(name)  # obj : Player, temporarily stores the objects, ready to append to player_obj_list
        player_obj_list.append(obj)

    # deleting temporarily variables
    del obj
    
    # making robot obj
    for name in robots:
        obj = Robot(name)  # obj : Robot, temporarily stores the objects, ready to append to player_obj_list
        robot_obj_list.append(obj)

    # deleting temporarily variables
    del obj
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

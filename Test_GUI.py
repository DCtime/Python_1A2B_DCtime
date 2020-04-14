import tkinter as tk


def open_welcome_window():
    # FOR DEBUG: we are now opening welcome window
    print("Open : Opening Welcome window")

    """ Welcome window """
    # the start of the welcome window
    global welcome_window
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

    # setting the situations of the widgets
    label_game.pack()
    label_author.pack()
    button_start.pack(
        side="bottom",
        pady=30
    )

    # keep the window
    welcome_window.mainloop()


def close_welcome_window():
    welcome_window.destroy()
    open_add_player_window()


def open_add_player_window():
    # FOR DEBUG : we are now opening add player window
    print("Open : Opening Add player window")

    """ add_player_window """
    global add_player_window
    add_player_window = tk.Tk()
    add_player_window.title("Add players")
    add_player_window.geometry("400x200")
    add_player_window.resizable(0, 0)

    # widgets in add_player_window

    # label_player_quantity : Label object
    # shows "Player's Quantity"
    label_player_quantity = tk.Label(
        add_player_window,
        text="Player's Quantity:",
        font="Helvetica 15 bold",
        relief='groove'
    )

    # entry_player_quantity : Entry object
    # enter player's quantity
    entry_player_quantity = tk.Entry(
        font="Helvetica 15"
    )

    # label_robot_quantity : Label object
    # shows "Robot's Quantity"
    label_robot_quantity = tk.Label(
        add_player_window,
        text="Robot's Quantity:",
        font="Helvetica 15 bold",
        relief='groove'
    )

    # packing widgets
    label_player_quantity.pack(
        anchor='nw',
        side='left'
    )

    entry_player_quantity.pack(
        anchor='nw',
        side='left'
    )

    label_robot_quantity.pack(
        
    )

    # keep the window
    add_player_window.mainloop()


""" >>> Showing the windows <<< """
open_welcome_window()

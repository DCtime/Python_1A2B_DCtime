import tkinter as tk

# the start of the welcome window
welcome_window = tk.Tk()
welcome_window.title("1A2B Game Made by DCtime")
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
    font="Helvetica 15"
)

label_game.pack()
label_author.pack()
button_start.pack(
    side="bottom",
    pady=30
)
welcome_window.mainloop()





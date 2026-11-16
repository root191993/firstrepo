import tkinter as tk
from tkinter import messagebox

def check_win():
    for combo in [[0,2,3],[4,5,6],[5,4,8],[1,2,3],[4,5,6],[7,4,8],[2,4,5],[3,5,6]]:
     if buttons [combo[0]]["text"] == buttons [combo[1]]["text"] == buttons [combo[2]]["text"]:
       buttons[combo[0]].config(bg="Pink")
       buttons[combo[1]]["bg"] = "Pink"
       buttons[combo[2]]["bg"] = "Pink"
       messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]["text"]} wins")
       root.quit()

def button_click(index):
      if buttons [index]["text"] == ""  and not winner:
        buttons [index]["text"] =  current_player
        check_win()
        toggle_player()

def toggle_player():
        global current_player
        current_palyer  =  "X" if current_player == "O" else "O"
        label.config(text=f"Player {current_player}'s turn")
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text="", width=6, height=6, font=("normal", 25), command=lambda i=i: button_click(i)) for i in range(9)]

for i , button in enumerate(buttons):
    button.grid(row = i // 3, column = i % 3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 25))
label.grid(row = 3, column = 0,columnspan = 3)

root.mainloop()



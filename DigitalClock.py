import tkinter as tk
from time import strftime



root = tk.Tk()
root.title("Wall Clock")
root.geometry("400x400")
def time():
    string = strftime("%H:%M:%S %d/%m/%Y")
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=("Calibri",40),bg="yellow",fg="black")
label.pack(anchor="nw")

time()

root.mainloop()


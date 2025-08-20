
from tkinter import *

def update():
    print("Updating the GUI")
    root.geometry(f"{width_var.get()}x{height_var.get()}")

root = Tk()
root.title("Update Example")
root.geometry("300x200")

# Variables
width_var = StringVar()
height_var = StringVar()

# Width label + entry
Label(root, text="Width:").grid(row=0, column=0, padx=10, pady=5)
Entry(root, textvariable=width_var).grid(row=0, column=1, padx=10, pady=5)

# Height label + entry
Label(root, text="Height").grid(row=1, column=0, padx=10, pady=5)
Entry(root, textvariable=height_var).grid(row=1, column=1, padx=10, pady=5)

# Button
Button(root, text="Update", command=update).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
# This code creates a simple GUI application using Tkinter that allows the user to update the window size.
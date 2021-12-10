import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Calculator')
root.geometry('450x500')

frame1 = tk.Frame(root, height=50, width=50)
frame1.pack(expand=True, side="bottom", fill="both")

frame2 = tk.Frame(root, height=50, width=50)
frame2.pack(side="bottom", expand=True, fill="both")

frame3 = tk.Frame(root, height=50, width=50)
frame3.pack(side="bottom", fill="both", expand=True)

button_add = tk.Button(frame1, text="+", height=3, width=14)
button_add.pack(side="right", fill="both", padx=2, pady=2)

button_subtract = tk.Button(frame2, text="-", height=3, width=14)
button_subtract.pack(side="right", fill="both", padx=2, pady=2)

button_multiply = tk.Button(frame3, text="*", height=3, width=14)
button_multiply.pack(side="right", fill="both", padx=2, pady=2)

nine = tk.Button(frame3, text="9", height=3, width=14)
nine.pack(side="right", fill="both", padx=2, pady=2)

eight = tk.Button(frame3, text="8", height=3, width=14)
eight.pack(side="right", fill="both", padx=2, pady=2)

seven = tk.Button(frame3, text="7", height=3, width=14)
seven.pack(side="right", fill="both", padx=2, pady=2)

six = tk.Button(frame2, text="6", height=3, width=14)
six.pack(side="right", fill="both", padx=2, pady=2)

five = tk.Button(frame2, text="5", height=3, width=14)
five.pack(side="right", fill="both", padx=2, pady=2)

four = tk.Button(frame2, text="4", height=3, width=14)
four.pack(side="right", fill="both", padx=2, pady=2)

three = tk.Button(frame1, text="3", height=3, width=14)
three.pack(side="right", fill="both", padx=2, pady=2)

two = tk.Button(frame1, text="2", height=3, width=14)
two.pack(side="right", fill="both", padx=2, pady=2)

one = tk.Button(frame1, text="1", height=3, width=14)
one.pack(side="right", fill="both", padx=2, pady=2)

root.mainloop()

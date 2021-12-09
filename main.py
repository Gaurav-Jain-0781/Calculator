import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Calculator')

frame1 = tk.Frame(root, height=50, width=50)
frame1.pack()

button1 = tk.Button(frame1, text="1", height=3, width=7)
button1.pack(side="left")

button3 = tk.Button(frame1, text="3", height=3, width=7)
button3.pack(side="right")

button2 = tk.Button(frame1, text="2", height=3, width=7)
button2.pack(side="right")

frame2 = tk.Frame(root, height=50, width=50)
frame2.pack()

button4 = tk.Button(frame2, text="4", height=3, width=7)
button4.pack(side="left")

button6 = tk.Button(frame2, text="6", height=3, width=7)
button6.pack(side="right")

button5 = tk.Button(frame2, text="5", height=3, width=7)
button5.pack(side="right")

frame3 = tk.Frame(root, height=50, width=50)
frame3.pack()

button7 = tk.Button(frame3, text="7", height=3, width=7)
button7.pack(side="left")

button9 = tk.Button(frame3, text="9", height=3, width=7)
button9.pack(side="right")

button8 = tk.Button(frame3, text="8", height=3, width=7)
button8.pack(side="right")

root.mainloop()
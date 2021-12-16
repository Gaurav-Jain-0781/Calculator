import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('450x500')

entry = tk.Entry(root, justify="right")
entry.pack(side="top", padx=4, pady=2, fill="both", ipady=35)

frame4 = tk.Frame(root, height=50, width=50)
frame4.pack(side="bottom", expand=True, fill="both")

frame1 = tk.Frame(root, height=50, width=50)
frame1.pack(expand=True, side="bottom", fill="both")

frame2 = tk.Frame(root, height=50, width=50)
frame2.pack(side="bottom", expand=True, fill="both")

frame3 = tk.Frame(root, height=50, width=50)
frame3.pack(side="bottom", fill="both", expand=True)

frame5 = tk.Frame(root, height=50, width=50)
frame5.pack(side="bottom", fill="both", expand=True)

button_add = tk.Button(frame1, text="+", height=3, width=14)
button_add.pack(side="right", fill="both", padx=2, pady=2, expand=True)

button_subtract = tk.Button(frame2, text="-", height=3, width=14)
button_subtract.pack(side="right", fill="both", padx=2, pady=2, expand=True)

button_multiply = tk.Button(frame3, text="*", height=3, width=14)
button_multiply.pack(side="right", fill="both", padx=2, pady=2, expand=True)

nine = tk.Button(frame3, text="9", height=3, width=14)
nine.pack(side="right", fill="both", padx=2, pady=2, expand=True)

eight = tk.Button(frame3, text="8", height=3, width=14)
eight.pack(side="right", fill="both", padx=2, pady=2, expand=True)

seven = tk.Button(frame3, text="7", height=3, width=14)
seven.pack(side="right", fill="both", padx=2, pady=2, expand=True)

six = tk.Button(frame2, text="6", height=3, width=14)
six.pack(side="right", fill="both", padx=2, pady=2, expand=True)

five = tk.Button(frame2, text="5", height=3, width=14)
five.pack(side="right", fill="both", padx=2, pady=2, expand=True)

four = tk.Button(frame2, text="4", height=3, width=14)
four.pack(side="right", fill="both", padx=2, pady=2, expand=True)

three = tk.Button(frame1, text="3", height=3, width=14)
three.pack(side="right", fill="both", padx=2, pady=2, expand=True)

two = tk.Button(frame1, text="2", height=3, width=14)
two.pack(side="right", fill="both", padx=2, pady=2, expand=True)

one = tk.Button(frame1, text="1", height=3, width=14)
one.pack(side="right", fill="both", padx=2, pady=2, expand=True)

equals_to = tk.Button(frame4, text="=", height=3, width=14)
equals_to.pack(side="right", fill="both", padx=2, pady=2, expand=True)

point = tk.Button(frame4, text=".", height=3, width=14)
point.pack(side="right", fill="both", padx=2, pady=2, expand=True)

zero = tk.Button(frame4, text="0", height=3, width=14)
zero.pack(side="right", fill="both", padx=2, pady=2, expand=True)

negative = tk.Button(frame4, text="+/-", height=3, width=14)
negative.pack(side="right", fill="both", padx=2, pady=2, expand=True)

percentage = tk.Button(frame5, text="%", height="3", width="14")
percentage.pack(side="right", padx=2, pady=2, fill="both", expand=True)

divide = tk.Button(frame5, text="/", height=3, width=14)
divide.pack(side="right", padx="2", pady="2", fill="both", expand=True)

clear_entry = tk.Button(frame5, text="CE", height=3, width=14)
clear_entry.pack(side="right", padx=2, pady=2, fill="both", expand=True)

clear_all = tk.Button(frame5, text="C", height=3, width=14)
clear_all.pack(side="right", padx=2, pady=2, fill="both", expand=True)

root.mainloop()

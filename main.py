import tkinter as tk
import re
import tkinter.font as font


def operate():
    data = entry.get()
    pattern = re.search("([0-9,.]*)([\W])([0-9]*)([\W]?)", data)
    first_value = pattern[1]
    operator = pattern[2]
    second_value = pattern[3]
    special_operator = pattern[4]
    result(first_value, operator, second_value, special_operator)


def result(first_value, operator, second_value, so):
    fv = float(first_value)
    sv = float(second_value)
    operator_type = operator
    second_time_operator = so
    entry.delete(0, "end")
    result_displayed = 0
    if second_time_operator:
        to_be_multiplied_with = sv / 100
        result_displayed = fv * to_be_multiplied_with
    else:
        if operator_type == "+":
            result_displayed = fv + sv
        elif operator_type == "-":
            result_displayed = fv - sv
        elif operator_type == "*":
            result_displayed = fv * sv
        else:
            result_displayed = fv / sv
    entry.insert(0, result_displayed)


def delete_last_entry():
    data = entry.get()
    data_list = []
    for d in data:
        data_list.append(d)
    entry.delete(len(data_list)-1, "end")


def delete_all():
    entry.delete(0, "end")


def display_entry(value):
    print(value)
    if value == "minus":
        entry.insert(0, "-")
    else:
        entry.insert("end", value)


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

button_add = tk.Button(frame1, text="+", height=3, width=14, command=lambda: display_entry("+"))
button_add.pack(side="right", fill="both", padx=2, pady=2, expand=True)

button_subtract = tk.Button(frame2, text="-", height=3, width=14, command=lambda: display_entry("-"))
button_subtract.pack(side="right", fill="both", padx=2, pady=2, expand=True)

button_multiply = tk.Button(frame3, text="*", height=3, width=14, command=lambda: display_entry("*"))
button_multiply.pack(side="right", fill="both", padx=2, pady=2, expand=True)

percentage = tk.Button(frame5, text="%", height="3", width="14", command=lambda: display_entry("%"))
percentage.pack(side="right", padx=2, pady=2, fill="both", expand=True)

divide = tk.Button(frame5, text="/", height=3, width=14, command=lambda: display_entry("/"))
divide.pack(side="right", padx="2", pady="2", fill="both", expand=True)

nine = tk.Button(frame3, text="9", height=3, width=14, command=lambda: display_entry(9))
nine.pack(side="right", fill="both", padx=2, pady=2, expand=True)

eight = tk.Button(frame3, text="8", height=3, width=14, command=lambda: display_entry(8))
eight.pack(side="right", fill="both", padx=2, pady=2, expand=True)

seven = tk.Button(frame3, text="7", height=3, width=14, command=lambda: display_entry(7))
seven.pack(side="right", fill="both", padx=2, pady=2, expand=True)

six = tk.Button(frame2, text="6", height=3, width=14, command=lambda: display_entry(6))
six.pack(side="right", fill="both", padx=2, pady=2, expand=True)

five = tk.Button(frame2, text="5", height=3, width=14, command=lambda: display_entry(5))
five.pack(side="right", fill="both", padx=2, pady=2, expand=True)

four = tk.Button(frame2, text="4", height=3, width=14, command=lambda: display_entry(4))
four.pack(side="right", fill="both", padx=2, pady=2, expand=True)

three = tk.Button(frame1, text="3", height=3, width=14, command=lambda: display_entry(3))
three.pack(side="right", fill="both", padx=2, pady=2, expand=True)

two = tk.Button(frame1, text="2", height=3, width=14, command=lambda: display_entry(2))
two.pack(side="right", fill="both", padx=2, pady=2, expand=True)

one = tk.Button(frame1, text="1", height=3, width=14, command=lambda: display_entry(1))
one.pack(side="right", fill="both", padx=2, pady=2, expand=True)

equals_to = tk.Button(frame4, text="=", height=3, width=14, command=lambda: operate())
equals_to.pack(side="right", fill="both", padx=2, pady=2, expand=True)

point = tk.Button(frame4, text=".", height=3, width=14, command=lambda: display_entry("."))
point.pack(side="right", fill="both", padx=2, pady=2, expand=True)

zero = tk.Button(frame4, text="0", height=3, width=14, command=lambda: display_entry(0))
zero.pack(side="right", fill="both", padx=2, pady=2, expand=True)

negative = tk.Button(frame4, text="+/-", height=3, width=14, command=lambda: display_entry("minus"))
negative.pack(side="right", fill="both", padx=2, pady=2, expand=True)

clear_entry = tk.Button(frame5, text="CE", height=3, width=14, command=lambda: delete_last_entry())
clear_entry.pack(side="right", padx=2, pady=2, fill="both", expand=True)

clear_all = tk.Button(frame5, text="C", height=3, width=14, command=lambda: delete_all())
clear_all.pack(side="right", padx=2, pady=2, fill="both", expand=True)


root.mainloop()

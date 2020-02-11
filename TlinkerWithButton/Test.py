from tkinter import *

root = Tk()

# Initialise items
num = 0
buttons = []
buttons_string = StringVar()


# My button function
def buttons_selection(a):
    print(a)
    buttons[a][1].set(a)


# Buttons is a 2d list where I store the button and it's text variable in
for i in range(9):
    buttons.append([])
    buttons[i].append(0)
    buttons[i].append(buttons_string)

# These for loops create the buttons
for x in range(3):
    for y in range(3):
        buttons[num][0] = Button(root, command=lambda a=num: buttons_selection(a),
                                 textvariable=buttons[num][1],  height=2, width=5) .grid(row=y, column=x)
        num += 1

root.mainloop()
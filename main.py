# importing tkinter
from tkinter import *

# color definition
color1 = "#3b3b3b" # black
color2 = "#feffff" # white
color3 = "#5c889c" # blue
color4 = "#eceff1" # gray
color5 = "#112342" # orange

# creating new window and setting its size
window = Tk()
window.title("Simple Calculator")
window.geometry("310x340")
window.config(bg=color1)

# frames
displayFrame = Frame(window, width=310, height=50, bg=color3)
displayFrame.grid(row=0, column=0)

bodyFrame = Frame(window, width=310, height=340)
bodyFrame.grid(row=1, column=0)

# init variable
allValues = ""
result = ""
textValue = StringVar()

# functions
def displayValue(event):
    global allValues, result
    allValues = allValues + str(event)
    textValue.set(allValues)
  
def calculate():
    global allValues, result
    result = str(eval(allValues))
    allValues = result
    textValue.set(result)


def flush():
    global allValues, result, equalsFlag
    allValues = ""
    result = ""
    equalsFlag = 0
    textValue.set(allValues)

# label
appLabel = Label(displayFrame, textvariable=textValue, text="", width=20, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=color3, fg=color2)
appLabel.place(x=0, y=0)

# buttons
b_1 = Button(bodyFrame, command= lambda:flush(), text="C", width=12, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(bodyFrame, command= lambda:displayValue("%"), text="%", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=150, y=0)
b_3 = Button(bodyFrame, command= lambda:displayValue("/"), text="/", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=220, y=0)

b_4 = Button(bodyFrame, command= lambda:displayValue("7"), text="7", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=57)
b_5 = Button(bodyFrame, command= lambda:displayValue("8"), text="8", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=75, y=57)
b_6 = Button(bodyFrame, command= lambda:displayValue("9"), text="9", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=150, y=57)
b_7 = Button(bodyFrame, command= lambda:displayValue("*"), text="*", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=220, y=57)

b_8 = Button(bodyFrame, command= lambda:displayValue("4"), text="4", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=114)
b_9 = Button(bodyFrame, command= lambda:displayValue("5"), text="5", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=75, y=114)
b_10 = Button(bodyFrame, command= lambda:displayValue("6"), text="6", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=150, y=114)
b_11 = Button(bodyFrame, command= lambda:displayValue("-"), text="-", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=220, y=114)

b_12 = Button(bodyFrame, command= lambda:displayValue("1"), text="1", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=171)
b_13 = Button(bodyFrame, command= lambda:displayValue("2"), text="2", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=75, y=171)
b_14 = Button(bodyFrame, command= lambda:displayValue("3"), text="3", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=150, y=171)
b_15 = Button(bodyFrame, command= lambda:displayValue("+"), text="+", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=220, y=171)

b_16 = Button(bodyFrame, command= lambda:displayValue("0"), text="0", width=12, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=228)
b_17 = Button(bodyFrame, command= lambda:displayValue("."), text=".", width=5, height=2, bg=color4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=150, y=228)
b_18 = Button(bodyFrame, command= lambda:calculate(), text="=", width=5, height=2, bg=color5, fg=color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=220, y=228)

window.mainloop()


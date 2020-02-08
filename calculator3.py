# use loopsss
from tkinter import *
from math import *

def btnLog(numbers):
    global operator
    operator = operator + btnLog(numbers)
    text_Input.set(operator)



def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




cal = Tk()
cal.title("The Bryann Calculator")
operator = ""
text_Input = StringVar()

cal.resizable(width=False, height=False)


txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify="right").grid(columnspan=4)


# row 1
btn7 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="7", bg="powder blue", command=lambda:btnClick(7)).grid(row=1, column=0)

btn8 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="8", bg="powder blue", command=lambda:btnClick(8)).grid(row=1, column=1)

btn9 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="9", bg="powder blue", command=lambda:btnClick(9)).grid(row=1, column=2)

Addition = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="+", bg="powder blue", command=lambda:btnClick("+")).grid(row=1, column=3)



# row 2
btn4 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="4", bg="powder blue", command=lambda:btnClick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="5", bg="powder blue", command=lambda:btnClick(5)).grid(row=2, column=1)

btn6 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="6", bg="powder blue", command=lambda:btnClick(6)).grid(row=2, column=2)

Subtraction = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="-", bg="powder blue", command=lambda:btnClick("-")).grid(row=2, column=3)



# row 3
btn1 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="1", bg="powder blue", command=lambda:btnClick(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="2", bg="powder blue", command=lambda:btnClick(2)).grid(row=3, column=1)

btn3 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
        text="3", bg="powder blue", command=lambda:btnClick(3)).grid(row=3, column=2)

Multiply = Button(cal, padx=16, bd=8, fg="black", width=2, font=("arial", 20, "bold"),
            text="*", bg="powder blue", command=lambda:btnClick("*")).grid(row=3, column=3)



# row 4
btn0 = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
            text="0", bg="powder blue", command=lambda:btnClick(0)).grid(row=4, column=0)

btnClear = Button(cal, padx=16, bd=8, fg="black", width=2,font=("arial", 20, "bold"),
            text="C", bg="powder blue", command=btnClearDisplay).grid(row=4, column=1)

btnSin = Button(cal, padx=16, bd=8, fg="black", width=2, font=("arial", 20, "bold"),
            text="^2", bg="powder blue", command=lambda:btnClick("**2")).grid(row=4, column=2)

Division = Button(cal, padx=16, bd=8, fg="black", width=2,font=("arial", 20, "bold"),
            text="/", bg="powder blue", command=lambda:btnClick("/")).grid(row=4, column=3)


# row 4
btnDot = Button(cal, padx=16, bd=8, fg="black", width=2, font=("arial", 20, "bold"),
            text=".", bg="powder blue", command=lambda:btnClick(".")).grid(row=5, column=0)

btnPercentage = Button(cal, padx=16, bd=8, fg="black", width=2,font=("arial", 20, "bold"),
            text="%", bg="powder blue", command=lambda:btnClick("/100")).grid(row=5, column=1)

btnLog = Button(cal, padx=16, bd=8, fg="black", width=2,font=("arial", 20, "bold"),
            text="log", bg="powder blue", command=lambda:btnClick("log")).grid(row=5, column=2)

btnEqual = Button(cal, padx=16, bd=8, fg="black",width=2, font=("arial", 20, "bold"),
        text="=", bg="powder blue", command=btnEqualsInput).grid(row=5, column=3)


def donothing():
    filewin = Toplevel(cal)
    button = Button(filewin, text="Do nothing button")
    button.pack()



menubar = Menu(cal)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()


filemenu.add_command(label="Exit", command=cal.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)


menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", command=donothing)

cal.config(menu=menubar)





cal.mainloop()
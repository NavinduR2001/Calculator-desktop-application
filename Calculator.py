from tkinter import *

# Create the main window
win = Tk()
win.title("Simple Calculator")
win.geometry("400x400")
win.resizable(0, 0)

expression=""
input_text=StringVar()


# Function to update expression in the input field
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def clear():
    global expression
    expression = ""
    input_text.set("")

def result():
    global expression
    try:
        total = str(eval(expression))
        input_text.set(total)
        expression = ""
    except:
        input_text.set(" error ")
        expression = ""



#input field
input_frame = Frame(win, width=400, height=50, bg="#e8e9eb")
input_frame.pack(side=TOP , fill=X)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=50, bd=5, justify=RIGHT, relief=FLAT, textvariable=input_text, show="")
input_field.pack(fill=X, padx=3, pady=6, ipady=10)

#button frame
button_frame= Frame(win, width=400, height=350, bg="#e8e9eb")
button_frame.pack(side=TOP, fill=BOTH, expand=True)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

clear = Button(button_frame, text="C", width=32, height=3, bd=0, bg="#BBBBBB", cursor="hand2" , command=clear)
clear.grid(row=0, column=0, columnspan=3 , padx=3, pady=3, sticky="nsew")

divide = Button(button_frame, text="/", width=10, height=3, bd=0, bg="#BBBBBB", cursor="hand2" , command= lambda:btn_click("/"))
divide.grid(row=0, column=3, padx=3, pady=3, sticky="nsew")

#Buttons
btn7 = Button(button_frame, text="7", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(7))
btn7.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

btn8 = Button(button_frame, text="8", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(8))
btn8.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")

btn9 = Button(button_frame, text="9", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(9))
btn9.grid(row=1, column=2, padx=3, pady=3, sticky="nsew")

multiply = Button(button_frame, text="*", width=10, height=3, bd=0, bg="#BBBBBB", cursor="hand2" , command= lambda:btn_click("*"))
multiply.grid(row=1, column=3, padx=3, pady=3, sticky="nsew")

btn4 = Button(button_frame, text="4", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(4))
btn4.grid(row=2, column=0, padx=3, pady=3, sticky="nsew")

btn5 = Button(button_frame, text="5", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(5))
btn5.grid(row=2, column=1, padx=3, pady=3, sticky="nsew")

btn6 = Button(button_frame, text="6", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(6))
btn6.grid(row=2, column=2, padx=3, pady=3, sticky="nsew")

subtract = Button(button_frame, text="-", width=10, height=3, bd=0, bg="#BBBBBB", cursor="hand2" , command= lambda:btn_click("-"))
subtract.grid(row=2, column=3, padx=3, pady=3, sticky="nsew")

btn1 = Button(button_frame, text="1", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(1))
btn1.grid(row=3, column=0, padx=3, pady=3, sticky="nsew")

btn2 = Button(button_frame, text="2", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(2))
btn2.grid(row=3, column=1, padx=3, pady=3, sticky="nsew")

btn3 = Button(button_frame, text="3", width=10, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(3))
btn3.grid(row=3, column=2, padx=3, pady=3, sticky="nsew")

add = Button(button_frame, text="+", width=10, height=3, bd=0, bg="#BBBBBB", cursor="hand2" , command= lambda:btn_click("+"))
add.grid(row=3, column=3, padx=3, pady=3, sticky="nsew")

btn0 = Button(button_frame, text="0", width=21, height=3, bd=0, bg="#fff", cursor="hand2" , command= lambda:btn_click(0))
btn0.grid(row=4, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")

decimal = Button(button_frame, text=".", width=10, height=3, bd=0, bg="#BBBBBB", cursor="hand2" , command= lambda:btn_click("."))
decimal.grid(row=4, column=2, padx=3, pady=3, sticky="nsew")

equals = Button(button_frame, text="=", width=10, height=3, bd=0, bg="#BBBBBB", cursor="hand2" , command=result)
equals.grid(row=4, column=3, padx=3, pady=3, sticky="nsew")

# Run the main loop

win.mainloop()
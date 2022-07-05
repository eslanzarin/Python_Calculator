from tkinter import*

cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify = 'right').grid(columnspan=4)

# FIRST ROW

btn7=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="powder blue").grid(row=1, column=0)

btn8=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="powder blue").grid(row=1, column=1)

btn9=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="powder blue").grid(row=1, column=2)

Addition=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg="powder blue").grid(row=1, column=3)

# SECOND ROW

btn4=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="powder blue").grid(row=2, column=0)

btn5=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="powder blue").grid(row=2, column=1)

btn6=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="powder blue").grid(row=2, column=2)

Subtraction=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg="powder blue").grid(row=2, column=3)

# THIRD ROW

btn1=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg="powder blue").grid(row=3, column=0)

btn2=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg="powder blue").grid(row=3, column=1)

btn3=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg="powder blue").grid(row=3, column=2)

Multiplication=Button (cal, padx=16,bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="powder blue").grid(row=3, column=3)

#FOURTH ROW


cal.mainloop()

'''
window = tk.Tk()
label = tk.Label(text="Python rocks!")
label.pack()
window.mainloop()

class Application:
    def __init__(self, master=None):
        pass
root = tk()
Application(root)
root.mainloop()
'''
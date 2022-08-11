from tkinter import *
from tkinter import ttk
Window = Tk()
Window.title("Currency Converter")

def test():
    test = ttk.Button(Window, text='yes')
    test.pack()

test = ttk.Button(Window, text='yes', command=test)
test.pack()
Window.mainloop()

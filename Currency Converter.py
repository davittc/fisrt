from tkinter import *
from tkinter import ttk
Window = Tk()
Window.title("Currency Converter")

#def to_lanuage_seletor():

#def to_currency_converter():

#def to_references():

def quit_button():
    quit()



def test():
    test = ttk.Button(Window, text='yes')
    test.pack()

quit_button = ttk.Button(Window, command=quit_button())
test = ttk.Button(Window, text='yes', command=test)
test.pack()
Window.mainloop()

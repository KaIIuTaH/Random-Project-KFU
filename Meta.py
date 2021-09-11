from tkinter import *


#functions


def dataswap():
    swapped = ent.get()
    ver = str(variation.get())
    lbl.configure(text=swapped)
    lbl2.configure(text=ver)

def varswap():
    variation = 1

variation = 0
#main
root = Tk()
root.title('Интерфейс Tkinter')
root.geometry('640x480')
lbl = Label(text='MainText', font='Arial 20')
lbl.pack()
ent = Entry(root, width='10')
ent.pack()
but = Button(text='Замена', command=dataswap)
but.pack()
checkbox_state = BooleanVar()
checkbox_state.set(False)
checkbox = Checkbutton(text='Я дебил.', var = checkbox_state)
checkbox.pack()
lbl2 = Label(text=variation)
lbl2.pack()
btn2 = Button(text='Замена значения', command = varswap)
btn2.pack()

root.mainloop()


from tkinter import *


#functions


def dataswap():         #функция, позволяющая менять значения
    swapped = ent.get() #получение данных с Ent
    ver = str(variation.get()) #получение данных с variation
    lbl.configure(text=swapped)
    lbl2.configure(text=ver)

def varswap(): #сомнительная замена значения variation на 1
    variation = 1

variation = 0 #зачем эту фигню я добавил?
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
checkbox_state.set(False) #изначальное состояние Checkbox
checkbox = Checkbutton(text='Я дебил.', var = checkbox_state)
checkbox.pack()
lbl2 = Label(text=variation)
lbl2.pack()
btn2 = Button(text='Замена значения', command = varswap)
btn2.pack()

root.mainloop()


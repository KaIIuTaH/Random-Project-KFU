import time
from tkinter import *


def upd():
    tm.configure(text=time.ctime(time.time()))


window = Tk()
window.title('TimeScript')
window.geometry('240x180') #задал геометрию и название окна

tm = Label(window, text = time.ctime(time.time()))
but_upd = Button(window, text = "/Update time/", bd='4', bg='beige', fg='grey', command = upd)
#сделал небольшое оформление кнопки


tm.pack()
but_upd.pack()

window.mainloop()

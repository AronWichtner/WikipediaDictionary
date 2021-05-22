from tkinter import *

window = Tk()

window.title("WIKI-DICTIONARY")
#window.geometry("900x500")
#window.resizable(height=False, width=False)

f1 = Frame(window, width=900, height=100, bg="red").grid(column=0, row=0)
l1 = Label(mater=f1, text="Wikipedia-Dictionary").grid(column=0, row=0)

f2 = Frame(window, width=900, height=100, bg="blue").grid(column=0, row=1)
l2 = Label(master=f2, text="Enter: ").grid(column=0, row=1)
e1 = Entry(master=f2).grid(column=0, row=1)

window.mainloop()
from tkinter import *
from WebScraper import webscrape


window = Tk()


window.title("WIKI-DICTIONARY")
window.resizable(height=False, width=False)
window.configure(bg="white")


def onbtn2press():
    e1.delete(0, END)


def onbtn1press():
    t1.delete('1.0', END)
    entryinput = e1.get()
    try:
        text = webscrape(entryinput)
    except:
        text = "We could not find a proper definition. Please check your entry."
    t1.insert('1.0', text)


f1 = Frame(window, height=15, width=700, bg="yellow", pady=6).grid(column=0, row=0)

l1 = Label(master=window, text="Wikipedia-Dictionary", bg="#ffe0d5").grid(column=0, row=0)

f2 = Frame(window, width=900, height=100, bg="#7fffd4", pady=10, padx=10)

e1 = Entry(master=f2, bg="#ffede3")
e1.grid(column=0, row=0)
t1 = Text(master=f2, bg="#fffbe9")
t1.grid(column=0, row=2)

f3 = Frame(master=f2, bg="yellow")

btn1 = Button(master=f3, text="Enter", bg="#ffede3", command=onbtn1press).grid(column=1, row=0)
btn2 = Button(master=f3, text="Clear", bg="#ffede3", command=onbtn2press).grid(column=0, row=0)

f3.grid(column=0, row=1)

f2.grid(column=0, row=2)


window.mainloop()


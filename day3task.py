'''python programming-simple registration form'''
#importing library
from tkinter import *
from tkinter import ttk

window =Tk()
#declaring window title
window.title("Registration Screen")
#declaring window size
window.geometry('300x300')
#declaring window colour
window.configure(background = "green");
#below four fields are declared
Firstname = Label (window ,text = "first Name").grid(row = 0,column = 0)
Lastname = Label (window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label (window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row =3,column = 1)
#function declaration
def clicked():
    res = "Welcome to" + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window,text="submit").grid(row=4,column=0)
btn = ttk.Button(window,text="radio").grid(row=5,column=0)
btn = ttk.Button(window,text="Drop down).grid(row=6,column=0)
window.mainloop()
    
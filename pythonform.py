''' todays task #python form'''
#importing library
from tkinter import *
from tkinter import ttk


window =Tk()
#Declaring window title
window.title("Hike Details")
#Declaring window size
window.geometry('600x600')
#declaring window colour
window.configure(background = "Blue");
#below 10 feilds are declared
Employeename = Label (window ,text = "Employee Name").grid(row = 0,column = 0)
Employeeid = Label (window ,text = "Employee Id").grid(row = 1,column = 0)
Mobile = Label (window ,text = "Contact Number").grid(row = 2,column = 0)
Email = Label (window ,text = "Email Id").grid(row = 3,column = 0)
Age = Label (window ,text = "Age").grid(row = 4,column = 0)
Gender = Label (window ,text = "Gender").grid(row = 5,column = 0)
Residence = Label (window ,text = "Residence").grid(row = 6,column = 0)
Salary = Label (window ,text = "Current salary").grid(row = 7,column = 0)
Experience = Label (window ,text ="Experience").grid(row = 8,column = 0)
Hike = Label (window ,text ="Hike").grid(row = 9,column = 0)
Employeename1 = Entry(window).grid(row = 0,column = 1)
Employeeid1 = Entry(window).grid(row = 1,column = 1)
Mobile1 = Entry(window).grid(row = 2,column = 1)
Email1 = Entry(window).grid(row = 3,column = 1)
Age1 = Entry(window).grid(row = 4,column = 1)
Gender1 = Entry(window).grid(row = 5,column = 1)
Residence1 = Entry(window).grid(row = 6,column = 1)
Salary1 = Entry(window).grid(row = 7,column = 1)
Experience1 = Entry(window).grid(row = 8,column = 1)
Hike1 = Entry(window).grid(row = 9,column = 1)
# function declaration
def clicked():
    res = "Welcome to" + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window,text="submit").grid(row = 10,column = 0)
btn = ttk.Button(window,text="Radio").grid(row = 11,column = 1)
btn = ttk.Button(window,text="Drop down").grid(row = 12,column = 2)
window.mainloop()



    

from tkinter import *
from datetime import date

#create window

window=Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

#adding widgets
#adding label
lbl=Label(text="hello!",fg="white",bg="#072F5f",height=1,width=300)

# adding label for getting name as input from the user

Name_label=Label(text="full name",bg="#3895D3")

# use entry widget to create a text box for user to enter details
name_entry=Entry()

#function to display a message

def display():

#read input given by the user

    name=name_entry.get()
    global Message

    Message="welcome to THE application \n today's date is..."
    greet="Hello:)" + name + "\n"

#display details in the text box

    Text_box.insert(END,greet)
    Text_box.insert(END,Message)
    Text_box.insert(END,date.today())
Text_box=Text(height=3)
btn=Button(text="begin",command=display,height=1,bg="#1261A0",fg="white")
lbl.pack()
Name_label.pack()
name_entry.pack()
btn.pack()
Text_box.pack()
window.mainloop()
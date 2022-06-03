from time import strftime
from tkinter import *

from TkinterPRo01 import MainUI

UsernameList = ['Hardik007','Jagrat009','Jay003','Varun369']
passwordList =['hardik007','jagrat009', 'jay003','varun369']
def validateLogin(username,password) :
    print("username entered :",username.get())
    print("password entered :",password.get())
    return

tkWindow = Tk()
tkWindow.geometry('450x450')
tkWindow.title('Tkinter Login Form - pythonexamples.org')

Label(tkWindow,text='Data Extraction GUI',font=("Raleway",30),fg="Black",height=2,width=20).place(x=5,y=40)

def myTime():
    time_string = strftime('%Y-%m-%d %H:%M:%S')  # time format
    l1.config(text=time_string)
    l1.after(1000,myTime)  # time delay of 1000 milliseconds

myfont = ('Raleway',25,'bold')
l1 = Label(tkWindow,font=myfont)
l1.place(x=70,y=350)
myTime()

# username label and text entry box
Label(tkWindow,font=("Raleway",18),text="User Name").place(x=10,y=150)
username = StringVar()
usernameEntry = Entry(tkWindow,textvariable=username,font="Raleway",borderwidth=6,relief="groove",bg="#FFFFFF",
                      fg="black",width=20)
usernameEntry.place(x=150,y=150)

# password label and password entry box
Label(tkWindow,font=("Raleway",18),text="Password").place(x=10,y=200)
password = StringVar()
passwordEntry = Entry(tkWindow,textvariable=password,font="Raleway",borderwidth=6,relief="groove",bg="#FFFFFF",
                      fg="black",width=20)
passwordEntry.place(x=150,y=200)

validateLogin = partial(validateLogin,username,password)

# login button

Button(tkWindow,text="Login",font=("Raleway",15),borderwidth=6,command=lambda : MainUI.PressedLogin(),height=1,
       width=10).place(x=250,y=270)
tkWindow.mainloop()
tkWindow.withdraw()




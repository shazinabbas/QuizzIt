from tkinter import *
# import tksvg
import pyrebase
from database import*
import CreateQuiz as cq
import signup as sp
from tkinter import messagebox

def Signup():
    sp.SignUp()
    login()
    return
    
def btn_clickedlogin(window,userdata,pass_data):
    username=str(userdata.get())
    password=str(pass_data.get())
    if(len(username)==0 or len(password)==0):
        messagebox.showwarning('Warning','\nPlease fill all the fields.')
        return
    flag=0
    users=db.child("user").get()
    for user in users.each():   
        if(username==user.key()):
            flag=1
            if(password==user.val()['Password']):
                window.destroy()
                cq.Welcome(username)
            else:
                messagebox.showwarning('Warning',"Incorrect Password!")
                pass_data.set("")
                return
    if(flag==0):
        messagebox.showwarning('Warning','User not found!\nSignup or try again.')
        userdata.set("")
        pass_data.set("")
        return

def login():
    window = Tk()
    window.title("Login")
    window.geometry("1007x628")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=628,
        width=1007,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="background23.png")
    background = canvas.create_image(
        504.0, 315.0,
        image=background_img)

    img0 = PhotoImage(file="SP.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda : [window.destroy(),Signup()],
        relief="flat")

    b0.place(
        x=269.0, y=467.0,
        width=191,
        height=22)

    entry0_img = PhotoImage(
        file="img_textBox0.png")
    entry0_bg = canvas.create_image(
        363.77508544921875, 310.3297424316406,
        image=entry0_img)
    userdata=StringVar()
    entry0 = Entry(
        bd=0,
        bg="#f3ebeb",
        textvariable=userdata,
        highlightthickness=0)

    entry0.place(
        x=259.5393133163452, y=295.8297424316406,
        width=208.47154426574707,
        height=27)

    entry1_img = PhotoImage(
        file="img_textBox1.png")
    entry1_bg = canvas.create_image(
        363.77508544921875, 374.15087890625,
        image=entry1_img)
    pass_data=StringVar()
    entry1 = Entry(
        bd=0,
        bg="#f3ebeb",
        textvariable=pass_data,
        highlightthickness=0)

    entry1.place(
        x=259.5393133163452, y=359.65087890625,
        width=208.47154426574707,
        height=27)

    img1 = PhotoImage(file="login.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda : btn_clickedlogin(window,userdata,pass_data),
        relief="flat")

    b1.place(
        x=323.7510681152344, y=420.9259033203125,
        width=75,
        height=31)

    window.resizable(False, False)
    window.mainloop()
login()
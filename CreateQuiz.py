from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database import*
from attempt import*
import Submitted as sb
from PIL import ImageTk, Image
import getQues

def getcode(user):

    def startQuiz():
        codes=db.child("Host").child("Quizzes Hosted").get()
        qCode=qcode.get()
        flag1=0
        for code in codes.each():
            if(str(code.val()['QuizCode'])==str(qCode)):
                flag1=1
                window.destroy()
                AttemptQuiz(user,qCode)
                sb.submitted(user,qCode)
        if(flag1==0):
            messagebox.showwarning('Warning','\nEnter correct quizcode.')
            qcode.set("")
            return

    window = Tk()
    window.title("QuizCode")
    window.geometry("750x414")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=414,
        width=750,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="background24.png")
    background = canvas.create_image(
        375.0, 207.0,
        image=background_img)

    canvas.create_text(
        375.5, 120.0,
        text="ENTER QUIZ CODE",
        fill="#000000",
        font=("BMHANNA", int(30.0)))

    entry0_img = PhotoImage(
        file="img_textBoxcode.png")
    entry0_bg = canvas.create_image(
        372.0, 186.5,
        image=entry0_img)
    qcode=StringVar()
    entry0 = Entry(
        bd=0,
        bg="#ffffff",
        textvariable=qcode,
        highlightthickness=0)

    entry0.place(
        x=277.0, y=166.0,
        width=190,
        height=39)

    img0 = PhotoImage(file="code.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=startQuiz,
        relief="flat")

    b0.place(
        x=520.0, y=262.0,
        width=87,
        height=39)

    window.resizable(False, False)
    window.mainloop()

def Welcome(user):
    Teacher=str(user)
    win=Tk()
    win.title("Welcome")
    win.geometry("500x300")
    win.resizable(False, False)
    bg=ImageTk.PhotoImage(Image.open("x.jpg"),master=win)
    blabel = Label(win, image=bg)
    blabel.pack()
    user=Label(win,text=f"Welcome {user}!").place(x=190,y=60)
    host_button = Button(win,text = "Host a Quiz",command=lambda: [win.destroy(),HostQuiz(Teacher)]).place(x = 140,y = 90)
    join_button = Button(win,text = "Join a Quiz",command=lambda: [win.destroy(),getcode(Teacher)]).place(x = 260,y = 90)
    win.mainloop()
    
def HostQuiz(user):
    def quizDetails(b0):
        def addDetails(win):
            Time_Duration=TimeDuration.get()
            if(not(Time_Duration.isnumeric()) or int(Time_Duration)<=0):
                messagebox.showwarning('Warning','\nEnter correct Time Duration.')
                TimeDuration.set(" 0000")
            else:
                data1={"QuizCode":f"{QuizName}123","Teacher":user}
                db.child("Host").child("Quizzes Hosted").child(f"{QuizName}123").set(data1)
                data={"QuizName":QuizName,"Num of questions":numQuestions,"Time Restriction": Time,"QuizStatus":"Inactive","Time Duration":Time_Duration}
                db.child("Host").child(user).child(f"{QuizName}123").child('QuizDetails').set(data)
                win.destroy()      
                getQues.getQues(user,f"{QuizName}123")          

        QuizName=quizName.get()
        numQuestions=str(nQuestions.get())
        Time=OptionSelected.get()

        if(len(QuizName)==0 or len(numQuestions)==0 or Time=="Select"):
            messagebox.showerror("Empty Fields", "\nPlease enter all the values.")

        elif(not(numQuestions.isnumeric()) or int(numQuestions)<=0):
            messagebox.showwarning('Warning','\nEnter a positive number of questions.')
            entry1.delete(0, END)

        else:
            if(Time=='Time limit for the whole quiz'):
                entry2_img = PhotoImage(file="TimeDuration.png")
                canvas.create_image(
                            706.0, 393.0,
                            image=entry2_img)
                TimeDuration=StringVar()
                TimeDuration.set(" 0000")
                entry2 = Entry(
                        bd=0,
                        bg="#d9d9d9",
                        textvariable=TimeDuration,
                        highlightthickness=0)

                entry2.place(
                        x=606.0, y=390.0,
                        width=200.0,
                        height=28)
                b0.destroy()
                img1 = PhotoImage(file="nextbutton.png")
                b0 = Button(window,image=img1,borderwidth=0.7,command=lambda:addDetails(window))
                b0.place(x=739.0, y=440.0,width=77,height=28)
                window.mainloop()
            else:
                data={"QuizName":QuizName,"Num of questions":numQuestions,"Time Restriction": Time,"QuizStatus":"Inactive"}
                data1={"QuizCode":f"{QuizName}123","Teacher":user}
                db.child("Host").child("Quizzes Hosted").child(f"{QuizName}123").set(data1)
                db.child("Host").child(user).child(f"{QuizName}123").child('QuizDetails').set(data)

    window = Tk()
    window.title("QuizDetails")
    window.geometry("1050x650")
    window.configure(bg="#461a42")
    canvas = Canvas(
        window,
        bg="#461a42",
        height=650,
        width=1050,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)
    background_img = PhotoImage(file="background.png")
    background = canvas.create_image(
        525.0, 327.0,
        image=background_img)

    img0 = PhotoImage(file="nextbutton.png")
    b0 = Button(window,image=img0,borderwidth=0.7,command=lambda : quizDetails(b0))
    b0.place(x=740.0, y=396.0,width=77,height=28)

    quizName=StringVar()
    nQuestions=StringVar()
    
    entry0 = Entry(
        bd=0,
        bg="#d9d9d9",
        textvariable=quizName,
        highlightthickness=0)

    entry0.place(
        x=606.0, y=178.0,
        width=200.0,
        height=28)

    entry1 = Entry(
        bd=0,
        bg="#d9d9d9",
        textvariable=nQuestions,
        highlightthickness=0)

    entry1.place(
        x=606.0, y=250.0,
        width=200.0,
        height=28)

    img1 = PhotoImage(file="quizit.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat")

    b1.place(
        x=0.0, y=15.0,
        width=126,
        height=30)

    OptionsList=["Time limit for the whole quiz","No time restriction"] 
    OptionSelected=StringVar(window)
    OptionSelected.set("Select Time Restriction")
    optmenu = OptionMenu(window, OptionSelected, *OptionsList)
    optmenu.place(x=596.0,y=317.0,width=223.0,height=32)
    
    window.resizable(False, False)
    window.mainloop()
# Welcome("Niteesh")
# get_Questions("Niteesh","Try1","5","Time limit per question")


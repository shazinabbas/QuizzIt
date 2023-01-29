from tkinter import *
from database import*

def btn_clicked() -> None:
    print("Button Clicked")

def Leaderboard(quizCode):
    
    codes=db.child("Host").child("Quizzes Hosted").child(quizCode).get()
    Teacher=codes.val()['Teacher']
    Questions=db.child("Host").child(Teacher).child(quizCode).child("QuizDetails").child("Num of questions").get()
    numQuestions=Questions.val()
    Students=db.child("Host").child(Teacher).child(quizCode).child("Students Enrolled").get()
    Students_Data=[]
    for student in Students.each():
        Students_Data.append(student.val())
    Data = sorted(Students_Data, key=lambda d: d['Score']) 
    n=int(len(Data))

    window = Tk()
    window.title("Leaderboard")
    window.geometry("1050x650")
    window.configure(bg="#FFFFFF")
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=650,
        width=1050,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="lbBG.png")
    background = canvas.create_image(
        525.0, 325.5,
        image=background_img)

    canvas.create_text(
        885.5, 168.0,
        text="QUESTIONS ATTEMPTED",
        fill="#ffffff",
        font=("None", int(13.0)))

    canvas.create_text(
        624.5, 168.0,
        text="CORRECT ANSWERS",
        fill="#ffffff",
        font=("None", int(13.0)))

    canvas.create_text(
        292.5, 168.0,
        text="NAME",
        fill="#ffffff",
        font=("None", int(13.0)))

    canvas.create_text(
        69.5, 168.0,
        text="RANK",
        fill="#ffffff",
        font=("None", int(13.0)))
    for i in range(n):
        canvas.create_text(
            885.5, 224+(i*38),
            text=numQuestions,
            fill="#ffffff",
            font=("None", int(13.0)))

        canvas.create_text(
            619.5, 224+(i*38),
            text=Data[n-i-1]['Score'],
            fill="#ffffff",
            font=("None", int(13.0)))

        canvas.create_text(
            297.5, 222+(i*38),
            text=Data[n-i-1]['Name'],
            fill="#ffffff",
            font=("None", int(13.0)))

        canvas.create_text(
            61.5, 224+(i*38),
            text=i+1,
            fill="#ffffff",
            font=("None", int(13.0)))

    canvas.create_text(
        524.5, 95.5,
        text="LEADERBOARD",
        fill="#ffffff",
        font=("None", int(32.0)))

    img0 = PhotoImage(file="img4.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat")

    b0.place(
        x=976.0, y=15.0,
        width=49,
        height=25)

    img1 = PhotoImage(file="img5.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat")

    b1.place(
        x=900.0, y=15.0,
        width=64,
        height=25)

    img2 = PhotoImage(file="img6.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat")

    b2.place(
        x=14.0, y=8.0,
        width=80,
        height=36)

    window.resizable(False, False)
    window.mainloop()

# Leaderboard("Trial123")
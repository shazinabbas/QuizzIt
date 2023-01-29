from tkinter import *
from database import*

def viewAnalysis(studentName,quizCode):

    codes=db.child("Host").child("Quizzes Hosted").child(quizCode).get()
    Teacher=codes.val()['Teacher']
    Questions=db.child("Host").child(Teacher).child(quizCode).child("Questions").get()

    for Question in Questions.each():

        ques=db.child("Quiz Results").child(quizCode).child(studentName).child(Question.key()).get()
        question=Question.val()['Question']

        Given_Ans=ques.val()['Given Ans']
        Crct_Ans=ques.val()['Correct Answer']
        Expln=ques.val()['Explaination']

        window = Tk()
        window.title("QuizAnalysis")
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

        if((ques.val()['Correct'])==1):
            background_img = PhotoImage(file="backgroundcorrect.png")
        else:
            background_img = PhotoImage(file="backgroundwrong.png")
         
        background = canvas.create_image(
            525.0, 325.0,
            image=background_img)
        img0 = PhotoImage(file="img4.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=exit,
            relief="flat")

        b0.place(
            x=982.0, y=15.0,
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
            x=909.0, y=15.0,
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
            x=20.0, y=8.0,
            width=80,
            height=36)

        canvas.create_text(
            202.5, 140.5,
            text=quizCode[0:len(quizCode)-3],
            fill="#000000",
            font=("Inter-SemiBold", int(12.72624397277832)))

        canvas.create_text(
            526.0, 232.0,
            text=question,
            fill="#ffffff",
            font=("Inter-SemiBold", int(15.0)))

        canvas.create_text(
            463.0, 308.0,
            text=Given_Ans,
            fill="#ffffff",
            font=("Inter-Medium", int(11.0)))

        canvas.create_text(
            463.0, 365.0,
            text=Crct_Ans,
            fill="#ffffff",
            font=("Inter-Medium", int(11.0)))

        canvas.create_text(
            463.0, 420.0,
            text=Expln,
            fill="#ffffff",
            font=("Inter-Medium", int(11.0)))

        img = PhotoImage(file="nextbutton.png")
        next_button = Button(window,image=img,borderwidth=0.7,command=lambda:window.destroy()).place(x=824,y=508)
        window.resizable(False, False)
        window.mainloop()



# viewAnalysis("NiteeshK","Trial123")
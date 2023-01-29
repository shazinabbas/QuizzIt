from tkinter import *
import Submitted as sb
from database import*

correctCount=0

def AttemptQuiz(StudentName,quizCode):

    codes=db.child("Host").child("Quizzes Hosted").child(quizCode).get()
    Teacher=codes.val()['Teacher']
    Questions=db.child("Host").child(Teacher).child(quizCode).child("Questions").get()

    data2={"Correct Answers":0}
    db.child("Quiz Results").child(quizCode).child(StudentName).set(data2)

    for Question in Questions.each():
        crctAns=Question.val()['Correct Answer']
        Expln=Question.val()['Explaination']
        question=(Question.val()['Question'])
        def getAns(opt):
            qtype=Question.val()['QuesType']
            global correctCount
            if(qtype=="MCQ"):
              ans=opt
            else:
              ans=str(givenAns.get())
            if(ans.lower()==crctAns.lower()):
                Correct=1
                correctCount+=1
                data1={"Correct Answers":correctCount}
                db.child("Quiz Results").child(quizCode).child(StudentName).update(data1)
            else:
                Correct=0

            data={"Correct Answer":crctAns,"Explaination":Expln,"Given Ans":ans,"Correct":Correct}
            db.child("Quiz Results").child(quizCode).child(StudentName).child(Question.key()).set(data)
            window.destroy()

        window = Tk()
        window.title("Quiz")
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

        background_img = PhotoImage(file="background0.png")
        background = canvas.create_image(
            525.0, 325.0,
            image=background_img)

        img0 = PhotoImage(file="img4.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            command=exit,
            relief="flat")

        b0.place(
            x=982.0, y=15.0,
            width=49,
            height=25)

        img1 = PhotoImage(file="img4.png")
        b1 = Button(
            image=img1,
            borderwidth=0,
            command=exit)

        b1.place(
            x=909.0, y=15.0,
            width=64,
            height=25)

        img2 = PhotoImage(file="img6.png")
        b2 = Button(
            image=img2,
            borderwidth=0,
            command=exit,
            relief="flat")

        b2.place(
            x=20.0, y=8.0,
            width=80,
            height=36)

        canvas.create_text(
            201.5, 140.5,
            text=f"{quizCode[0:len(quizCode)-3]}",
            fill="#000000",
            font=("Inter-SemiBold", int(12)))

        qtype=Question.val()['QuesType']
        
        if(qtype=="MCQ"):
          OptionsList=Question.val()["Options"]
          L=list(OptionsList)
          for i in range(len(OptionsList)):
              if(i%2==0):
                L[i] = Button(
                    text=OptionsList[i],
                    borderwidth=0,
                    highlightthickness=0,
                    command=lambda: getAns(OptionsList[i]),
                    relief="flat")

                L[i].place(
                    x=328.0, y=325+(i*64),
                    width=145,
                    height=32)
              else:
                L[i] = Button(
                    text=OptionsList[i],
                    borderwidth=0,
                    highlightthickness=0,
                    command=lambda: getAns(OptionsList[i]),
                    relief="flat")

                L[i].place(
                    x=594.0, y=325+((i-1)*64),
                    width=145,
                    height=32)
        else:
          entry0_img = PhotoImage(
              file="img_textBox11.png")
          entry0_bg = canvas.create_image(
              524.5, 337.5,
              image=entry0_img)

          givenAns=StringVar()
          entry0 = Entry(
              bd=0,
              bg="#edfeff",
              textvariable=givenAns,
              highlightthickness=0)

          entry0.place(
              x=334.7873296737671, y=326.0,
              width=379.4253406524658,
              height=23)

        canvas.create_text(
            862.0, 135.0,
            text="00:00:00",
            fill="#e91d1d",
            font=("Inter-SemiBold", int(11)))

        canvas.create_text(
            519.0, 292.0,
            text=question,
            fill="#ffffff",
            font=("Inter-SemiBold", int(14)))

        img = PhotoImage(file="nextbutton.png")
        next_button = Button(window,image=img,borderwidth=0.7,command=lambda:getAns('dummy')).place(x=824,y=508)

        window.resizable(False, False)
        window.mainloop()

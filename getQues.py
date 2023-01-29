from database import*
from tkinter import messagebox
from getOptions import*

def add_Ques(root,j,user,quizcode,question,crctAns,Expln,OptionSelected):
    Question=str(question.get())
    Crct_Ans=str(crctAns.get())
    Explaination=str(Expln.get())
    if(len(Question)==0 or len(Crct_Ans)==0 or len(Explaination)==0):
            messagebox.showerror("Empty Fields", "Please enter all the values.")
    else:
        data={'Question':Question,'Correct Answer':Crct_Ans,'Explaination':Explaination,"QuesType":"OneWord"}
        db.child("Host").child(user).child(quizcode).child("Questions").child(f'Q{j+1}').set(data)
        root.destroy()

def getoptions(j,user,quizcode,nOptions):
    numOptions=nOptions.get()
    if(not(numOptions.isnumeric()) or int(numOptions)<=0):
        messagebox.showwarning('Warning','Enter a postive number of options')
        nOptions.set(" Num of Options")
    else:
        typeData={"QuesType":"MCQ"}
        Options_List=Options(int(numOptions))
        db.child("Host").child(user).child(quizcode).child("Questions").child(f'Q{j+1}').child("Options").set(Options_List)
        db.child("Host").child(user).child(quizcode).child("Questions").child(f'Q{j+1}').update(typeData)

def getQues(user,quizcode):
    details=db.child("Host").child(user).get()
    for detail in details.each():
        if(detail.key()==quizcode):
            for j in range(int(detail.val()['QuizDetails']['Num of questions'])):
                def questype(event):                     
                    if(OptionSelected.get()=="Multiple Choice Question"):
                        nOptions=StringVar()
                        nOptions.set(" Num of Options")
                        global entry
                        entry = Entry(win,bd=0,bg="#edfeff",highlightthickness=0,textvariable=nOptions)
                        entry.place(x=400.48, y=329.32,width=115,height=23)
                        global optbutton
                        optbutton=Button(win,text="✔",bg="#edfeff",highlightthickness=0,command=lambda:getoptions(j,user,quizcode,nOptions))
                        optbutton.place(x=516,y=329,width=23,height=23)
                        win.mainloop()
                        
                    elif(OptionSelected.get()=="One Word Answer"):
                        try:
                            entry.destroy()
                            optbutton.destroy()
                        except:
                            pass
                win = Tk()
                win.title("getQues")
                win.geometry("1050x650")
                win.configure(bg="#FFFFFF")
                canvas = Canvas(
                    win,
                    bg="#FFFFFF",
                    height=650,
                    width=1050,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file="background4.png")
                background = canvas.create_image(
                    525.0, 325.0,
                    image=background_img)

                entry0_img = PhotoImage(
                    file="img_textBox8.png")
                entry0_bg = canvas.create_image(
                    413.4819030761719, 277.033935546875,
                    image=entry0_img)

                question=StringVar()
                crctAns=StringVar()
                Expln=StringVar()

                entry0 = Entry(
                    bd=0,
                    bg="#edfeff",
                    textvariable=question,
                    highlightthickness=0)

                entry0.place(
                    x=193.26923274993896, y=264.533935546875,
                    width=440.4253406524658,
                    height=23)

                entry1_img = PhotoImage(
                    file="img_textBox9.png")

                entry2_bg = canvas.create_image(
                    290.4819030761719, 404.29638671875,
                    image=entry1_img)

                entry2 = Entry(
                    bd=0,
                    bg="#edfeff",
                    textvariable=crctAns,
                    highlightthickness=0)

                entry2.place(
                    x=193.26923274993896, y=391.79638671875,width=194.42534065246582,height=23)

                entry3_bg = canvas.create_image(
                    413.4819030761719, 467.0791931152344,
                    image=entry0_img)

                entry3 = Entry(
                    bd=0,
                    bg="#edfeff",
                    textvariable=Expln,
                    highlightthickness=0)

                entry3.place(
                    x=193.26923274993896, y=454.5791931152344,
                    width=440.4253406524658,
                    height=23)

                canvas.create_text(
                    220.71041870117188, 220.49322509765625,
                    text=f"Question {j+1}",
                    fill="#000000",
                    font=("Inter-SemiBold", int(12)))

                canvas.create_text(
                    352, 168,
                    text=f"Your quiz code is {quizcode}",
                    fill="#000000",
                    font=("Inter-SemiBold", int(9.5)))

                img0 = PhotoImage(file="quit.png")
                b0 = Button(
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=exit,
                    relief="flat")

                b0.place(
                    x=997.0, y=5.0,
                    width=50,
                    height=16)

                img1 = PhotoImage(file="home.png")
                b1 = Button(
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=exit,
                    relief="flat")

                b1.place(
                    x=924.0, y=5.0,
                    width=55,
                    height=16)

                img2 = PhotoImage(file="quizIT.png")
                b2 = Button(
                    image=img2,
                    borderwidth=0,
                    highlightthickness=0,
                    command=exit,
                    relief="flat")

                b2.place(
                    x=8.999992370605469, y=4.469565391540527,
                    width=62,
                    height=19)
                OptionsList=["Multiple Choice Question","One Word Answer"] 
                OptionSelected=StringVar(win)
                OptionSelected.set("Select Question Type")
                optmenu = OptionMenu(win, OptionSelected, *OptionsList,command=questype)
                optmenu.config(bg="#edfeff",fg="black",borderwidth=0,highlightthickness=0)
                optmenu.place(x=192, y=327,width=194.42534065246582,height=25)

                img = PhotoImage(file="nextbutton.png")
                next_button = Button(win,image=img,borderwidth=0.7,command=lambda:add_Ques(win,j,user,quizcode,question,crctAns,Expln,OptionSelected))
                next_button.place(x=668, y=501,width=77,height=28)
                win.resizable(False, False)
                win.mainloop()

# getQues("Lodu","Take69123")
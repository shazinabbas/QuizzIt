data3={"Name":studentName,"Score":score}
    db.child("Host").child(Teacher).child(quizCode).child("Students Enrolled").child(studentName).set(data3)
    rroot = Tk()
    rroot.title("QuizSubmitted")
    rroot.geometry("1050x650")
    rroot.configure(bg="#FFFFFF")
    canvas = Canvas(
        rroot,
        bg="#FFFFFF",
        height=650,
        width=1050,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="background1.png")
    background = canvas.create_image(
        525.0, 325.0,
        image=background_img)

    img0 = PhotoImage(file="view.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:[rroot.destroy(),analysis.viewAnalysis(studentName,quizCode)],
        relief="flat")

    b0.place(
        x=777.0, y=508.0,
        width=123,
        height=33)

    img1 = PhotoImage(file="img4.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat")

    b1.place(
        x=982.0, y=15.0,
        width=49,
        height=25)

    img2 = PhotoImage(file="img5.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat")

    b2.place(
        x=909.0, y=15.0,
        width=64,
        height=25)

    img3 = PhotoImage(file="img6.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat")

    b3.place(
        x=20.0, y=8.0,
        width=80,
        height=36)

    canvas.create_text(
        202.5, 140.5,
        text=f"{quizCode[0:len(quizCode)-3]}",
        fill="#000000",
        font=("Inter-SemiBold", int(12.72624397277832)))

    canvas.create_text(
        561.0, 327.5,
        text=score,
        fill="#ffffff",
        font=("Inter-SemiBold", int(17.0)))

    canvas.create_text(
        605.0, 370.5,
        text=score,
        fill="#ffffff",
        font=("Inter-SemiBold", int(17.0)))

    canvas.create_text(
        605.0, 409.5,
        text=int(numQuestions)-int(score),
        fill="#ffffff",
        font=("Inter-SemiBold", int(17.0)))
    

    rroot.resizable(False, False)
    rroot.mainloop()
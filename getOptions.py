from tkinter import*
def Options(numOptions):
    def exit():
        global Options_List
        Options_List=[]
        for i in L:
            Options_List.append(i.get())
        root.destroy()

    root=Toplevel()
    root.title("GetOptions")
    root.geometry("500x300")
    root.configure(bg="#ffffff")
    canvas = Canvas(
        root,
        bg="#ffffff",
        height=300,
        width=500,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)
    background_img = PhotoImage(file="background5.png")
    background = canvas.create_image(
        250.0, 150.00000000000003,
        image=background_img)

    entry_img = PhotoImage(
        file="img_textBox10.png")

    L=[]
    for i in range(numOptions):
        L.append(i)
        L[i]=StringVar()
        L[i].set(f"Option {i+1}")
        if(i%2==0):
            entry0_bg = canvas.create_image(
                145.5, 96+(i*22),
                image=entry_img)
            entry0 = Entry(
                root,
                bd=0,
                bg="#b6d8da",
                textvariable=L[i],
                highlightthickness=0)

            entry0.place(
                x=87.0, y=83.5+(i*22),
                width=117.0,
                height=24)
        else:
            entry1_bg = canvas.create_image(
                355.5, 96+((i-1)*22),
                image=entry_img)

            entry1 = Entry(
                root,
                bd=0,
                bg="#b6d8da",
                textvariable=L[i],
                highlightthickness=0)

            entry1.place(
                x=297.0, y=83.5+((i-1)*22),
                width=117.0,
                height=24)
    img0 = PhotoImage(file="nextbutton.png")
    b0 = Button(root,image=img0,borderwidth=0.7,command=exit)
    b0.place(x=329, y=231,width=77,height=24)
    root.resizable(False, False)
    root.mainloop()
    return Options_List
    exit
from tkinter import *
from database import*
from tkinter import messagebox

def SignUp():
    def get_data():
        username=str(userdata.get())
        password=str(pass_data.get())
        name=str(nameData.get())
        if(len(username)==0 or len(password)==0 or len(name)==0):
            messagebox.showwarning('Warning','Please fill all the fields.')
        else:
            users=db.child("user").get()
            flag=0
            for user in users.each():
                if(username==user.key()):
                    flag=1
                    messagebox.showwarning('Warning','Usename already exists.')
            if(flag==0):
                data={"Name":name,"Username":username,"Password":password}
                db.child("user").child(username).set(data)
                messagebox.showinfo("Information","User added successfully!")
                root.destroy()
                
    root = Tk()
    root.title("Signup")
    root.geometry("654x407")
    root.configure(bg="#ffffff")
    canvas = Canvas(
        root,
        bg="#ffffff",
        height=407,
        width=654,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="background3.png")
    background = canvas.create_image(
        327.0, 203.5,
        image=background_img)

    img0 = PhotoImage(file="img2.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda : root.destroy(),
        relief="flat")

    b0.place(
        x=89.0, y=372.0,
        width=198,
        height=15)

    userdata=StringVar()
    pass_data=StringVar()
    nameData=StringVar()

    entry0_img = PhotoImage(
        file="img_textBox7.png")
    entry0_bg = canvas.create_image(
        182.86000061035156, 174.6297607421875,
        image=entry0_img)

    entry0 = Entry(
        bd=0,
        bg="#ffe5cf",
        textvariable=nameData,
        highlightthickness=0)

    entry0.place(
        x=78.62422847747803, y=160.1297607421875,
        width=208.47154426574707,
        height=27)

    entry1_bg = canvas.create_image(
        182.86448669433594, 238.450927734375,
        image=entry0_img)

    entry1 = Entry(
        bd=0,
        bg="#ffe5cf",
        textvariable=userdata,
        highlightthickness=0)
    entry1.place(
        x=78.6287145614624, y=223.950927734375,
        width=208.47154426574707,
        height=27)
    entry2_bg = canvas.create_image(
        182.86448669433594, 301.450927734375,
        image=entry0_img)
    entry2 = Entry(
        bd=0,
        bg="#ffe5cf",
        textvariable=pass_data,
        highlightthickness=0)
    entry2.place(
        x=78.6287145614624, y=286.950927734375,
        width=208.47154426574707,
        height=27)
    img1 = PhotoImage(file="img3.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=get_data,
        relief="flat")
    b1.place(
        x=145.8404541015625, y=333.2259521484375,
        width=75,
        height=31)
    root.resizable(False, False)
    root.mainloop()
# SignUp()
import tkinter
from window2 import menu
from PIL import Image,ImageTk
import mysql.connector as mysql
#root=login page
#root1=menu
#rootp=patient form

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
#command for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='citech' and S2=='123'):
        menu()
    elif(S1=='citech' and S2=='citech'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("450x400")
    root.configure(background="#f6c065")
    topframe = tkinter.Frame(root)
    topframe.place(x=150,y=200)
    topframe.pack()
    imageframe = tkinter.Frame(root)
    imageframe.pack(padx=20,pady=10)
    middleframe = tkinter.Frame(root,background="#f6c065")
    middleframe.pack(padx=20,pady=20)
    bottomframe=tkinter.Frame(root,background="#f6c065")
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO C-19 MANAGEMENT SYSTEM",bg='white',fg='orange',font='Times 16 bold italic')
    image=Image.open("coronavirus.PNG")
    print(image)
    image=image.resize((180, 100))
    img = ImageTk.PhotoImage(image)

    imglabel = tkinter.Label(imageframe,image=img)
    username=tkinter.Label(middleframe,text="USERNAME",bg='#f6c065',font=("'Poppins', sans-serif",12))
    username.place(x=500, y=270)
    userbox = tkinter.Entry(middleframe,bg='#f6c065',font=("arial 8 bold",12,'bold'))
    userbox.place(x=500, y=270)
    password=tkinter.Label(middleframe,bg='#f6c065',text="PASSWORD",font=("arial 8 bold",12))
    passbox = tkinter.Entry(middleframe,bg='#f6c065',show="*",font=("arial 8 bold",12,'bold'))
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font=("arial 8 bold",12))
    heading.pack()
    username.pack()
    userbox.pack(padx=0,pady=2)
    password.pack()
    passbox.pack()
    login.pack()
    imglabel.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()
root.destroy()

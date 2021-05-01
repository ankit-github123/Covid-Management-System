import sqlite3
import tkinter
import tkinter.messagebox
import mysql.connector as mysql

P_id=None
rootR=None
P_room=None
P_roomType=None
P_room_date=None

##ROOM BUTTON
def room_button():
    global P_id,P_room,room,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn,P_roomType,P_room_date
    conn = mysql.connect(host="localhost", user="root", password="", database="covid")
    cursor = conn.cursor()
    print("DATABASE CONNECTION SUCCESSFUL")
    r1=P_id.get()
    r2=P_room.get()
    r3=P_roomType.get()
    r4=P_room_date.get()
    print(r1,r2,r3,r4)
    cursor.execute("INSERT INTO ROOM VALUES('" + r2 + "','" + r1 + "','" + r3 + "','" + r4 + "')")
    tkinter.messagebox.showinfo("C-19 DATABSE SYSTEM", "ROOM ALLOCATED")
    cursor.execute("commit")
    conn.close()

##ROOT FOR DISPLAY ROOM INFO
rootRD=None

##EXIT FOR ROOM_PAGE
def EXITT():
    global rootR
    rootR.destroy()


def exittt():
    rootRD.destroy()



def exitt():
    rootR.destroy()

L=None
L1=None
def Room_all():
    global rootR,room,P_room,r_head,P_id,P_roomType,id,P_room_date,L,i,room_t,room_no,L1,j,rate,da ,dd,Submit,room
    rootR=tkinter.Tk()
    rootR.configure(background="#fad586")

    rootR.title("ROOM ALLOCATION")
    rootR.geometry("300x400")
    r_head=tkinter.Label(rootR,text="ROOM ALLOCATION",font='Times 13 bold',fg="#fad586")
    r_head.place(x=75,y=10)

    id=tkinter.Label(rootR,bg='#fad586',text="PATIENT ID")
    id.place(x=100,y=60)
    P_id=tkinter.Entry(rootR)
    P_id.place(x=100,y=90)

    room=tkinter.Label(rootR,bg='#fad586',text="ROOM NUMBER")
    room.place(x=100,y=120)
    P_room=tkinter.Entry(rootR)
    P_room.place(x=100,y=150)
    # room.pack()
    room_type = tkinter.Label(rootR,bg='#fad586', text="ROOM Type")
    room_type.place(x=100, y=170)
    P_roomType = tkinter.Entry(rootR)
    P_roomType.place(x=100, y=195)
    #
    room_date = tkinter.Label(rootR,bg='#fad586', text="DATE")
    room_date.place(x=100, y=220)
    P_room_date = tkinter.Entry(rootR)
    P_room_date.place(x=100, y=250)

    Submit=tkinter.Button(rootR,text="SUBMIT",command=room_button)
    Submit.place(x=90,y=300)

    ee=tkinter.Button(rootR,text="EXIT",command=exitt)
    ee.place(x=150,y=300)
    rootR.mainloop()

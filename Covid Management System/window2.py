import tkinter
import tkinter.messagebox
from PATDELSU import P_display
from PATDELSU import D_display
from PATDELSU import P_UPDATE
from RooMT import Room_all
from BILLING import BILLING

import mysql.connector as mysql


conn=mysql.connect(host="localhost",user="root",password="",database="covid")
cursor=conn.cursor()
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_address=None
pat_sex=None
pat_BG=None
pat_contact=None
pat_dob=None
# def new():
#
#     rootnew =tkinter.Tk()
#     rootnew.geometry("220x255")

#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,m,imagelabel1,img,image,button5
    root1=tkinter.Tk()
    root1.geometry("280x350")
    root1.title("MAIN MENU")
    root1.configure(background="#fad586")
    m=tkinter.Label(root1,text="DASHBOARD",font='Times 16 bold italic',fg='grey')
    button1=tkinter.Button(root1,text="1.PATIENT REGISTRATION",command=PAT,bg='light blue',fg='black')
    button2 = tkinter.Button(root1, text="2.ROOM ALLOCATION",bg='light green',fg='black',command=Room_all)
    button3 = tkinter.Button(root1, text="3.PATIENT BILL",bg='light blue',fg='black',command=BILLING)
    button4 = tkinter.Button(root1, text="4.EXIT",command=ex,bg='light green',fg='black')
    # button5 = tkinter.Button(root1, text="4.NEW", command=new, bg='light green', fg='black')
    m.place(x=75,y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=50)
    button2.pack(side=tkinter.TOP)
    button2.place(x=80,y=100)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80,y=150)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)
    button5.pack(side=tkinter.TOP)
    # button5.place(x=80, y=250)
    # root1.mainloop()

p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6,conn,pp7
    conn = mysql.connect(host="localhost", user="root", password="", database="covid")
    cursor = conn.cursor()
    print("DATABASE CONNECTION SUCCESSFUL")
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4=pat_BG.get()
    pp5=pat_contact.get()
    print(pp5)
    pp6=pat_address.get()
    pp7=pat_dob.get()
    cursor.execute("INSERT INTO PATIENT VALUES('" + pp1 + "','" + pp2 + "','" + pp3 + "','" + pp4 + "','" + pp5 + "','" + pp6 + "','" + pp7 + "')")
    tkinter.messagebox.showinfo("C-19 DATABSE SYSTEM","DETAILS INSERTED INTO DATABASE")
    cursor.execute("commit")
    EXO()



#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def nothing():
    print("CONTACT DATABASE HEAD :921 ")

def nothing1():
    print("MADE BY C-19 Management system")

#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_CT, pat_dob, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,sex,addr,c1,c2,bg,SUBMIT,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.configure(background="#fad586")

    regform=tkinter.Label(rootp,text="REGISTRATION FORM",font="Arial 16 bold")
    id=tkinter.Label(rootp,text="PATIENT ID")
    pat_ID=tkinter.Entry(rootp)
    name=tkinter.Label(rootp,text="PATIENT NAME")
    pat_name = tkinter.Entry(rootp)
    sex=tkinter.Label(rootp,text="SEX")
    pat_sex=tkinter.Entry(rootp)

    bg=tkinter.Label(rootp, text="BLOOD GROUP")
    pat_BG=tkinter.Entry(rootp)
    c1=tkinter.Label(rootp, text="CONTACT NUMBER")
    pat_contact=tkinter.Entry(rootp)
    addr=tkinter.Label(rootp, text="ADDRESS")
    pat_address=tkinter.Entry(rootp)
    dob = tkinter.Label(rootp, text="DOB")
    pat_dob = tkinter.Entry(rootp)
    back=tkinter.Button(rootp,text="<< BACK",command=menu)
    SEARCH=tkinter.Button(rootp,text="  SEARCH >>  ",command=P_display)
    DELETE=tkinter.Button(rootp,text="  DELETE  ",command=D_display)
    UPDATE=tkinter.Button(rootp,text="  UPDATE  ",command=P_UPDATE)
    SUBMIT=tkinter.Button(rootp,text="  SUBMIT  ",command=IN_PAT,)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_contact.pack()
    addr.pack()
    pat_address.pack()
    dob.pack()
    pat_dob.pack()

    SUBMIT.pack()
    back.pack(side=tkinter.LEFT)
    UPDATE.pack(side=tkinter.LEFT)
    DELETE.pack(side=tkinter.LEFT)
    SEARCH.pack(side=tkinter.LEFT)
    #rootp.mainloop()


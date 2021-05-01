import tkinter
import sqlite3
import tkinter.messagebox
import mysql.connector as mysql
#variables
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None
#display/search button

def Search_button():
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    conn = mysql.connect(host="localhost", user="root", password="", database="covid")
    cursor = conn.cursor()
    print("DATABASE CONNECTION SUCCESSFUL search")
    inp_s=entry.get()
    cursor.execute("select * from patient where patient_id='" + inp_s + "' ");
    rows = cursor.fetchall()
    if (len(rows)==0):
        errorS=tkinter.Label(rootS,text="PATIENT RECORD NOT FOUND")
        errorS.pack()
    else:

        for i in rows:
            l1=tkinter.Label(rootS,text="PATIENT ID",fg='blue')
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="PATIENT NAME",fg='blue')
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="PATIENT SEX",fg='blue')
            dis3=tkinter.Label(rootS,text=i[2])
            l4=tkinter.Label(rootS,text="PATIENT BLOOD GROUP",fg='blue')
            dis4=tkinter.Label(rootS,text=i[3])
            l5=tkinter.Label(rootS,text="PATEINT CONTACT NO",fg='blue')
            dis5=tkinter.Label(rootS,text=i[4])
            l6=tkinter.Label(rootS,text="PATIENT ADDRESS",fg='blue')
            dis6=tkinter.Label(rootS,text=i[5])
            l1.pack()
            dis1.pack()
            l2.pack()
            dis2.pack()
            l3.pack()
            dis3.pack()
            l4.pack()
            dis4.pack()
            l5.pack()
            dis5.pack()
            cursor.execute("commit")
            conn.close()


def eXO():
    rootS.destroy()

##search window
def P_display():
    global rootS,head,inp_s,entry,searchB
    rootS=tkinter.Tk()
    rootS.configure(background="#fad586")

    rootS.title("SEARCH WINDOW")
    head=tkinter.Label(rootS,text="ENTER PATIENT ID TO SEARCH",fg="red")
    entry=tkinter.Entry(rootS)
    searchB=tkinter.Button(rootS,text='SEARCH',command=Search_button)
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_display)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    head.pack()
    entry.pack()
    searchB.pack()
    rootS.mainloop()

inp_d=None
entry1=None
errorD=None
disd1=None

#DELTE BUTTON
def Delete_button():
    global inp_d,entry1,errorD,disd1

    conn = mysql.connect(host="localhost", user="root", password="", database="covid")
    cursor = conn.cursor()
    print("DATABASE CONNECTION SUCCESSFUL del")
    inp_d = entry1.get()
    print(inp_d)
    # p=list(cursor.execute("select * from PATIENT where PATIENT_ID='"+inp_d+"'"))
    # print(p);
    if (1==0):
        errorD = tkinter.Label(rootD, text="PATIENT RECORD NOT FOUND")
        errorD.pack()
    else:
        cursor.execute("delete from patient where PATIENT_ID='"+inp_d+"'")
        disd1=tkinter.Label(rootD,text="PATIENT RECORD DELETED",fg='green')
        disd1.pack()
        cursor.execute("commit")


## DELETE SCREEN
def D_display():
    global rootD,headD,inp_d,entry1,DeleteB
    rootD=tkinter.Tk()
    rootD.configure(background="#fad586")

    rootD.title("DELETE WINDOW")
    headD=tkinter.Label(rootD,text="ENTER PATIENT ID TO DELETE",fg="blue")
    entry1=tkinter.Entry(rootD)
    DeleteB=tkinter.Button(rootD,text="DELETE",command=Delete_button)
    headD.pack()
    entry1.pack()
    DeleteB.pack()
    rootD.mainloop()

##variables for update

pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None

def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
    conn = mysql.connect(host="localhost", user="root", password="", database="covid")
    cursor = conn.cursor()
    print("DATABASE CONNECTION SUCCESSFUL update")
    u1 = pat_ID.get()
    u2 = pat_name.get()
    u3 = pat_sex.get()
    u4 = pat_BG.get()
    u5 = pat_contact.get()
    u6 = pat_address.get()
    p = 'ss'
    if len(p) != 0:
        cursor.execute("update patient set NAME='"+u2+"',SEX='"+u3+"',BG='"+u4+"',CONTACT='"+u5+"',ADDRESS='"+u6+"' WHERE patient_id='"+u1+"' ")
        tkinter.messagebox.showinfo("C-19 MANAGEMENT SYSTEM", "DETAILS UPDATED INTO DATABASE")
        cursor.execute("commit")

    else:
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")

labelu=None
bu1=None

def EXITT():
    rootU.destroy()
def get():
    conn = mysql.connect(host="localhost", user="root", password="", database="covid")
    cursor = conn.cursor()
    print("DATABASE CONNECTION SUCCESSFUL get")
    c1=pat_ID.get();
    cursor.execute("select * from patient where patient_id='"+c1+"' ");
    rows=cursor.fetchall()

    for row in rows:

        pat_name.insert(0, row[1])
        pat_sex.insert(0, row[2])
        pat_BG.insert(0, row[3])
        pat_contact.insert(0, row[4])
        pat_address.insert(0, row[5])

    conn.close()



##-----PATIENT UPDATE SCREEN -----##
def P_UPDATE():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootU, regform, id, name, dob, sex, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, p1f, p2f,HEAD
    rootU = tkinter.Tk()
    rootU.geometry("410x400")
    rootU.configure(background="#fad586")

    rootU.title("UPDATE WINDOW")
    menubar = tkinter.Menu(rootU)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_UPDATE)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXITT)
    rootU.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
    HEAD=tkinter.Label(rootU,text="ENTER NEW DETAILS TO UPDATE",bg='black',fg='white')
    id = tkinter.Label(rootU, text="PATIENT ID")
    pat_ID = tkinter.Entry(rootU)
    name = tkinter.Label(rootU, text="PATIENT NAME")
    pat_name = tkinter.Entry(rootU)
    sex = tkinter.Label(rootU, text="SEX")
    pat_sex = tkinter.Entry(rootU)

    bg = tkinter.Label(rootU, text="BLOOD GROUP")
    pat_BG = tkinter.Entry(rootU)
    c1 = tkinter.Label(rootU, text="CONTACT NUMBER")
    pat_contact = tkinter.Entry(rootU)

    addr = tkinter.Label(rootU, text="ADDRESS")
    pat_address = tkinter.Entry(rootU)
    SUBMIT=tkinter.Button(rootU,text="SUBMIT",command=up1)
    CHECK = tkinter.Button(rootU, text="CHECK", command=get)
    HEAD.pack()
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
    SUBMIT.pack()
    CHECK.pack()
    rootU.mainloop()

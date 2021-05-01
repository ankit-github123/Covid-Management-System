
import tkinter
import tkinter.messagebox
import mysql.connector as mysql


#variables
rootB=None



def up():
    global c1, b1, P_id,bno, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = mysql.connect(host="localhost", user="root", password="", database="covid")
    cursor = conn.cursor()
    print("DATABASE CONNECTION SUCCESSFUL")
    b1 = P_id.get()
    b2 = bno.get()
    b3 = cost_t.get()
    cursor.execute("INSERT INTO BILLING VALUES('" + b1 + "','" + b2 + "','" + b3 + "','" + str(0) + "')")
    cursor.execute("commit")
    print(b1,b3)
    cursor.callproc('cal_gst',(b1,b3))
    cursor.execute("commit")
    conn.close()
    tkinter.messagebox.showinfo("C-19 DATABASE SYSTEM", "BILLING DATA SAVED")


L1=None
def exitt():
    rootB.destroy()

def BILLING():
    global rootB,L1,treat1,P_id,bno,dd,cost,med,med_q,price,treat_1,treat_2,cost_t
    rootB=tkinter.Tk()
    rootB.configure(background="#fad586")
    rootB.geometry("450x350")
    rootB.title("BILLING SYSTEM")
    head=tkinter.Label(rootB,text="PATIENT BILL",font="Arial 16 bold italic",bg='#fad586',fg='grey')
    head.place(x=100,y=10)
    id = tkinter.Label(rootB,bg='#fad586', text="PATIENT ID")
    id.place(x=20, y=60)
    P_id = tkinter.Entry(rootB)
    P_id.place(x=100, y=60)
    B_no = tkinter.Label(rootB,bg='#fad586', text="BILL No")
    B_no.place(x=20, y=100)
    bno = tkinter.Entry(rootB)
    bno.place(x=100, y=100)
    costl= tkinter.Label(rootB, text="COST ₹")
    costl.place(x=20, y=140)
    cost_t = tkinter.Entry(rootB,width=5)
    cost_t.place(x=100, y=140)
    b2 = tkinter.Button(rootB, text="INSERT DATA", command=up)
    b2.place(x="100", y="210")
    ee=tkinter.Button(rootB,text="EXIT",command=exitt)
    ee.place(x='310',y='210')
    rootB.mainloop()

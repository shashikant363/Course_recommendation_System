from tkinter import *
from tkinter import messagebox
from subprocess import call
window=Tk()
window.title("COURSE RECOMMENDATION SYSTEM")
window.geometry('870x600')
window['bg'] = '#5d8a82'
def clrinput():
    tx1.delete(0,END)
    tx2.delete(0, END)
def login1():
    if((int(tx1.get())<1001 and int(tx1.get())>0) and (tx2.get()=="vit123")):
        window.destroy()
        import GOption
    else:
        messagebox.showwarning("WARNING","*invalid id or password* Login again")

lbA = Label(window, text="WELCOME  TO  COURSE  RECOMMENDATION  SYSTEM", fg='blue', font=('Arial', 20)).place(x=60,y=40)
lb1=Label(window,text="ID : ",fg='blue',font=('Arial',15)).place(x=170,y=140,width=230)

data1=StringVar()
tx1=Entry(window,textvariable=data1,fg='blue',font=('Arial',15))
tx1.place(x=470,y=140,width=230)
lb2=Label(window,text="PASSWORD : ",fg='blue',font=('Arial',15)).place(x=170,y=240,width=230)
data=StringVar()
tx2=Entry(window,textvariable=data,fg='blue',font=('Arial',15))
tx2.place(x=470,y=240,width=230)
btn1=Button(window,text="LOGIN AS STUDENT",fg='blue',font=('Arial',14),command=login1).place(x=60,y=340,width=230)

btn2=Button(window,text="LOGIN AS FACUILTY",fg='blue',font=('Arial',14)).place(x=315,y=340,width=230)  #,command=rec_course

btn3=Button(window,text="CLEAR INPUTS",fg='blue',font=('Arial',14),command=clrinput).place(x=570,y=340,width=230)  #,command=rec_course


window.mainloop()
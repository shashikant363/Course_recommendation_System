from tkinter import *

window=Tk()
window.title("COURSE RECOMMENDATION SYSTEM")
window.geometry('870x600')
window['bg'] = '#5d8a82'
def next1():
    import GCrec
def next2():
    #window.destroy()
    import GPgrade

lbA=Label(window,text="WELCOME  TO  COURSE  RECOMMENDATION  SYSTEM",fg='blue',font=('Arial',20)).place(x=60,y=40)
btn1=Button(window,text="GRADE PREDICTION",fg='blue',font=('Arial',14),command=next2).place(x=150,y=150) #,command=pre_grae
btn2=Button(window,text="COURSE RECOMMENDATION",fg='blue',font=('Arial',14),command=next1).place(x=440,y=150)  #,command=rec_course

window.mainloop()
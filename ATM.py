from tkinter import*
from tkinter import messagebox
global bal
global txt1
global x
global label2,label3,btnca,btnt,btnpr,bal2,txtu,window,z
bal2=1000
z=0
x=0
def returnbal():
    label2.destroy()
    label3.destroy()
    btnt.destroy()
    btnpr.destroy()
    firstwin()


def return1():
    global label2,txt1
    label2.destroy()
    label3.destroy()
    txt1.destroy()
    btnca.destroy()
    btnt.destroy()
    btnpr.destroy()
    firstwin()



def submit(x):
    global bal2,z,txtu,window,txt1

    if x==2:
        bal2 = bal2+int(txt1.get())
        print(bal2)

        messagebox.showinfo("Info", "Deposit Request Successful!")

    elif x==1:

        if int(txt1.get()) <= bal2:
            bal2 = bal2-int(txt1.get())
            print(bal2)

            messagebox.showinfo("Your Balance", "Withdrawal Request Successful!")
        else:
            messagebox.showinfo("Error occurred", "Your selected amount was higher than your balance!")
    else:
        z = txtu.get()
        window2.destroy()
        window = Tk()
        window.geometry("200x390")
        firstwin()



def withdraw():
    global txt1
    global label2, label3, btnca, btnt, btnpr
    x=1
    label1.destroy()
    btnDe.destroy()
    btnWi.destroy()
    btnSu.destroy()
    btne.destroy()
    label2 = Label(window, text="Options")
    label2.grid(column=0, row=0, pady=20, padx=40)
    label3 = Label(window, text="Amount:")
    label3.grid(column=0, row=1, pady=10, padx=40)
    txt1 = Entry(window, width=20)
    txt1.grid(column=0, row=2, pady=20, padx=40)
    btnca = Button(window, text="Submit",bg="light green",width=15, height=2,command=lambda:submit(x))
    btnca.grid(column=0, row=3, pady=20, padx=40)
    btnpr = Button(window, text="Previous Page", width=15, height=2, command=return1)
    btnpr.grid(column=0, row=4, pady=20, padx=40)
    btnt = Button(window, text="Exit", width=15,bg="Red", height=2, command=exit)
    btnt.grid(column=0, row=5, pady=10, padx=40)

def deposit():
    global txt1
    global label2, label3, btnca, btnt, btnpr
    x=2
    label1.destroy()
    btnDe.destroy()
    btnWi.destroy()
    btnSu.destroy()
    btne.destroy()
    label2=Label(window,text="Options")
    label2.grid(column=0,row=0,pady=20,padx=40)
    label3=Label(window,text="Amount:")
    label3.grid(column=0, row=1,pady=10,padx=40)
    txt1= Entry(window,width=20)
    txt1.grid(column=0, row=2,pady=20,padx=40)
    btnca= Button(window,text="Submit",width=15,bg="light green", height=2,command=lambda:submit(x))
    btnca.grid(column=0, row=3,pady=20,padx=40)
    btnpr = Button(window, text="Previous Page", width=15, height=2, command=return1)
    btnpr.grid(column=0, row=4, pady=20, padx=40)
    btnt = Button(window,text="Exit",  width=15, height=2,bg="Red",command=exit)
    btnt.grid(column=0, row=5, pady=10, padx=40)


def exit():
    window.destroy()
def balance():
    global label2,label3,txt1
    label1.destroy()
    btnDe.destroy()
    btnWi.destroy()
    btnSu.destroy()
    btne.destroy()
    btnpr = Button(window, text="Previous Page", width=15, height=2, command=returnbal)
    btnpr.grid(column=0, row=3, pady=20, padx=40)
    btnt = Button(window, text="Exit", width=15, height=2, bg="Red", command=exit)
    btnt.grid(column=0, row=4, pady=10, padx=40)
    label2=Label(window,text="Your Balance: ")
    label2.grid(column=0,row=0,pady=20,padx=40)
    label3 = Label(window,text=str(bal2)+"$")
    label3.grid(column=0, row=1, pady=20, padx=40)



def firstwin():

    global label1, btnt,btnpr,btnca,btnDe,btnWi,btnSu,btne,txt1
    label1=Label(window,text="Welcome, "+z)
    label1.grid(column=0,row=0,pady=20, padx=40)

    btnDe = Button(window,text="Deposit", bg="light green",width=15,height=2,command=deposit)
    btnDe.grid(column=0,row=1, pady=10,padx=40)

    btnWi = Button(window,text="Withdraw", bg="light green",width=15,height=2,command=withdraw)
    btnWi.grid(column=0,row=2,pady=10,padx=40)

    btnSu = Button(window,text="Balance", bg="light green",width=15,height=2,command=balance)
    btnSu.grid(column=0,row=3,pady=10,padx=40)

    btne = Button(window,text="Exit", bg="light green",width=15,height=2,command=exit)
    btne.grid(column=0,row=4,pady=10,padx=40)

def name():
    x=3
    global z,window2,txtu,txt1
    window2 = Tk()
    label1 = Label(window2, text="Welcome!")
    label1.grid(column=0, row=0, pady=20, padx=40)
    label2 = Label(window2, text="Name:")
    label2.grid(column=0, row=1)
    txtu = Entry(window2, width=20)
    txtu.grid(column=0, row=2)

    btnca = Button(window2, text="Submit", width=15, bg="light green", height=2, command=lambda:submit(x))
    btnca.grid(column=0, row=3, pady=20, padx=40)
name()

window2.mainloop()
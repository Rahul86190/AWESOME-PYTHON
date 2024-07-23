
import tkinter as tk
from tkinter import messagebox
import time
root=tk.Tk()
root.title("MY BANK")
root.configure(background="BLACK")
a=S=str(20000)

PIN=int(900112)
name="rahul saini"
AN=str("22EAIAD090")

l0=tk.Label(text="Welcome to our website NIRA BANK OF WORLD",fg="blue")
l0.grid(row=0,column=3)

l1=tk.Label(text="PLEASE enter your name here")
l1.grid(row=1,column=0)
e1=tk.Entry(root,fg="brown",width=20)
e1.grid(row=1,column=1)

pinL1=tk.Label(text="ENTER PIN",width=25)
pinL1.grid(row=1,column=5)
pinE2=tk.Entry(root,fg="brown",width=10)
pinE2.grid(row=1,column=6)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label1.config(text=current_time)
    root.after(1000, update_time)  # Schedule the function to be called after 1000 milliseconds (1 second)

label1 = tk.Label(root, font=('calibri', 20, 'bold'), background='purple', foreground='white')
label1.place(x=1400,y=1)
update_time()

def login():
    n1=e1.get()
    p1=int(pinE2.get())

    if n1==name and p1==PIN:
        messagebox.showinfo("Login","Login Successful")
        l2=tk.Label(text=n1+" You have successfully entered")
        l2.grid(row=3,column=1)
        l1.grid_remove()
        b1.grid_remove()
        
        e1.grid_remove()
        pinE2.grid_remove()
        pinL1.grid_remove()

        l3=tk.Label(text="Which task you have to Perform ")
        l3.grid(row=4,column=0)
        l4=tk.Label(text="1. Balance Enquiry",width=20,height=1)
        l4.grid(row=6,column=0)
        l5=tk.Label(text="2. Cash Withdrawal",width=20,height=1)
        l5.grid(row=7,column=0)
        l6=tk.Label(text="3. Cash Deposit   ",width=20,height=1)
        l6.grid(row=8,column=0)
        l7=tk.Label(text="4. Chnage PIN NO. ",width=20,height=1)
        l7.grid(row=9,column=0)
        l8=tk.Label(text="5. Fund Transfer   ",width=20,height=1)
        l8.grid(row=10,column=0)
        l9=tk.Label(text="6. Exit...........",width=20,height=1)
        l9.place(x=16,y=405)

        b2=tk.Button(text="Check",command=balance,width=20,height=1 ,fg="brown")
        b2.grid(row=6,column=1)

        b3=tk.Button(text="Withdraw",command=withdraw,width=20,height=1 ,fg="brown")
        b3.grid(row=7,column=1)

        b4=tk.Button(text="Deposite",command=deposite ,width=20,height=1,fg="brown")
        b4.grid(row=8,column=1)

        b6=tk.Button(text="Change Pin",command=Change ,width=20,height=1,fg="brown")
        b6.grid(row=9,column=1)

        b5=tk.Button(text="GO for Transfer",command=FT,width=20,height=1,fg="brown")
        b5.grid(row=10,column=1)


        b7=tk.Button(text="Exit",command=exit ,width=20,height=1,fg="brown")
        b7.place(x=500,y=400)

    elif n1 != name:
        messagebox.showerror("Login","Invalid Name")
        l2=tk.Label(text="Invalid User Name")
        l2.grid(row=3,column=1)
    else:
        messagebox.showerror("Login","Invalid Pin")
        l2=tk.Label(text="Invalid Password")
        l2.grid(row=3,column=1)
    l1.grid_remove()
    b1.grid_remove()
        
    e1.grid_remove()
    pinE2.grid_remove()
    pinL1.grid_remove()

        
        

def withdraw():
    
    global a
    B=a
    l11=tk.Label(text="Enter amount to withdraw ->")
    l11.grid(row=7,column=2)

    def W1():
  
        M=e2.get()
        M1=int(M)
        g1=int(B)
        
        
        if M1<=g1:
            l12=tk.Label(text="Money withdrawl...")
            l12.grid(row=8,column=3)
            messagebox.showinfo("WITHDRAW ",M+"₹ Money SUCCESSFULLY withdrawl from your account ")
            
            l12.grid_remove()
            b8.grid_remove()
            e2.grid_remove()
            l11.grid_remove()
            global S
            S=g1-M1
            messagebox.showinfo("LEFT AMMOUNT","₹"+str(S)+" are left in your account ")
        else:
            l12=tk.Label(text=" INVALID...")
            l12.grid(row=8,column=3)
            messagebox.showinfo(" INVALID WITHDRAW ",M+"₹ Amount can't be able to withdraw \n Your Account Has Insufficient Balance ")
            l12.grid_remove()
            b8.grid_remove()
            e2.grid_remove()
            l11.grid_remove()

    e2=tk.Entry()
    e2.grid(row=7,column=3)
    b8=tk.Button(text="Get money",command=W1,width=20,height=1,fg="brown")
    b8.grid(row=7,column=4)


def deposite():
    global a
    B=a

    l13=tk.Label(text="Enter amount to DEPOSITE (One time limit 50000) ->")
    l13.grid(row=8,column=2)

    def D1():
  
        M=e3.get()
        M1=int(M)
        g1=int(B)

        if M1<=50000:
            l14=tk.Label(text="Money Deposited...")
            l14.grid(row=9,column=3)
            messagebox.showinfo("DEPOSITE ",M+"₹ Money SUCCESSFULLY Deposited in your account ")
            
            l14.grid_remove()
            b9.grid_remove()
            e3.grid_remove()
            l13.grid_remove()
            global S
            S=g1+M1
            messagebox.showinfo("AMMOUNT","TOTAL Amount in your account is ₹"+str(S))
        else:
            l14=tk.Label(text=" INVALID...")
            l14.grid(row=9,column=3)
            messagebox.showinfo(" INVALID WITHDRAW ",M+"₹ Amount can't be able to deposite \n One time limit is 50000 ")
            l14.grid_remove()
            b9.grid_remove()
            e3.grid_remove()
            l13.grid_remove()

    e3=tk.Entry()
    e3.grid(row=8,column=3)

    b9=tk.Button(text="Deposite money",command=D1,width=20,height=1,fg="brown")
    b9.grid(row=8,column=4)


def Change():
    l15=tk.Label(text="Enter your current PIN -> ")
    l15.grid(row=9,column=2)

    e4=tk.Entry(root)
    e4.grid(row=9,column=3)

    def c1():
        E1=int(e4.get())
        
        if E1==PIN:
            messagebox.showinfo("PIN CHECKING...","Successfully checked...\nYou may proceed to cahnge your PIN")
            l15.grid_remove()
            l16=tk.Label(text="Enter your new PIN -> ")
            l16.grid(row=9,column=2)
            e4.grid_remove()
            e5=tk.Entry(root)
            e5.grid(row=9,column=3)
            
            def c2():
                global PIN
                PIN=int(e5.get())
                messagebox.showinfo("PIN CHANGED...","Successfully changed your PIN\nNew PIN = "+e5.get())
                l16.grid_remove()
                e5.grid_remove()
                b11.grid_remove()
                
                
            b11=tk.Button(text="Change PIN",command=c2,width=20,height=1,fg="brown")
            b11.grid(row=9,column=4)

            b10.grid_remove()
            
            l15.grid_remove()

        else:
            messagebox.showinfo("PIN CHECKING...","Invalid PIN\nPlease try again")
            b10.grid_remove()
            e4.grid_remove()
            l15.grid_remove()
            
    
    b10=tk.Button(text="Confirm",command=c1,width=20,height=1,fg="brown")
    b10.grid(row=9,column=4)

def FT():
    l17=tk.Label(text="MY Account NO.")
    l17.grid(row=10,column=2)
    e6=tk.Entry(root)
    e6.grid(row=11,column=2)
    l18=tk.Label(text="Transfer To (Account no.)")
    l18.grid(row=10,column=3)
    e7=tk.Entry(root)
    e7.grid(row=11,column=3)
    l19=tk.Label(text="Amount")
    l19.grid(row=10,column=4)
    e8=tk.Entry(root)
    e8.grid(row=11,column=4)
    l20=tk.Label(text="YOUR PIN")
    l20.grid(row=10,column=5)
    e9=tk.Entry(root)
    e9.grid(row=11,column=5)
    S1=S
    def FT1():
        AC1=e6.get()
        AC2=e7.get()
        amount=int(e8.get())
        CP=int(e9.get())
        
        if AC1==AN and CP==PIN and amount<=int(S1):
            global S
            S=int(S1)-int(amount)
            messagebox.showinfo("TRANSFER","Successfully transferred\nAmount = "+str(amount)+"\nIn Account NO. "+AC2)
            l17.grid_remove()
            e6.grid_remove()
            l18.grid_remove()
            e7.grid_remove()
            l19.grid_remove()
            e8.grid_remove()
            l20.grid_remove()
            e9.grid_remove()
            b12.grid_remove()
            
        else:
            if AC1!=AN:
                messagebox.showinfo("TRANSFER","Your Invalid Account No.\nPlease try again")
            elif CP!=PIN:
                messagebox.showinfo("TRANSFER","Invalid PIN\nPlease try again")
            else:
                messagebox.showinfo("TRANSFER","Insufficient Balance\nPlease try again")
            l17.grid_remove()
            e6.grid_remove()
            l18.grid_remove()
            e7.grid_remove()
            l19.grid_remove()
            e8.grid_remove()
            l20.grid_remove()
            e9.grid_remove()
            b12.grid_remove()


    b12=tk.Button(text="SEND",command=FT1,width=20,height=1,fg="brown")
    b12.grid(row=16,column=3)


def balance():
    global a
    a=str(S)
    l10=tk.Label(text="Your balance is ₹"+a)
    l10.grid(row=6,column=2)


b1=tk.Button(text="Submit",command=login ,width=20,height=1,fg="brown")
b1.grid(row=3,column=3)



root.mainloop()

import tkinter as tk
import random
root =tk.Tk()
from tkinter import messagebox
root.geometry("400x400")
root.title("DATE PROPOSAL")
root.config(background="pink")

def yes():
    l3=tk.Label(text="yehhhhhh !!!!!!  lets go ",font=("bold",40))
    l3.place(x=400,y=350)
    messagebox.showinfo("!!!!!   HURRRREYY   !!!!! ","DATE PROPOSAL ACCEPTED😁❤️    ^_^")

def move_button(event):
    window_width=root.winfo_width()
    window_height=root.winfo_height()

    new_x=random.randint(0,window_width - b2.winfo_width())
    new_y=random.randint(0,window_height - b2.winfo_height())

    b2.place(x=new_x,y=new_y)
l1=tk.Label(text="DO YOU LIKE to DATE ME ❤️ ",font=("bold",30))
# l1.grid(row=3,column=6)
l1.place(x=400,y=100)

b1=tk.Button(text="yes",command=yes,fg="blue")
b1.place(x=500,y=200)
b2=tk.Button(root,text="NO",fg="red")
b2.place(x=500,y=250)
b2.bind("<Enter>",move_button)
root.mainloop()

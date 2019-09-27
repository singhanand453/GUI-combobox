from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
window=Tk()
window.geometry("400x300")
window.title("combobox")
label1=Label(window,text="enter your name : ")
label1.grid(row=0,column=1,pady="2")
entry=Entry(window)
entry.grid(row=0,column=2,pady="2",ipady="1")

label=Label(window,text="select your  city : ")
label.grid(row=2,column=1,pady="1")

combobox=Combobox(window,state="readonly",values=("noida","Agra","lucknow","agra","delhi"),background="gray")
combobox.grid(row=2,column=2,pady="2",ipady="1")
def submit_button():
    messagebox.showinfo("Mess-age","Your city: "+combobox.get())

button=Button(window,text="sub-mit",command=submit_button)
button.grid(row=3,column=2)

window.mainloop()

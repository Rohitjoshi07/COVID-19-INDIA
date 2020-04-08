import tkinter
from tkinter import *
import corona
from corona import *

def update():
    list1.delete(0,END)
    list2.delete(0, END)
    list3.delete(0, END)
    list4.delete(0, END)
    list5.delete(0, END)
    list1.insert(END, corona.totalcases())
    list2.insert(END, corona.activecases())
    list3.insert(END, corona.deaths())
    list4.insert(END, corona.recovered())
    list5.insert(END, corona.time())

window=Tk()

window.wm_title("COVID-19/INDIA")

l1=Label(window,text="Total cases",width=10,font=10,bg="maroon")
l1.grid(row=0,column=0)
l2=Label(window,text="Active cases",font=10,width=10,bg="Grey")
l2.grid(row=1,column=0)
l3=Label(window,text="Deaths",width=10,font=10,bg="maroon")
l3.grid(row=2,column=0)
l4=Label(window,text="Recovered",width=10,font=10,bg="Grey")
l4.grid(row=3,column=0)
l5=Label(window,text="Time",width=10,font=10,bg="Maroon")
l5.grid(row=4,column=0)

list1=Listbox(window,height=1,width=20)
list1.grid(row=0,column=1,rowspan=1,columnspan=2)
list2=Listbox(window,height=1,width=20)
list2.grid(row=1,column=1,rowspan=1,columnspan=2)
list3=Listbox(window,height=1,width=20)
list3.grid(row=2,column=1,rowspan=1,columnspan=2)
list4=Listbox(window,height=1,width=20)
list4.grid(row=3,column=1,rowspan=1,columnspan=2)
list5=Listbox(window,height=1,width=20)
list5.grid(row=4,column=1,rowspan=1,columnspan=2)


b2=Button(window,text="Update",width=10,bg="maroon",font=10,command=update)
b2.grid(row=2,column=3)

b1=Button(window,text="Close",width=10,bg="Grey",font=10,command=window.destroy)
b1.grid(row=5,column=2)

window.mainloop()

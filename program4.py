from tkinter import *
from tkinter import messagebox
import os
import time

counter=900
   
def counter_label(label):
   def count():
    global counter
    counter= counter-1
    label.config(text=str(counter))
    label.after(1000, count)
   count()

sdef systempause():
   os.system("pause")
 
 
root = Tk()
root.title("Timer")
label = Label(root, fg="dark green")
label.pack()
counter_label(label)
button =Button(root, text='Stop', width=25, command=systempause)
button.pack()
root.mainloop()





"""
from tkinter import *
from tkinter import messagebox
import os
import time
top = Tk()
top.geometry("100x100")
def timer1():
   t=60
   while t:
       print(t//60,":",t%60)
       time.sleep(1)
       t=t-1


def timer2(self,timer1):
   self.timer1()
   

B1 = Button(top, text = "Player1", command = timer1)
B2= Button(top,text="stop",command=timer2)
B1.place(x = 35,y =50)
B2.place(x = 90,y=50)

top.mainloop()
"""

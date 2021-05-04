from tkinter import *

top = Tk ()

def results ():
    result = E1.get ()
    print (result)
    print (type(result))

L1 =  Label (top, text="helow world ")
# this is a lable wiget 
L1.grid(column= 0, row= 1)
#this is a entry wiget 

E1  = Entry (top, bd = 5 )
E1.grid (column= 2 , row= 2)
 #this is a button wiget

B1 = Button (text="     get data      ",bg="blue",   command= results )
B1.grid(column = 0, row= 3)
top.mainloop () 


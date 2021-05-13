from tkinter import  *
import random

top = Tk()
playlist = []
myRolls = []
dieTypes = 0
rollTimes = 0 

def results():
    result = E1.get()
    playlist.append(result)
    E1.delete(0, END)
    
def printList():
    print(playlist)

def exportList():
    with open('test.txt', 'w') as f:
        for item in list:
            f.write("%s/n" % item)

def clearWindow ():
    for widget in top .winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    Lmain = Label(top, text="block 5 gui projects")
    Lmain.grid(column= 0, row= 1)
    B1main = Button (text = " week 1 ", bg="white", command = week1)
    B1main.grid (column= 0, row = 2)
    B2main = Button (text = " week 2 ", bg="red", command = week2 )
    B2main.grid (column= 0, row = 3)
    B3main= Button (text = " +week 3", bg="red", )
    B3main.grid (column= 0, row = 4)


def week1():
     clearWindow()
     def results():
         result = E1.get()
         playlist.append(result)
         E1.delete(0, END)
    #this is a label widget
    L1 = Label(top, text="Playlist generator")
    L1.grid(column= 0, row= 1)

    #this is a entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)


    #This is a button widget
    B1 = Button (text = " + ", bg="red", command = results)
    B1.grid (column= 1, row = 3)

    B2 = button(text = "print ", bg = "light blue", command = )
    B2.grid(column = 2, row = 2)     

    B3 = Button (text = "exportList ", bg = "#B4FFCD", command = exportList)
    B3.grid(column = 0, row = 3)     

    Bexit = Button (text = "main menu ", bg = "#B4FFCD", command = mainMenu)
    Bexit.grid(column = 0, row = 3)

def week2():
    def rollDice ()
    dieType = E2Week2.get()
    rollTimes = E1Week2.get()
    clearWindow()
    for x in range(0, int (rollTimes)):
        myRolls.append(random.randint(1, int(dieType)))

    L4Week2 = Label()
    L5Week2 = Lable()
    b2Week2 = Button()
        
        



    
    clearWindow()
    B1Week2= Button (text = "roll em", bg="yellow")
    B1week2.grid(column= 2 , row=  4)
    
    L1Week2 = label(top, text= "dice roller app")
    L1week2.grid(column= 2 , row=  1)
    
    L2Week2 = label(top, text="# of rolls")
    L2week2.grid(column= 0, row= 2 )

    L3Week2 = label(top, text="# of sides")
    L3week2.grid(column= , row= 3)

    E1week2 = Entry(top, bd = 5 )
    E1week2.grid(column= 0, row= 3)

    E2week2 = Entry(top, bd= 5 )
    E2week2.grid(column= 3, row= 3)




    
if __name__="__main__":
    mainMenu()
    top.mainloop()
top.mainloop()

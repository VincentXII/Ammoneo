import subprocess, sys, os, shutil, tkinter, csv
from tkinter import *

class Ammoneo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()

root = Tk()
readvar = StringVar()

kaiser = Ammoneo(master=root)
kaiser.master.title("Ammoneo GUI v0.1")

f= Frame(root, height=300, width=500)
f.pack_propagate(0)
f.pack()

L = Label(root, anchor=NE, text="Kaiser GUI v0.1")
L.pack()

def newlist():
    new = input("Name of New List: ")
    new = new + ".vtdl"
    firstremind = input("First Reminder: ")
    with open(new, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([firstremind])

def readlist():
    read = readvar.get()
    read = read + ".vtdl"
    f = open(read, 'r')
    reader = csv.reader(f)
    for row in reader:
        print (','.join(row))
        mlabel2 = Label(root,text=row).pack()

def exit():
    global root
    root.quit()


mEntry = Entry(root,textvariable=readvar).pack()

newlist = Button(root, text="Create New List", command=newlist)
newlist.pack() 

readlist = Button(root, text="Read List", command=readlist)
readlist.pack()

exit = Button(root, text="Exit", command=exit)
exit.pack(fill=BOTH, expand=1)

mainloop()


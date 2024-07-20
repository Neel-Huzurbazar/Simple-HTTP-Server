import tkinter
from tkinter import *
import os
import socket
from tkinter import filedialog
from tkinter import messagebox

string=""
file=""

def choose():
    global file
  
    file = filedialog.askdirectory()
    print(file)
    r.delete(0,END)
    r.insert(0,file)
    first=file[0:2]
    last=file[2:]
    global string
    string="cmd /k {t} ^& cd {u} ^& python -m http.server".format(t=first ,u=last)
    #print(string)

'''
def singleFile():
    file=filedialog.askopenfilename(parent=win, initialdir= "/", title='Please select a directory')
    print(file)
    first=file[0:2]
    last=file[3:]
  #  ind=last.index('/')
  #  mid=file[ind:5]
   # print(mid)
    print(first)
    print(last)
    global string
    string="cmd /k {t} ^& cd {u} ^& python -m http.server".format(t=first ,u=last)
    print(string)

'''

def com():
    print("string="+string)
    if(file==""):
        tkinter.messagebox.showinfo("Server","Please select a folder")
    else:
        os.system(string)

def help_():
    win=Tk()
    win.geometry('400x200')
    win.resizable(0,0)
    win.iconbitmap("S.ico")
    win.title("Help")
    s='''\nThe server chooses folders to display.\nIn order to display a single file ,move it into a folder and then choose that folder.\nThe content you choose will only be visible to\n people present in the same network.\nDo not close terminal unless your are done.\n
    '''
    t=Text(win)
    t.insert(END,s.rjust(10))
    t.config(state='disabled')
    t.place(x=0,y=0,w=400,h=200)
    
def stop():
    exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
v=s.getsockname()[0]
s="http://"+v+':8000'
    
win=Tk()
win.resizable(0,0)
win.geometry('300x320')
win.iconbitmap("S.ico")
win.title("Simple HTTP Server")

menu=Menu(win)
menu.add_command(label="Help",command=help_)
win.config(menu=menu)



l1=Label(win,text="Server localhost url:-")
l1.place(x=10,y=20)

en=Entry(win,fg="black")
en.place(x=140,y=20)

b=Button(win,text="Start",bg="red",command=com)
b.place(x=260,y=130)

be=Button(win,text="Select Folder",bg="red",command=choose)
be.place(x=10,y=130)

r=Entry(win,width=26)
r.place(x=94,y=133)


en.insert(0,"http://localhost:8000")

p=Label(win,text="(same machine)").place(x=10,y=37)

l3=Label(win,text="To access server from\nanothe machine use:-").place(x=10,y=75)

e=Entry(win)
e.place(x=140,y=80)
e.insert(0,s)
#e.configure(state='disabled')

l4=Label(win,text="*Note:- This server will work in the same network \n only and can not be accessed outside network",fg="red").place(x=10,y=180)

l5=Label(win,text="Designed and developed by Neel Huzurbazar",fg="blue").place(x=10,y=250)
l2=Label(win,text="Do not close the command prompt(cmd) ",fg="red")
l2.place(x=10,y=220)


win.mainloop()



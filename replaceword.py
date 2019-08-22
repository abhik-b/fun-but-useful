import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog



root=tkinter.Tk()

root.geometry("500x500")
# root.resizable(0,0)
root.title("Replace_Word") 






style=ttk.Style()
style.configure('TEntry',foreground = '#151515',background="#151515")

data=StringVar()
# text=input("anythin")
selectdata=StringVar()
replacedata=StringVar()

uppa=Frame(root,bg="#151515")
uppa.pack(expand=True,fill = "both")

wdtor=Label(
    uppa,
    text="word to replace",
    # anchor=SE,
    font=("Verdana",22),
    
    bg="#151515",
    fg="#fff"
)
wdtor.pack(expand=True,fill="both") 

# def btnclick():
#     filename_path = filedialog.askopenfilename()
#     f=open(filename_path,"r")
#     contents=f.read()
    # print("Previous ",contents)
    
        
    # data.set(contents)

def btn2click():
    
    filename_path = filedialog.askopenfilename()
    f=open(filename_path,"r")
    contents=f.read()
    data.set(contents)
    sd=selectdata.get()
    rd=replacedata.get()
    contents=contents.replace(sd,rd)
    
    f.close()

    f=open(filename_path,"wt")
    f.write(contents)
    # print("\n\n NaWW!!!! ",contents)
    data.set(contents)
    f.close()
    





entry=ttk.Entry(uppa,textvariable=selectdata,font=( 'verdana',20,'bold'),foreground="green")
entry.pack(expand=True)

wrdr=Label(
    uppa,
    text="replaced word",
    # anchor=SE,
    font=("Verdana",22),
    
    bg="#151515",
    fg="#fff"
)
wrdr.pack(expand=True,fill="both") 

entry2=ttk.Entry(uppa,textvariable=replacedata,font=( 'verdana',20,'bold'),foreground="red")
entry2.pack(expand=True)
midd=Frame(root,bg="#151515")
midd.pack(expand=True,fill = "both")
# btn1=Button(
#     lowerframe,
#     text="say",
#     font=("Verdana",22),
#     relief= GROOVE,
#     border=0,
#     command=btnclick,
#     bg="#111111",
#     fg="#585858"
    
# )
# btn1.pack(side=LEFT,expand =True,fill ="both")

btn2=Button(
    midd,
    text="replace",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
    command=btn2click,
    bg="#151515",
    fg="#00ff5e"
    
)
btn2.pack(expand =True,fill ="both")

lowerframe=Frame(root,bg="#151515")
lowerframe.pack(expand=True,fill = "both")

lbl=Label(
    lowerframe,
    text="Label",
    # anchor=SE,
    font=("Verdana",22),
    textvariable=data,
    bg="#151515",
    fg="#fff"
)
lbl.pack(expand=True,fill="both")  

root.mainloop()
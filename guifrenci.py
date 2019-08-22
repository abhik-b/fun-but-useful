from tkinter import *
import speech_recognition as sr 
from textblob import TextBlob

root=Tk()
root.title("guifrenci")
root.configure(bg="#151515")

data=StringVar()
data2=StringVar()

def btnclick():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Anything \n\n")
        audio=r.listen(source)
        

        try:
            text=r.recognize_google(audio)
            print("you said   {}".format(text))
            data2.set("you said   {}".format(text))
            wrd=TextBlob(text)
            z=wrd.translate(from_lang='en', to='fr')
            print("\n French :   ",z)
            data.set("\n French :  {} ".format(str(z)))
            
        except:
            data.set("sorry man samajh nei aya")



lbl=Label(root,text="hi there",bg="#151515",fg="#fff",font='Verdana 25 italic',textvariable=data2)
lbl.pack(expand=True,fill='both')
lbl1=Label(root,text="hi there",bg="#151515",fg="#fff",font='Verdana 25 italic',textvariable=data)
lbl1.pack(expand=True,fill='both')
btn1=Button(root,text="SPEAK",bg="#151515",fg="#00ff5e",font='Verdana 50 bold',border=0,command=btnclick)
btn1.pack(expand=True,fill='both')



root.mainloop()
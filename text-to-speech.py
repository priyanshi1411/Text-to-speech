from tkinter import *
import pyttsx3
root=Tk()
root.title('First GUI')
root.geometry('600x600') 
frame=Frame(root,width=600,height=600,background='Pink')
frame.place(x=0,y=0)
def speak():
    txt=E.get()
    
    tts=pyttsx3.init()
    rate=tts.getProperty('rate')
    tts.setProperty('rate',rate-100)
    voices=tts.getProperty('voices')      #For female voice
    tts.setProperty('voice',voices[1].id)  
    tts.say(txt)
    
    print(txt)
    tts.runAndWait()
L=Label(frame,text='Enter Text')
L.place(x=50,y=200)
B=Button(root,text='speak now',command=speak)
B.place(x=250,y=300)
E=Entry(root)
E.place(x=150,y=200)
root.mainloop()

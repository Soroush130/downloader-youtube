from ctypes import sizeof
from tkinter import *
from pytube import YouTube

root = Tk()
root.title("Downloader YouTube")
root.geometry('500x300')
root.resizable(0,0)
link = StringVar()
# =======================  FUNCTIONS ==============================
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 13').place(x= 180 , y = 210)  
# ======================= ENTRY ==============================
e1 = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
# ======================= LABELS ==============================
l1 = Label(root, text="Welcome to downloader youtube", font ='arial 15 bold').place(x=100,y=0)
l2 = Label(root, text="Paste Link Here:", font ='arial 10 bold').place(x=200,y=55)
# ======================= BOUTTON ==============================
Button(root,text = 'DOWNLOAD', font = 'arial 12 bold' , padx = 2, command = Downloader).place(x=200 ,y = 130)
root.mainloop()
import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
# from pytube import YouTube
import yt_dlp as youtube_dl
from PIL import ImageTk,Image

def download_func():
    link=video_link.get()
    yt_video={
           'outtmpl':r"C:\Users\User\Desktop\downloads\%(title)s.%(ext)s" 
    }
    with youtube_dl.YoutubeDL(yt_video) as ydl:
        ydl.download([link])

root=tk.Tk()
root.title("Youtube downloader")
root.geometry("900x362")
root.config()
root.resizable(0.0,0.0)
bg=ImageTk.PhotoImage(file=r"C:\Users\User\Desktop\Data Analytics\img2.png")
bg_label =Label(root,image=bg).place(x=0,y=0)
y1=tk.Label(text="YOUTUBE DOWNLOADER",font=("Segoe UI Black",25,"bold"),background="grey")
y1.grid(column=3,row=0)
z1=tk.Label(text="Paste your link here",font=("MV Boli",20,"bold"),background="grey")
z1.grid(column=3,row=1,pady=30)
video_link=tk.Entry(font=("Arial",28),width=40)
video_link.grid(column=3,row=2,padx=30)

btn_download=tk.Button(text="Download",bg='red',fg='white',relief='groove',font=("MV Boli",20),command=download_func)
btn_download.grid(column=3,row=3,pady=30)
root.mainloop()
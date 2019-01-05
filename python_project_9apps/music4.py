from tkinter import *
import tkinter as tk
import os
import re
import pygame
from tkinter.filedialog import askdirectory
listofsongs=[]
index=0
volume=0.5
class Application(Frame):
    
    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)

        self.grid()
        self.create_widgets()
    def playsong(event):
        pygame.mixer.music.play()

    def pausesong(event):
        pygame.mixer.music.pause()
    def resumesong(event):
        pygame.mixer.music.unpause()

    def nextsong(event):
        global index
        index+=1

        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        if index==2:
            index=0
    def prevsong(event):
        global index
        index-=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        if index==0:
            index=2
    def stopsong(event):
        pygame.mixer.music.stop()
    def get_volume():
        global volume
        volume=pygame.mixer.music.get_volume()

    def volume_up(event):
        global volume
        volume+=0.1
        pygame.mixer.music.set_volume(volume)
    def volume_down(event):
        global volume
        volume-=0.1
        pygame.mixer.music.set_volume(volume)
    def loop(event):
        global index
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    
    def directorychooser():
        global index
        directory=askdirectory()
        os.chdir(directory)
        for files in os.listdir(directory):
            if re.search(".ogg",files):


                listofsongs.append(files)
        print(listofsongs)
        pygame.init()

        pygame.mixer.music.load(listofsongs[index])

    directorychooser()

    def create_widgets(self):
        #listbox
        self.listbox=tk.Listbox(self,height=15,width=30,bg="cornsilk2")
        self.listbox.grid(row=0,columnspan=3)
        for items in listofsongs:
            self.listbox.insert(END,items)

        #playbutton
        self.play=PhotoImage(master=self,file="play.gif")
        self.button1 = tk.Button(self,text = "play",image=self.play, padx = 35, pady = 25,command=self.playsong,height=75,width=75,bg="black",activebackground="black")
        self.button1.image=self.play
        self.button1.grid(row = 1, column = 1, sticky = W)
        #pausebutton
        self.pause=PhotoImage(master=self,file="pause.gif")
        self.button2 = tk.Button(self,text = "pause",image=self.pause, padx = 33, pady = 25, bg="black",command=self.pausesong,height=75,width=75,activebackground="black")
        self.button2.grid(row = 2, column = 0, sticky = W)
        self.button2.image=self.pause

        #nextbuttton
        self.next=PhotoImage(master=self,file="next.gif")
        self.button3 = tk.Button(self,text = "next",image=self.next ,height=75,width=75,bg="black",padx = 33, pady = 25,command=self.nextsong,activebackground="black")
        self.button3.grid(row = 1, column = 2, sticky = W)
        self.button3.image=self.next


        #previousbutton
        self.prev=PhotoImage(master=self,file="prev.gif")
        self.button4 = tk.Button(self, text="previous",image=self.prev,height=75,width=75,bg="black",padx=25,pady=25,command=self.prevsong,activebackground="black")
        self.button4.grid(row = 1, column = 0, sticky = W)
        self.button4.image=self.prev

        #stop button
        self.stop=PhotoImage(master=self,file="stop.gif")

        self.button5 = tk.Button(self,text = "stop",image=self.stop,padx = 33, pady = 25,height=75,width=75,bg="black",command=self.stopsong,activebackground="black")
        self.button5.image=self.stop
        self.button5.grid(row = 2, column = 2, sticky = W)

        #resume button5
        self.resume=tk.PhotoImage(master=self,file="play.gif")
        self.button6=tk.Button(self,text="resume",image=self.resume,height=75,width=75,bg="black",padx=25,pady=25,command=self.resumesong,activebackground="black")
        self.button6.grid(row=2,column=1,sticky=W)
        self.button6.image=self.resume
        #volume_up
        self.volumeup=tk.PhotoImage(master=self,file="volume.gif")
        self.button7=tk.Button(self,text="volume up",image=self.volumeup,height=75,width=75,padx=19,pady=25,command=self.volume_up,bg="black",activebackground="black")
        self.button7.grid(row=3,column=0,sticky=W)
        self.button7.image=self.volumeup

        #volume down
        self.volume=tk.PhotoImage(master=self,file="mute.gif")
        self.button8=tk.Button(self,text="volume down",height=75,width=75,image=self.volume,padx=8,pady=25,command=self.volume_down,bg="black",activebackground="black")
        self.button8.grid(row=3,column=1,sticky=W)
        self.button8.image=self.volume
        
        self.loop_image =tk.PhotoImage(master=self,file="loop_on.gif")
        self.button9=tk.Button(self,height=75,width=75,image=self.loop_image,command=self.loop,activebackground="black",bg="black")       
        self.button9.grid(row=3,column=2,sticky=W)
        self.button9.image=self.loop_image


Music_player = Tk()

Music_player.minsize(200,300)
Music_player.title("Music player")
app = Application(Music_player)

Music_player.resizable(height=FALSE,width=FALSE)
Music_player.mainloop()

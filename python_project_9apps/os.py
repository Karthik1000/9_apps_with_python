import os
from tkinter import*

class Application(Frame):


    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
    def create_widget(self):
        self.cal=PhotoImage(file="cal.gif")  
    
    
        self.button1 = Button(self, text="Calculator",image=self.cal, command= lambda : os.system('python3 cal.py'))
        self.button1.grid(row=0, column=0)
        self.button1.image=self.cal

        self.mail=PhotoImage(file="mail.gif")
       	self.button2 = Button(self, text="Mail",image=self.mail, command=lambda: os.system('python3 mail.py'))
       	self.button2.grid(row=0, column=1)
       	self.button2.image=self.mail


        self.tic=PhotoImage(file="tic.gif")
        self.button3 = Button(self, text="Tic-Tac-Toe",image=self.tic, command=lambda: os.system('python3 tic.py'))
        self.button3.grid(row=0, column=2)
        self.button3.image=self.tic


        self.music=PhotoImage(file="music.gif")
        self.button4 = Button(self, text="Music",image=self.music, command=lambda: os.system('python3 music4.py'))
        self.button4.grid(row=1, column=0)
        self.button4.image=self.music
		
        self.game=PhotoImage(file="ball.gif")
        self.button5 = Button(self, text="paddle",image=self.game, command=lambda: os.system('python ball.py'))
        self.button5.grid(row=1, column=1)
        self.button5.image=self.game
        
        self.curr=PhotoImage(file="curr.gif")
        self.button6 = Button(self, text="currency",image=self.curr, command=lambda: os.system('python3 currency.py'))
        self.button6.grid(row=1, column=2)		
        self.button6.image=self.curr
        
        
        self.guess=PhotoImage(file="guss2.gif")
        self.button7 = Button(self, text="guessing",image=self.guess, command=lambda: os.system('python3 guess.py'))
        self.button7.grid(row=2, column=0)
        self.button7=self.guess
        
        self.editor=PhotoImage(file="img.gif")
        self.button8 = Button(self, text="editor",image=self.editor, command=lambda: os.system('python3 editor.py'))
        self.button8.grid(row=2, column=1)
        self.button8.image=self.editor
       
        
        
        self.main=PhotoImage(file="d3.gif")
        self.button9 = Button(self, text="text",image=self.main, command=lambda: os.system('python3 main.py'))
        self.button9.grid(row=2, column=2)
        self.button9.image=self.main
        

window = Tk()
app = Application(window)
window.title("APPThon")
window.mainloop()


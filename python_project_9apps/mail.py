from tkinter import*
import smtplib
import os
class email(Frame):

    def __init__(self, master):

        super(email, self).__init__(master)
        self.mail_text = StringVar()
        self.pass_text = StringVar()
        self.msg_text = StringVar()
        self.omail_text = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.label1 = Label(self,text="Your Email ID:")
        self.label1.grid(row=0, column=0)

        self.label2 = Label(self, text="Password:")
        self.label2.grid(row=1, column=0,sticky=W)

        self.label3 = Label(self, text="To:")
        self.label3.grid(row=2, column=0, sticky=W)

        self.label4 = Label(self, text="message:")
        self.label4.grid(row=3, column=0, sticky=W)


        e1=Entry(self,textvariable=self.mail_text,width = 24)
        e1.grid(row=0,column=1)


        e2 = Entry(self, textvariable=self.pass_text,show="*",width = 24)
        e2.grid(row=1, column=1)


        e3 = Entry(self, textvariable=self.omail_text,width = 24)
        e3.grid(row=2, column=1)


        e4 = Entry(self, textvariable=self.msg_text,width = 24)
        e4.grid(row=3, column=1)

        self.button1 = Button(self, text="Send Mail",command =self.mailing)
        self.button1.grid(row=4,column=1)



    def mailing(self):
        msg=self.msg_text.get()
        print("message:",msg)
        mail_text2= self.mail_text.get()
        pass1 = self.pass_text.get()
        omail_text2 = self.omail_text.get()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(mail_text2, pass1)

        server.sendmail(mail_text2, omail_text2, msg)
        print('Mail sent')
        server.quit()



window=Tk()
b = email(window)
window.title("Mail")
window.mainloop()


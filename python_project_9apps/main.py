from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

master=Tk()
master.title("Diary Entry")
master.geometry("400x400")
text=Text(master,width=400,height=400,bd=3)
text.pack()

def save():
	path=filedialog.asksaveasfilename()
	write=open(path,mode="w")
	write.write(text.get("1.0",END))

def close():
	ans=messagebox.askquestion(title="Save File",message="Do you really want to quit?")
	if ans is True:
		save()
		master.quit()
	
def cut():
	master.clipboard_clear()
	text.clipboard_append(string=text.selection_get())
	text.delete(INDEX1=SEL_FIRST,INDEX2=SEL_LAST)

def copy():
	#master.clipboard_clear()
	#text.clipboard.append(string=text.selection_get())
	text.append(string=text.selection_get())
def paste():
	text.clipboard.append(string=text.selection_get())
	
def delete():
	text.delete(index1=SEL_FIRST,index2=SEL_LAST)
	
def delete_all():
	text.delete(1.0,END)

def new():
	ans=messagebox.askquestion(title="Save File",message="Do you wish to save the current file?")
	if ans is True:
		save()
	delete_all()
	


def open_file():
	new()
	file=filedialog.askopenfile()
	text.insert(INSERT,file.read())
	
	
menu=Menu(master)
master.config(menu=menu)
file_menu=Menu(menu)
menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New",command=new)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save)
file_menu.add_command(label="close",command=close)

edit_menu=Menu(menu)
menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut",command=cut)
edit_menu.add_command(label="copy",command=copy)
edit_menu.add_command(label="paste",command=paste)
edit_menu.add_command(label="delete",command=delete)

master.title("Text editor")
master.mainloop()

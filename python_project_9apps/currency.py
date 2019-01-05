from tkinter import *
from tkinter import messagebox
from tkinter import StringVar,ttk
#import time
#import datetime

root=Tk()
root.title("Currency Converter")
root.geometry("1000x300+0+0")
root.configure(background="black")

leftmainframe=Frame(root,width=660,bd=8)
leftmainframe.pack(side=LEFT)

rightmainframe=Frame(root,width=200,bd=8)
rightmainframe.pack(side=RIGHT)

#DateofOrder=StringVar()
value0=StringVar()
convert=DoubleVar()
currency=DoubleVar()

def currency1():
	if value0.get()=="US Dollar":
		convert1=float(convert.get() * 0.015041)
		convert2="USA dollars",str('%.2f'%(convert1))
		currency.set(convert2)

	elif value0.get()=="Australian Dollar":
		convert1=float(convert.get() * 0.019948)
		convert2="AUS dollars",str('%.2f'%(convert1))
		currency.set(convert2)

	elif value0.get()=="Canadian Dollar":
		convert1=float(convert.get() * 0.019288)
		convert2="CANADA dollars",str('%.2f'%(convert1))
		currency.set(convert2)

	elif value0.get()=="Euro":
		convert1=float(convert.get() * 0.012465)
		convert2="Euro",str('%.2f'%(convert1))
		currency.set(convert2)

	elif value0.get()=="Swiss Franc":
		convert1=float(convert.get() * 0.014919)
		convert2="Franc",str('%.2f'%(convert1))
		currency.set(convert2)

	elif value0.get()=="Malaysian Ringitt":
		convert1=float(convert.get() * 0.059000)
		convert2="Ringitts",str('%.2f'%(convert1))
		currency.set(convert2)

	elif value0.get()=="British Pound":
		convert1=float(convert.get() * 0.010936)
		convert2="Pounds",str('%.2f'%(convert1))
		currency.set(convert2)





def qexit():
	ans=messagebox.askyesno(title="Exit",message="Do you wish to close the program?")
	if ans > 0:
		root.destroy()
		return
		

def reset():
	value0.set("")
	convert.set("0.0")
	currency.set("0.0")

EntCurrency=Entry(leftmainframe,font=('arial',20,'bold'),textvariable=convert,bd=2,width=28,justify='center')
EntCurrency.grid(row=0,column=1)

lblindianrupee=Label(leftmainframe,font=('arial',20,'bold'),text='Indian Rupees equals',padx=2,pady=2,bd=2,fg='black',width=18)
lblindianrupee.grid(row=0,column=2)

box=ttk.Combobox(leftmainframe,textvariable=value0,state="readonly",font=('arial',20,'bold'),width=20)
box['values']=(' ','Australian Dollar','Canadian Dollar','Euro','Swiss Franc','Malaysian Ringitt','British Pound','US Dollar')
box.current(0)
box.grid(row=4,column=2)

lblCurrency=Label(leftmainframe,font=('arial',20,'bold'),textvariable=currency,bd=2,width=25,bg='white',pady=2,padx=2)
lblCurrency.grid(row=4,column=1)

btnConvert=Button(rightmainframe,text="Convert",padx=2,pady=2,bd=2,fg="black",font=('arial',20,'bold'),width=12,height=1,command=currency1).grid(row=1,column=0)


btnReset=Button(rightmainframe,text="Reset",padx=2,pady=2,bd=2,fg="black",font=('arial',20,'bold'),width=12,height=1,command=reset).grid(row=2,column=0)


btnExit=Button(rightmainframe,text="Exit",padx=2,pady=2,bd=2,fg="black",font=('arial',20,'bold'),width=12,height=1,command=qexit).grid(row=3,column=0)

root.mainloop()


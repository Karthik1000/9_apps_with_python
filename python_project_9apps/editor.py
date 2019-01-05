from tkinter import *
from tkinter import filedialog
from PIL import Image
import random

def openfn():
	filename = filedialog.askopenfilename(title='open')
	return filename

def resizeImage():
	path = openfn()
	image = Image.open(path)
	#label=Label(root,image=image)
	#label.pack()
	image = image.resize((20,20),Image.ANTIALIAS)
	image.save('{}.png'.format(random.randint(12345,21322)))
	print('resized and Saved!')
	
def rightrotate():
	path=openfn()
	image=Image.open(path)
	rightimage=image.rotate(-90)
	#rightimage.show()
	#label1=Label(root,image=rightimage)
	#label1.pack()

	#rightimage=image.transpose(Image.FLIP_RIGHT_LEFT)
	rightimage.save('{}.png'.format(random.randint(12345,21322)))
	print('rotated!')

def leftrotate():
	path=openfn()
	image=Image.open(path)
	rightimage=image.rotate(90)
	x=random.randint(12345,21322)
	#rightimage=image.transpose(Image.FLIP_RIGHT_LEFT)
	rightimage.save('{}.png'.format(x))
	print(' Left rotated and saved!')

def effects1():
	path=openfn()
	image=Image.open(path)
	r,g,b=image.split()
	editimage=Image.merge("RGB",(b,g,r))
	editimage.save('{}.png'.format(random.randint(12345,21322)))
	print(' Effects added and saved!')

def effects2():
	path=openfn()
	image=Image.open(path)
	r,g,b=image.split()
	editimage=Image.merge("RGB",(g,b,r))
	editimage.save('{}.png'.format(random.randint(12345,21322)))
	print(' Effects added and saved!')


	
	

root = Tk()
root.title("Image Editor")
root.resizable(0,0)
root.geometry("400x400")
btn = Button(root,text='resize image',width=30,command=resizeImage).pack()
btn1 = Button(root,text='right rotate image',width=30,command=rightrotate).pack()
btn2 = Button(root,text='left rotate image',width=30,command=leftrotate).pack()
btn3 = Button(root,text='add effects_1 to image',width=30,command=effects1).pack()
btn4 = Button(root,text='add effects_2 to image',width=30,command=effects2).pack()
#label1=Label(root,image=rightimage)

#label1.pack()

root.mainloop()


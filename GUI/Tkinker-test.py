from tkinter import *
import time

root=Tk()
root.title=('test')
root.geometry('300x300')
lable=Label(root)
for i in range(100):
	lable['text']=i
	lable.pack()
	root.update()
	time.sleep(0.5)

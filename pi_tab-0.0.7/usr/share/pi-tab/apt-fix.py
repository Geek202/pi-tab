import os
from tkinter import *
from tkinter import ttk
def install():
	global root
	os.system("sudo apt-get --allow-unauthenticated --force-yes install mplayer")
	root.destroy()
if os.system("mplayer") == 32512:
	root = Tk()
	label1 = Label(root,text="Sorry, you can't\nuse radio because mplayer\nis not installed.\nDo you want to install?",font=("American Typewriter",16))
	label1.pack(side='top')
	root.title("Software Install")
	yesButton = Button(root,text="Yes",command=install)
	yesButton.pack(side='bottom')
	noButton = Button(root,text="No",command=exit)
	noButton.pack(side='left')
	root.mainloop()
else:
	os._exit(0)

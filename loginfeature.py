'''
Going to handle all user og in functionality here
'''

from tkinter import *

# creating window with tkinter
root = Tk()

# adjusting size and window title, along with background image 
root.geometry('1000x600+100+100')
root.title('Login Page')
LoginBackground = PhotoImage(file='background1x.png')
LoginBackgroundLabel =  Label(root, image=LoginBackground)
LoginBackgroundLabel.place(x=0, y=0)

root.mainloop()

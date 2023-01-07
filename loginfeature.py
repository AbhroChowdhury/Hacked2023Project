'''
Going to handle all user og in functionality here
'''

from tkinter import *

# creating window with tkinter
root = Tk()

# adjusting size and window title, adding in background image 
root.geometry('1000x600+100+100')
root.title('Login Page')
LoginBackground = PhotoImage(file='background6x.png')
LoginBackgroundLabel =  Label(root, image=LoginBackground)
LoginBackgroundLabel.place(x=0, y=0)

# Styling Text Box that will include all the login features
LoginFrame = Frame(root, width = 600, height = 300, bg='white')
LoginFrame.place(x=200, y=140)



root.mainloop()

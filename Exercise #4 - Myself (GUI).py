#Julia Coleene Panggoy - 1stYear/BSCS
from tkinter import Tk, Label, PhotoImage, LEFT, RIGHT, RIDGE
root = Tk()

text = Label(root,
             font=('Times', 16, 'bold italic'),
             foreground='white',
             background='black',
             pady=10,
             text='Julia Coleene Panggoy \n Davao City, October 2002 ')
text.pack(side=RIGHT)

me = PhotoImage(file='jia.p.gif')
meLabel = Label(root,
                borderwidth=5,
                relief=RIDGE,
                image=me,)
meLabel.pack(side=LEFT)

root.mainloop()
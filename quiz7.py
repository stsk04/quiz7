from tkinter import *
answer1 = Toplevel
answer2 = Toplevel


root = Tk()
root.title("Quiz")


canvas1 = Canvas(root, width = 400, height =300, relief = 'raised')

canvas1.pack()

title = Label(root, text='Spooky Quiz')
title.config(font=('helvetica', 30))
question= Label(root, text="question1")
question.config(font=('helvetica',20))

canvas1.create_window(200,25,window=title)
canvas1.create_window(200,100,window=question)


button1= Button(root, text="ans1", command = root.destroy)
button1.config(font=('helvetica',15))
button2= Button(root, text="ans2", command = answer2)
button2.config(font=('helvetica',15))
canvas1.create_window(160,140,window=button1)
canvas1.create_window(240, 140, window=button2 )

root.mainloop()

from tkinter import *

root = Tk()

c = Canvas(root, width=500, height=500, bg='white')
c.pack()
c.create_oval(225, 235, 275, 285, width=2)
c.create_oval(200, 210, 300, 310, width=2)
c.create_oval(225, 80, 275, 210, width=2)
c.create_oval(225, 310, 275, 450, width=2)
c.create_oval(60, 240, 200, 285, width=2)
c.create_oval(300, 240, 440, 285, width=2)
root.mainloop()

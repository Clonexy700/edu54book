from tkinter import *

root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

vagon1 = c.create_rectangle(0, 50, 60, 90, fill='blue')
line = c.create_line(60, 70, 70, 70, fill='brown', width=6)
vagon2 = c.create_rectangle(70, 50, 130, 90, fill='blue')
relsa = c.create_line(0, 90, 300, 90, fill='gray', width=3)


def motion():
    c.move(vagon1, 1, 0)
    c.move(vagon2, 1, 0)
    c.move(line, 1, 0)
    if c.coords(vagon1)[0] < 300:
        root.after(20, motion)


motion()

root.mainloop()

from tkinter import *
root = Tk()
c = Canvas(root, width=400, height=400, bg='white')
c.pack()
c.create_oval(20, 20, 200, 200, fill='lightgoldenrod', outline='white')
c.create_arc(20, 20, 200, 200, start=180, extent=25, fill='bisque')
c.create_arc(20, 20, 200, 200, start=160, extent=-320, style=ARC, outline='salmon', width=5)
c.create_arc(10, 10, 210, 210, start=20, extent=-230, style=ARC, outline='turquoise1', width=5)
root.mainloop()

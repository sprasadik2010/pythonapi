from tkinter import *
from turtle import color

ws = Tk()
ws.title('PythonGuides')
ws.geometry('350x450+700+200')
ws.resizable(0,0)


Text(
    ws,
    #text="Life means lot more \n than you know\nLife means lot more \n than you know",
    fg='#00f',
    font=('Times', 20),
    height = 5,
    width = 20
).pack()

Button(
    ws,
    text="Life means lot more \n than you know\nLife means lot more \n than you know",
    fg='#00f',
    font=('Times', 20)
).pack()

Label(
    ws,
    text="Life means lot more \n than you know\nLife means lot more \n than you know",
    fg='#00f',
    font=('Times', 20)
    ).pack(fill=BOTH, expand=True)

ws.mainloop()
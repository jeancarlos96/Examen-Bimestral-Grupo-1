from tkinter import*
ventana= Tk()
canvas =Canvas (ventana, width=800, height=800)
canvas.pack()

canvas.create_polygon(0,0,50,0,0,50,fill="white")
canvas.create_polygon(0,50,0,50,50,100,100,50,fill="black")
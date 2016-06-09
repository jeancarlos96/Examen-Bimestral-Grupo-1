from tkinter import*
ventana= Tk()
canvas =Canvas (ventana, width=800, height=800)
canvas.pack()

canvas.create_polygon(0,0,50,0,0,50,fill="white")
canvas.create_polygon(50,0,150,0,100,50,fill="white")
canvas.create_polygon(150,0,250,0,200,50,fill="white")
canvas.create_polygon(250,0,350,0,300,50,fill="white")

canvas.create_polygon(0,50,50,100,100,50,50,0,fill="black")
canvas.create_polygon(150,0,100,50,150,100,200,50,fill="black")
canvas.create_polygon(250,0,200,50,250,100,300,50,fill="black")
canvas.create_polygon(350,0,300,50,350,100,400,50,fill="black")
canvas.create_polygon(450,0,400,50,450,100,500,50,fill="black")

canvas.create_polygon(0,150,50,200,100,150,50,100,fill="black")
canvas.create_polygon(150,100,100,150,150,200,200,150,fill="black")
canvas.create_polygon(250,100,200,150,250,200,300,150,fill="black")
canvas.create_polygon(350,100,300,150,350,200,400,150,fill="black")
canvas.create_polygon(450,100,400,150,450,200,500,150,fill="black")

canvas.create_polygon(50,200,0,250,50,300,100,250,fill="black")
canvas.create_polygon(150,200,100,250,150,300,200,250,fill="black")
canvas.create_polygon(250,200,200,250,250,300,300,250,fill="black")
canvas.create_polygon(350,200,300,250,350,300,400,250,fill="black")
canvas.create_polygon(450,200,400,250,450,300,500,250,fill="black")
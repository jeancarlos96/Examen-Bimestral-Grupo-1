from tkinter import*
ventana= Tk()
canvas =Canvas (ventana, width=800, height=800)
canvas.pack()
#segunda parte

canvas.create_polygon(50,300,0,350,50,400,100,350,fill="black")
canvas.create_polygon(150,300,100,350,150,400,200,350,fill="black")
canvas.create_polygon(250,300,200,350,250,400,300,350,fill="black")
canvas.create_polygon(350,300,300,350,350,400,400,350,fill="black")
canvas.create_polygon(450,300,400,350,450,400,500,350,fill="black")

canvas.create_polygon(0,350,50,400,0,450,fill="white")
canvas.create_polygon(100,350,50,400,100,450,150,400,fill="white")
canvas.create_polygon(200,350,150,400,200,450,250,400,fill="white")
canvas.create_polygon(300,350,250,400,300,450,350,400,fill="white")
canvas.create_polygon(400,350,350,400,400,450,450,400,fill="white")
canvas.create_polygon(500,350,450,400,500,450,fill="white")

canvas.create_polygon(50,400,0,450,50,500,100,450,fill="black")
canvas.create_polygon(150,400,100,450,150,500,200,450,fill="black")
canvas.create_polygon(250,400,200,450,250,500,300,450,fill="black")
canvas.create_polygon(350,400,300,450,350,500,400,450,fill="black")
canvas.create_polygon(450,400,400,450,450,500,500,450,fill="black")

canvas.create_polygon(0,450,0,550,50,500,fill="white")
canvas.create_polygon(100,450,50,500,100,550,150,500,fill="white")
canvas.create_polygon(200,450,150,500,200,550,250,500,fill="white")
canvas.create_polygon(300,450,250,500,300,550,350,500,fill="white")
canvas.create_polygon(400,450,350,500,400,550,450,500,fill="white")
canvas.create_polygon(500,450,450,500,550,500,fill="white")

canvas.create_polygon(50,500,0,550,50,600,100,550,fill="black")
canvas.create_polygon(150,500,100,550,150,600,200,550,fill="black")
canvas.create_polygon(250,500,200,550,250,600,300,550,fill="black")
canvas.create_polygon(350,500,300,550,350,600,400,550,fill="black")
canvas.create_polygon(450,500,400,550,450,600,500,550,fill="black")

from tkinter import *
from tkinter import messagebox
import math

root = Tk()
root.title('AREA Y VOLUMEN')

radio_label = Label(root,text="INGRESE EL RADIO DE LA ESFERA:")
radio_label.grid(row=1,column=1)
radio_str = StringVar()
radio_entry = Entry(root,textvariable=radio_str)
radio_entry.grid(row=1,column=2)

#FUNCION Area y Volumen 	
def volumen():
   n1=float(radio_entry.get())
   vol =(4*math.pi*(n1*n1*n1))/3
   messagebox.showinfo("test","El volumen es: %.2f"%vol)
   area_entry.delete(0,20)
   
def area():
   n1=float(radio_entry.get())
   ar=4*math.pi*(n1*n1)
   messagebox.showinfo("test","el area es: %.2f"%ar)
   area_entry.delete(0,20)
   

area = Button(root, text = "AREA", command = area, width=15)
area.grid(row=4,column=2)
volumen = Button(root, text = "VOLUMEN", command = volumen, width=15)
volumen.grid(row=6, column=2)
root.mainloop()

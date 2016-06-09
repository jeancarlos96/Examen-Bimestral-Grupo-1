from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('AREA Y VOLUMEN')

radio_label = Label(root,text="INGRESE EL RADIO DE LA ESFERA:")
radio_label.grid(row=1,column=1)
radio_str = StringVar()
radio_entry = Entry(root,textvariable=radio_str)
radio_entry.grid(row=1,column=2)

#FUNCION SUMA Y RESTA 
def area():
   n1=float(area_entry.get())
   area = n1+n2
   messagebox.showinfo("test","LA SUMA ES IGUAL A: ")
   area_entry.delete(0,20)
   
def volumen():
   n1=float(area_entry.get())
   resta=n1-n2
   messagebox.showinfo("test","LA RESTA ES IGUAL A: %.2f"%resta)
   area_entry.delete(0,20)
   

area = Button(root, text = "AREA", command = area, width=15)
area.grid(row=4,column=2)
volumen = Button(root, text = "VOLUMEN", command = volumen, width=15)
volumen.grid(row=6, column=2)
root.mainloop()

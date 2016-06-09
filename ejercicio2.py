#Ejercicio 2

import math 

def multiplos():  
	x= int(input("Ingrese el numero del cual desea conocer los multiplos: ")) 
	cont= x 
	for i in range(x,1000): 
		if (i%x==0): 
			cont=x+i 
			print(cont) 
		else: i=x

	archi=open('ejercicio2.txt','w') 
	archi.close() 

	archi=open('ejercicio2.txt','a') 
	archi.write("Los multiplos de " +str(x) +" son: " +str(cont)) 
	archi.close()

multiplos()


#Ejercicio 3

def contartxt():
	archi=open('examen.txt','r')
	texto=archi.readline()
	while texto!="":
		cont=texto.split(".")
		for i in range(len(cont)):
			palabras=len(cont[i].split(" "))
			print ("El texto tiene: " +str(palabras) +" palabras")
			print ("El texto tiene: " +str(i) +" saltos de linea")
			texto=archi.readline()
		archi.close()

		archi=open('ejercicio1.txt','w')
		archi.close()

		archi=open('ejercicio1.txt','a')
		archi.write("El texto tiene: " +str(palabras) +" palabras\n")
		archi.write("El texto tiene: " +str(i) +" saltos de linea\n")
		archi.close()

contartxt()
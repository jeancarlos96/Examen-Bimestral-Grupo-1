num= input("inserta un numero: ")
numero = int(num)
c=2
contador = 0
verificar= False
for i in range(1,numero+1):
	if (numero% i)==0:
		contador = contador + 1
	if contador >= 3:
		verificar=True
		break


if contador==2 or verificar==False:
	print ("El número es primo")
	print ("La secuencia es:" )

else: 
	print ("El numero no es primo")
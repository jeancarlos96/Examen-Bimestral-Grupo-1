num= input("Ingrese un número: ")
numero = int(num)
contador = 0
verificar= False
for i in range(1,numero+1):

	while (numero% i)==0:
		contador = contador + 1
		print (contador)
	if contador >= 3:
		verificar=True
		break

if contador==2 or verificar==False:
	print ("El número es primo")
		print ()
else: 
	print ("El numero no es primo")

def creartxt():
	archi=open('primos.txt', 'w')
	archi.close()

def grabartxt():
	archi=open('primos.txt','a')
	archi.write(numero)
	archi.close()

creartxt()
grabartxt()
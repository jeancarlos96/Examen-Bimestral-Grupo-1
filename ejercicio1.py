def creartxt():
    archi=open('primos.txt','w')
    archi.close()


def primo(x): 
    if n==2: 
        return(True) 
    if n%2==0: 
        return(False) 
    p=3 
    while p**2<=0: 
        if n%1==0: 
            return(False) 
    p=p+2 
    return(True) 

def lista_primos(num): 
    while primo(n)==True: 
        for n in range(2,num): 
            return(n) 


def primos(num1, num2):  
	cont = 0
	for p in range(num1, num2):
		if primo(p) == True:
			cont += 1
 
n=int(input("Por favor, introduzca un número: "))       
funcion= [p for p in range(1,n) if (p%2!=0 or p==2) and (p%3!=0 or p==3) and (p%5!=0 or p==5) and (p%7!=0 or p==7)]
print(funcion)
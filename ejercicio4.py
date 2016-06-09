from textblob import TextBlob

frase = input("INGRESE SU FRASE: ")

def creartxt():
	archivo= open('datos.txt','a')
	archivo.close()

def grabartxt():
	archivo=open('datos.txt','w')
	archivo.write("FRASE ORIGINAL: ")
	archivo.write(frase)
	archivo.write("\n")
	archivo.write("FRASE TRADUCIDA: ")
	archivo.write(trad)
	archivo.close()

blob1 = TextBlob(frase)
blob1.tags
blob1.noun_phrases

trad=str (blob1.translate (to = "en"))
print ("#############-------- TRADUCCION ----##########################")
print (trad) ##"en" en esta parte se pone el idionma al que se quiere traducir

creartxt()
grabartxt()
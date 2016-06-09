from textblob import TextBlob

frase = input("INGRESE SU FRASE: ")

def creartxt():
	texto_trad = open ('datos.txt','a')
	texto_trad.close()

def grabartxt():
	texto_trad = open('datos.txt','w')
	txt = texto_trad.read()
	texto_trad.write(txt, 'w')	
	archi.close()

blob1 = TextBlob(frase)
blob1.tags
blob1.noun_phrases

print ("#############-------- TRADUCCION ----##########################")
print (blob1.translate (to = "en")) ##"en" en esta parte se pone el idionma al que se quiere traducir
#for sentence in blob1.sentences:
#	print(sentence.sentiment.polarity)


creartxt()
grabartxt()
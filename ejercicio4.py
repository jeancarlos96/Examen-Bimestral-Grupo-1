from textblob import TextBlob

text = 'Hola'

blob1 = TextBlob(text)
blob1.tags
blob1.noun_phrases

print ("#############-------- TRADUCCION ----##########################")
print (blob1.translate (to = "en")) ##"en" en esta parte se pone el idionma al que se quiere traducir
#for sentence in blob1.sentences:
#	print(sentence.sentiment.polarity)
 	
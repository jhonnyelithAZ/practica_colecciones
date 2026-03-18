frase="no te rindas nunca  no te traiciones a ti mismo"
palabras_totales={}
for palabra in frase.split():
    if palabra in palabras_totales:
        palabras_totales[palabra]+= 1
    else:
        palabras_totales[palabra] =1
print(palabras_totales)
notas=[5.0, 4.5, 1.0, 1.5, 1.9, 4.5, 1.4, 1.0]
suma=0
for i in notas:
    suma=suma+i
promedio=suma/len(notas)
print(f"el promedio del estudiante es {promedio}")
if promedio >= 3.0:
    print("aprovado")
else:
    print("pailas")
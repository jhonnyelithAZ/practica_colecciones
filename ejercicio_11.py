estudiantes=[{"jhony":5.0}, {"cas":4.5}, {"ehom":3.0}, {"dapsy":4.0}]
mejor_estudiante= None
mejor_nota=-1
for estudiante in estudiantes:
    for nombre,nota in estudiante.items():
        if nota>mejor_nota:
            mejor_nota=nota
            mejor_estudiante=nombre
print(f"el mejor estudiante es {mejor_estudiante},con {mejor_nota} de nota")
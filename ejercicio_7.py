notas={
    "jhonatan":5.0,
    "hesoyam":4.5,
    "louis":3.2,
    "wily":2.0,
    "lou":4.0
}
total=0
cantidad_alumnos=0
for estudiante in notas:
    total=total+notas[estudiante]
    cantidad_alumnos=cantidad_alumnos+1
promedio = total/cantidad_alumnos
print(f"el promedio de las notas es : {promedio}")
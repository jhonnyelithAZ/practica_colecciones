fuerza={
    "jeas":88,
    "cas":44,
    "ehom":77,
    "smas":33
}

invertido={}

for clave,valor in fuerza.items():
    invertido[valor]=clave

print(invertido)
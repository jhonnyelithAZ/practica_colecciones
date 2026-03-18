identificacion={
            "jhon":29,
            "ivi":21,
            "joa":32,
}
for nombre, edad in identificacion.items():
    if edad >= 18:
        print(f"-{nombre} ({edad}años)")
palabras=["julius", "marsus", "japiter", "momazos", "zebra", "coco", "cabra"]

alfabeticamente={}

for palabra in palabras:
    alfabeticamente[palabra]=len(palabra)
alfabeticamente_ordenado=dict(sorted(alfabeticamente.items()))
print(alfabeticamente_ordenado)
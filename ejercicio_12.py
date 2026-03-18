productos=[
    {"nombre":"manzanas","precio":5000,"cantidad":8},
    {"nombre":"coco","precio":4000,"cantidad":4},
    {"nombre": "queso","precio":9500,"cantidad":8}
]

valor_total=0
for producto in productos:
    valor_producto=producto["precio"] * producto["cantidad"]
    valor_total+=valor_producto
    print(f"-{producto['nombre']}: {producto['cantidad']} unidades a ${producto['precio']} c/u = ${valor_producto}")
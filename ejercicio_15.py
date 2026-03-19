lista_de_ventas=[
    {"producto": "papa", "monto":4000},
    {"producto": "piña", "monto":9000},
    {"producto":"pera", "monto":6000}
]
total_vendido_por_producto={}

for venta in lista_de_ventas:
    producto=venta["producto"]
    monto= venta["monto"]
    if producto in total_vendido_por_producto:
        total_vendido_por_producto[producto]+= monto
    else:
        total_vendido_por_producto[producto]= monto
print (total_vendido_por_producto)
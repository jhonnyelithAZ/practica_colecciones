productos={
        "jabon":5000,
        "shampo":10000,
        "gel":2000,
        "crema":6000,
}
producto_mas_caro= max(productos, key=productos.get)
print(f"el producto mas caro es : {producto_mas_caro} con un precio de {productos[producto_mas_caro]}")
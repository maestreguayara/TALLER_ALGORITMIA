'''
Cálculo del descuento: El algoritmo debe calcular el precio con descuento basado en una condición.
Requerimiento: debe llevar entrada de datos, condicionales, operadores aritméticos

'''

producto = float(input("Ingresa el valor del producto: "))
descuento = (producto * 5 / 100)

producto_descuento = producto - descuento
if producto < 1:
    print("error")
else:
    print(producto_descuento, "pagas este valor")
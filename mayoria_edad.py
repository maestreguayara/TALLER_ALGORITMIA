'''
Verificar mayoría de edad: Determine por medio de un algoritmo si un usuario es mayor de edad.
Requerimientos: debe tener entrada de datos, 
y llevar por lo mínimo una condicional y un operador relacional.

'''

edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("eres mayor de edad")
else: 
    print("eres menor de edad")
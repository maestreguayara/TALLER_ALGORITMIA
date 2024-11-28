'''
Determinar por medio de un algoritmo si un año es bisiesto:
Requerimientos: debe llevar entrada de datos, condicionales, operadores lógicos, 
también debe investigar y posteriormente implementar el operador modulo (%).
'''

año = int(input("Ingresa un año: "))
if año % 4 and año % 400:
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")
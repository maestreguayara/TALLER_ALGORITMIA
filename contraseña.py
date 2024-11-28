'''
Crear un algoritmo que valide una contraseña: sin requerimiento.
'''

longitud = 10
contraseña = input("ingresa una contraseña de 10 caracteres: ")

if len(contraseña) == longitud: 
    print("contraseña valida")
else:
    print("la contrasela es de 10 caracteres")


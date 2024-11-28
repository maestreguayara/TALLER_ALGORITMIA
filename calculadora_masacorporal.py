'''
Calculadora de índice de masa corporal (IMC):
Requerimientos: Investigar y aplicar el operador de potencia, debe llevar entrada de datos.
'''

peso = int(input("Ingrese su peso en kilos: "))
estatura = float(input("Ingrese su estatura en metros: "))

def calcular_imc(peso, estatura):
    imc = peso / estatura ** 2
    return imc
resultado = calcular_imc(peso, estatura)
print("Tu masa corporal es: ", resultado)
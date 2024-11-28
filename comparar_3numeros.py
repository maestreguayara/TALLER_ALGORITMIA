# Comparar tres números: comparar tres números y determinar cuál de los tres es mayor. Sin requerimientos.

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
num3 = int(input("ingresa el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("el primero es mayor")
elif num2 > num1 and num2 > num3:
    print("el segundo es mayor")
elif num3 > num1 and num3 > num2:
    print("el tercero es mayor")
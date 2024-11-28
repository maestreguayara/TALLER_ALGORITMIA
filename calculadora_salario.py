'''

Calculadora de salario: desarrolle un algoritmo de una calculadora que 
calcule el salario neto después de impuesto, el impuesto es de libre elección.
Requerimientos: debe tener entrada de datos, solo debe llevar un (if), 
un operador relacional, y un operador aritmético. 
Nota es posible que le toque investigar acerca del (f-string).

'''

salario = int(input("ingresa tu salario:"))
impuesto = (salario * 10 / 100)
salario_neto = salario - impuesto
if salario < 100:
    print("tu salario no tiene impuesto")
else:
    print(f"tu salario neto es: {salario_neto}")
    








import sys
n1 = 0
n2 = 0

operaciones = """
1.suma
2.resta
"""

def suma():
    print("Ingresa el primer numero:")
    n1 = float(input())
    print("Ingresa el segundo numero:")
    n2 = float(input())
    print("Total =", n1 + n2)

def resta():
    print("Ingresa el primer numero:")
    n1 = float(input())
    print("Ingresa el segundo numero:")
    n2 = float(input())
    print("Total =", n1 - n2)


print("Selecciona una operacion a realizar")
while True:
    print(operaciones)
    opc = int(input())
    if opc == 1:
        suma()
    elif opc == 2:
        resta()
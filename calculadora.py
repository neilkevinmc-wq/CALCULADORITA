## CALCULADORA - VERSIÓN 2
# Autor(a): NEIL MEZA

print("CALCULADORA")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\n1. Sumar")
print("2. Restar")

opcion = input("\nSeleccione una opción: ")

if opcion == "1":
    print("\nLa suma es:", num1 + num2)

elif opcion == "2":
    print("\nLa resta es:", num1 - num2)

else:
    print("\nOpción no válida.")

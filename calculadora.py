## CALCULADORA - VERSIÓN 4
# Autor(a): NEIL MEZA

print("CALCULADORA")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\n1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("\nSeleccione una opción: ")

if opcion == "1":
    print("\nLa suma es:", num1 + num2)

elif opcion == "2":
    print("\nLa resta es:", num1 - num2)

elif opcion == "3":
    print("\nLa multiplicación es:", num1 * num2)

elif opcion == "4":
    if num2 != 0:
        print("\nLa División es:", num1 / num2)
    else:
        print("No se puede dividir entre cero.")

else:
    print("\nOpción no válida.")

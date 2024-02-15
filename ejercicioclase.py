def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def main():

    print("Operaciones: ")
    print("1. Suma")
    print("2. Resta")

    opcion = int(input("Ingrese el número de la operacion que desea realizar: "))

    if opcion < 1 or opcion > 2:
        print("Opcion invalida.")
        return

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if opcion == 1:
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
if __name__ == "__main__":
    main()

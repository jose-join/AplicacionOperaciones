def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if (b==0):
        raise ZeroDivisionError("No se puede hacer divisiones entre 0")
    return a/b
while True:
    try:
        print("Operaciones Básicas")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        opcion = int(input("Ingrese una opción válida: "))
        while(opcion < 1 or opcion > 5):
            print("Dato Inválido, vuelve a ingresar la opción")
            opcion = int(input("Ingrese una opción válida: "))
        if (opcion == 1):
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = suma(a, b)
            print("Resultado: ", resultado)
        if (opcion == 2):
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = resta(a, b)
            print("Resultado: ", resultado)
        if (opcion == 3):
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(a, b)
            print("Resultado: ", resultado)
        if (opcion == 4):
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = division(a, b)
            print("Resultado: ", resultado)
        if (opcion == 5):
            print("Gracias por usar la aplicación")
            break
    except ValueError as VE:
        print("\n !!!!!Ingrese Dato Válido \n")
    except Exception as e:
        print("Error",e)

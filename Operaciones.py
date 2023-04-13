def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if (b==0):
        # Se llama a la excepción ZeroDivision Erro que omite las divisiones entre 0
        raise ZeroDivisionError("No se puede hacer divisiones entre 0")
    return a/b
while True:
    try:
        print("------------------------------") # Separador
        print("Operaciones Básicas")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir\n")
        opcion = int(input("Ingrese una opción válida: "))
        while(opcion < 1 or opcion > 5):        #   Validamos el dato que se va ingresar
                                                #   Solo acepta numero del 1 al 4   
            print("Dato Inválido, vuelve a ingresar la opción")
            opcion = int(input("Ingrese una opción válida: "))
        if (opcion == 1):       #La opcion 1 Suma
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = suma(a, b)
            print("Resultado: ", resultado)
        elif (opcion == 2):       #La opcion 2 Resta
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = resta(a, b)
            print("Resultado: ", resultado)
        elif (opcion == 3):       #La opcion 3 Multiplicacion
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(a, b)
            print("Resultado: ", resultado)
        elif (opcion == 4):       #La opcion 4 Division
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = division(a, b)
            print("Resultado: ", resultado)
        elif (opcion == 5):
            print("Muchas Gracias por usar la aplicación")
            break
    except ValueError as VE: # Si el valor no es un int o float usa esta excepcion
        print("\n Error, Ingrese Dato Válido \n")
    except Exception as e: # La Excepción general
        print("Error",e)

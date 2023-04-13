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
        print("------------------------------")
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
        if (opcion == 2):       #La opcion 2 Resta
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = resta(a, b)
            print("Resultado: ", resultado)
        if (opcion == 3):       #La opcion 3 Multiplicacion
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(a, b)
            print("Resultado: ", resultado)
        if (opcion == 4):       #La opcion 4 Division
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = division(a, b)
            print("Resultado: ", resultado)
<<<<<<< HEAD
        elif (opcion == 5):
            print("Muchas Gracias por usar la aplicación")
            break
    except ValueError as VE:
        print("\n Error, Ingrese Dato Válido \n")
    except Exception as e:
=======
        if (opcion == 5):       #La opcion 5 SALIR
            print("Gracias por usar la aplicación")
            break
    except ValueError as VE:        #   Cual valor erroneo captura el error y lo ignora
        print("\n !!!!!Ingrese Dato Válido \n")
    except Exception as e:          #   Cual valor erroneo captura el error y lo ignora
>>>>>>> Exception
        print("Error",e)

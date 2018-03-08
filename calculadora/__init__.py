#1desplegar las instrucciones
#2obtener los numeros de operacion
#3obtener los numeros del usuario
#4realizar las operaciones en base a la peticion del usuario

#5desplegar el resultado
#6preguntar si quieres realizar otro oepracion


def realizar_operacion(operacion,numero1,numero2):
    
    if(operacion == 1):
        return (numero1 + numero2)
    elif(operacion == 2):
        return (numero1- numero2)
    elif (operacion == 3):
        return (numero1*numero2)
    else:
        return (numero1/numero2)

print("Bienvenido  a la calculadora en python".upper())
while True:
    print("Puedes realizar las siguientes operaciones escoje una: ".upper())
    print("1- suma".upper())
    print("2- resta".upper())
    print("3- multiplicacion".upper())
    print("4- Division".upper())
    
    
    try:
        operacion = int(input("Introduze el numero de la operacion que deseas realizar".upper()))
        
        numero1 = int(input("Introduze el primer numero : "))
        numero2 = int(input("Introduze el segundo numero:  "))
    except ValueError:
        #python y sus diferentes tipos de excepciones ("ZeroDivisionError")
        print("Por favor, introduze solo numeros")
    else:
        if (operacion <1 or operacion >4):
            print("Ese no es un numero de operacion valido")
            continue
        print()
        print()
        resultado = realizar_operacion(operacion, numero1, numero2)
        print("Tu resultado es " , resultado)
        continuar = input("Deseas Continuar? si/no")
        print()
        print()
        if continuar != "si":
            break
print("Gracias por utilizar nuestra calculadora")


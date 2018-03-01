from builtins import str

# las excepciones en python
try:
    a = int(input("Dame un numero"))
    b = int(input("Dame otro numero"))
except ValueError:
    print("Ese no es un numero!!!!")
else:
    suma = a + b
    resta = a -b 
    multiplicacion = a * b
    division = a + b
    print("La suma es " + str(suma))
    print("La suma es " + str(resta))
    print("La suma es " + str(multiplicacion))
    print("La suma es " + str(division))
           
#vamos crear un reloj del mundo

import datetime

print("Bienvenido al reloj del mundo")
print("Estas son las operaciones que puedes realizar")
print("1- Para ver la hora")
print("2- Para ver la fecha y hora")
print("3- Para ver la hora en Nueva York")
print("4- Para ver  la hora en San Francisco")
print("5- Ver las instrucciones Nuevamente")
print("6- Para salir")

while True:
    operacion = input(": ")
    if (operacion == "1"):
        print(datetime.datetime.utcnow().time())
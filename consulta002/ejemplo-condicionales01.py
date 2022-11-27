'''En este programa se pide que ingrese la edad y depende de eso el programa ejecutara
si la edad ingresada corresponde a mayor de edad y correcta, o si no de lo contrario.'''

edad = int(input("Ingrese su edad: "))

if edad>0 and edad<100:
    print("La edad ingresada es correcta")
    if edad>18:
        print("Es mayor de edad")
    elif edad<=18:
        print("Es menor de edad")
else:
    print("La edad ingresada es incorrecta")

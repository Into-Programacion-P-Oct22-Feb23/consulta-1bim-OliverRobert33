'''
Este proceso lo que ejecuta es una multiplicaion y decir si el resultado de dicha multiplicacion es numero par o impar
Mostrar en pantalla el resultado
Mostrar en pantalla si es Par o Impar
'''
producto = 0
numero1 = int(input("Ingrese el multiplicando: "))
numero2 = int(input("Ingrese el multiplicador: "))

producto = numero1 * numero2
residuo = producto % 2

print(f"El resultado de la multiplicacion es: \n{producto}")

if residuo == 0:
    print("El resultado es numero par")
else:
    print("El resultado es numero impar")
'''
El siguiente programa sirve para ingresar el nombre del alumno y 3 notas y sacar el promedio correspondiente, y decir si el promedio es:
malo, bueno, muy bueno o sobresaliente.
'''

nombre = input("Ingrese el nombre del alumno: ")
nota1 = float(input("Ingrese nota 1: ")) 
nota2 = float(input("Ingrese nota 2: ")) 
nota3 = float(input("Ingrese nota 3: ")) 

suma = nota1 + nota2 + nota3
promedio = suma / 3

print(f"El alumno/a: {nombre}\nCon notas: {nota1} - {nota2} - {nota3}\nCon promedio final de: {promedio:.2f}")

if promedio>=9 and promedio<=10:
    print("Su promedio es sobre saliente")
elif promedio>=8 and promedio<9:
    print("Su promedio es muy bueno")
elif promedio>=7 and promedio<8:
    print("Su promedio es bueno")
else:
    print("Su promedio es malo")


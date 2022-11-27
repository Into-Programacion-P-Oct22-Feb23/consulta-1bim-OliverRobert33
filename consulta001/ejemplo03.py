intitucion = input("Ingrese el nombre de la INSTITUCION: ")
curso = input("Ingrese el CURSO del estudiante: ")
estudiante = input("Ingrese el nombre del ESTUDIANTE: ")
nota1 = float(input("Ingrese la NOTA de la asignatura de Matematicas: "))
nota2 = float(input("Ingrese la NOTA de la asignatura de Lengua y Literatura: "))
nota3 = float(input("Ingrese la NOTA de la asignatura de Ingles: "))

promedio = nota1 + nota2 + nota3 / 30

print(f"Nombre de estuadiante es: \n{estudiante}\nInstitucion o Unidad Educativa:\n {intitucion}\
    \nNota de la Asignatura de Matematicas es:\n {nota1}\nNota de la Asignatura de Lengua y Literatura es:\n {nota1}\
    \nNota de la Asignatura de Ingles es:\n {nota1}\nSu promedio es:\n {promedio:.2f}")

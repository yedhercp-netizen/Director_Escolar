from Helpers import verificacion_seguimiento
def eliminar_calificacion():
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "r") as AC:
        lineas = AC.readlines()
        alumno = input("""\nIngrese el nombre con el que ingreso al alumno, 
se recomienda revisar el nombre ante de eliminar la calificacion para confirmar
que el nombre es correcto.
: """).upper()
        if verificacion_seguimiento(alumno):
            return
        materia = input("""Favor de ingresar la materia la cual quiere eliminar
- Matematicas
- Español
- Programacio
: """).upper()
        if verificacion_seguimiento(materia):
            return
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "w") as AC:            
        for i in lineas:
            if not (alumno in i and materia in i):
                AC.write(i)
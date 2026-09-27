from Helpers import Verificacion_Informacion as Verificacion_Nombre
from Helpers import verificacion_seguimiento
def alta_calificacion_completa():
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "a+") as AC:
        AC.seek(0)
        print("\nSi quieres canselar solo pon Back en cualquiera de los inputs")      
        input_nombre = input("Ingrese el codigo del Alumno que quiera dar de alta sus calificaciones: ").upper()
        if verificacion_seguimiento(input_nombre):
            return
        if not Verificacion_Nombre(input_nombre):
            nombre = ("Nombre: " + input_nombre)
            print("\nFavor de siempre referirce al alumno como se a llamado en el nombre, gracias ;)")
            input_materia = input("""Ingrese alguna de las siguentes materias
-Matematicas
-Español
-Programacion
: """).upper()
            if verificacion_seguimiento(input_materia):
                return
            if input_materia in ("MATEMATICAS", "ESPAÑOL", "PROGRAMACION"):
                materia = (" / " + "Materia: " + input_materia)
                calificacion = input("\nIngrese la calificacion que saco el alumno: ")
                if verificacion_seguimiento(calificacion):
                    return
                if calificacion.isdigit():
                    if int(calificacion) > 0 and int(calificacion) <= 100:
                        calificacion = (" / " + "Calificacion: " + calificacion)
                        AC.write(nombre + materia + calificacion + "\n")
                    else:
                        print("La calificacion no puede ser mayor que 100 o menor que 0")
                else:
                    print("No se puede ingresar letras")
            else:
                print("Esa materia no esta en el sistema")
        else:
            print("Alumno no encontrado")
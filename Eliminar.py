from Helpers import Verificacion_Informacion
from Helpers import verificacion_seguimiento
def Eliminar_Calificaciones_Automaticamente(Nombre):
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "r") as AC:
            lineas = AC.readlines()
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "w") as AC:            
            for i in lineas:
                if Nombre not in i:
                    AC.write(i)

def eliminar():
    with open("Alumnos_CBTis_49.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("\nIngrese 'Back' para regresar al menú")
        alumno = input("""Ingrese el número telefónico del alumno, 
se recomienda revisar el numero antes de eliminar para confirmar
que el numero es correcto.
: """).upper()
        verdad = Verificacion_Informacion(alumno)
        if verificacion_seguimiento(alumno):
            return
        if verdad == True:
            accion = input("¿Quieres eliminar también las calificaciones? [Y/N]: ").upper()
            if verificacion_seguimiento(accion):
                return
            if accion == "Y":
                nombre = ("Nombre: " + input("Ingrese el nombre del alumno que quiera dar de alta sus calificaciones: ").upper())
                Eliminar_Calificaciones_Automaticamente(nombre)
            with open("Alumnos_CBTis_49.txt", "w") as archivo:            
                for i in lineas:
                    if alumno not in i:
                        archivo.write(i)
        else:
            print("Alumno no existente")
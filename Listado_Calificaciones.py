from Helpers import Verificacion_Calificaciones
from Helpers import verificacion_seguimiento
def listado_calificaciones():
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "r") as AC:
        Leer = AC.readlines()
        Nombre = input("\nIngrese el codigo de la persona que quiera saber sus calificaciones: ").upper()
        if verificacion_seguimiento(Nombre):
            return
        Verdad = Verificacion_Calificaciones(Nombre)
        if Verdad == True:
            for i in Leer:
                if Nombre in i:
                    print(i, end="")
            accion = input("Precione Enter para regresar al menú de calificaciones")
            if accion:
                return
        else:
            print("Ese alumno no tiene calificaciones")
from Helpers import Verificacion_Informacion
from Helpers import verificacion_seguimiento
import time
def alta():
    print("\nPara regresar al menu inicial ingrese Back")
    Nombre = input("Ingrese el nombre: ").upper()
    if verificacion_seguimiento(Nombre):
        return
    
    Verdad = Verificacion_Informacion(Nombre)
    with open("Alumnos_CBTis_49.txt", "a") as A:
        if Verdad == False:
            Grupo = input("Ingrese el grupo: ").upper()
            if verificacion_seguimiento(Grupo):
                return
            Grado = input("Ingrese el grado: ").upper()
            if verificacion_seguimiento(Grado):
                return
            Numero_Telefonico = input("Ingrese el numero telefonico: ").upper()
            if verificacion_seguimiento(Numero_Telefonico):
                return
            lista = Nombre.split()
            Codigo_lista = []
            for i in lista:
                vuelta = 0
                for x in i:
                    if vuelta == 0:
                        Codigo_lista.append(x)
                        vuelta += 1
            Codigo = "".join(Codigo_lista)
            A.write(f"Nombre: {Nombre} / Grupo: {Grupo} / Grado: {Grado} / Numero Telefonico: {Numero_Telefonico} / Codigo: {Codigo} \r")
        else:
            print("Alumno ya incrito, no se puede volver a ingresar")
            time.sleep(1)
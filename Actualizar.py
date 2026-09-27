from Helpers import Verificacion_Informacion
from Helpers import Verificacion_Actualizacion
from Helpers import verificacion_seguimiento
import time

def actualizar():
    with open("Alumnos_CBTis_49.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("\nIngresa 'Back' para poder ingresar al menu inicical")
        Telefono = input("""Ingrese el numero telefonico del alumno, 
se recomienda revisar el numero ante de actualizar para confirmar
que el numero correcto.
: """).upper()
        if verificacion_seguimiento(Telefono):
            return
        Verdad = Verificacion_Informacion(Telefono)
        if Verdad == True:
            with open("Alumnos_CBTis_49.txt", "a") as Archivo:
                print("Ingrese 'Back' en una si quiere regresar y luego de enter multiples veces hasta que acabe")
                Nombre = input("Ingrece el nombre completo del alumno: ")
                if verificacion_seguimiento(Nombre):
                    return
                Grupo = input("Ingrece el grupo del alumno")
                if verificacion_seguimiento(Grupo):
                    return
                Grado = input("Ingrece el grado del alumno: ")
                if verificacion_seguimiento(Grado):
                    return
                Numero_Telefonico = input("Ingrese el numero telefonico del alumno")
                if verificacion_seguimiento(Numero_Telefonico):
                    return
                lista = Nombre.split()
                Codigo_lista = []
                for i in lista:
                    Codigo_lista.append(i)
                Codigo = "".join(Codigo_lista)
                info_new = (f"Nombre: {Nombre} / Grupo: {Grupo} / Grado: {Grado} / Numero Telefonico: {Numero_Telefonico} / Codigo: {Codigo}")
                verificacion = info_new.strip()
                Verdad = Verificacion_Actualizacion(verificacion)
                if Verdad == False:
                    with open("Alumnos_CBTis_49.txt", "w") as archivo:            
                        for i in lineas:
                            if Telefono not in i:
                                archivo.write(i)

                    with open("Alumnos_CBTis_49.txt", "a") as Archivo:
                        Archivo.write(info_new + "\n")

                else:
                    print("La informacion es la misma")
        else:
            return print("No se a encontrado al alumno pruebe otra vez porfavor")
        time.sleep(1)
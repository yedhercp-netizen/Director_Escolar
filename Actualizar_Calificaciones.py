from Helpers import Verificacion_Actualizacion_Calificaciones
from Helpers import Verificacion_Calificaciones_Nombre_Materia as VCNM
from Helpers import verificacion_seguimiento
import time

def actualizar_calificaciones():
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "r") as archivo:
        lineas = archivo.readlines()
        print("\nPara regresar al menú inicial ingresa 'Back'")
        alumno = input("""\nIngrese el codigo con el que ingreso al alumno, 
se recomienda revisar el nombre ante de actualizar la calificacion para confirmar
que el codigo es correcto.
: """).upper()
        if verificacion_seguimiento(alumno):
            return
        input_materia = input("""Favor de ingresar la materia la cual quiere eliminar
- Matematicas
- Español
- Programacio
: """).upper()
        if verificacion_seguimiento(input_materia):
            return
        Verdad = VCNM(alumno, input_materia)
        if input_materia == ("MATEMATICAS", "ESPAÑOL", "PROGRAMACION"):
            return print("Esa materia no esta disponible")

        if Verdad == True:
            with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "a") as Archivo:
                nombre = ("Nombre: " + alumno)
                materia = (" / " + "Materia: " + input_materia)
                calificacion = input("Ingrese la calificacion que saco el alumno: ")
                if verificacion_seguimiento(calificacion):
                    return
                if calificacion.isdigit() :
                    if int(calificacion) > -1 and int(calificacion) < 101:
                        calificacion = (" / " + "Calificacion: " + calificacion)
                        info_new = (nombre + materia + calificacion + "\r")
                        verificacion = info_new.strip()
                        Verdad = Verificacion_Actualizacion_Calificaciones(verificacion)
                        if Verdad == False:
                            with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "w") as archivo:            
                                for i in lineas:
                                    if not (alumno in i and input_materia in i):
                                        archivo.write(i)
        
                            with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "a") as Archivo:
                                Archivo.write(info_new + "\n")
                        else:
                            print("La informacion es la misma")
                    else:
                        print("No se pueden calificaciones mayores que 100 o menores que 0")
        else:
            return print("No se a encontrado el alumno o la materia en el archivo")
        time.sleep(2)
from Listado_Calificaciones import listado_calificaciones
from Alta_Calificacion import alta_calificacion_completa
from Actualizar_Calificaciones import actualizar_calificaciones
from Eliminar_Calificaciones import eliminar_calificacion
from Helpers import transicion
def submain():
    while True:
        print("""\n1. Listado
2. Alta Calificación
3. Actualizar Calificación
4. Eliminar Calificacion
5. Regresar al Menú Inicial""")
        accion = input("Escoja alguna de las opciones: ")
        if accion == "1":
            listado_calificaciones()
        elif accion == "2":
            alta_calificacion_completa()
        elif accion == "3":
            actualizar_calificaciones()
        elif accion == "4":
            eliminar_calificacion()
        elif accion == "5":
            break
        else:
            print("Esa accion no es posible")
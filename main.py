from Alta import alta
from Actualizar import actualizar
from Eliminar import eliminar
from Listado_Completo import listado_completo
from Submain import submain

with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "a"):
    pass
with open("Alumnos_CBTis_49.txt", "a"):
    pass
while True:
    print("""\n1. Alta
2. Actualización
3. Eliminar
4. Listado Completo
5. Menú de Calificaciones
6. Salir""")
    accion = input("""Por favor ingrese uno de los números anteriormente mencionados
: """)
    if accion.isnumeric():
        if int(accion) == 1:
            alta()
        elif int(accion) == 2:
            actualizar()
        elif int(accion) == 3:
            eliminar()
        elif int(accion) == 4:
            listado_completo()
        elif int(accion) == 5:
            submain()
        elif int(accion) == 6:
            break
        else:
            print("Esa opción no es posible")
    else:
        print("Solo se puede ingresar numeros")
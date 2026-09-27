def listado_completo():
    with open("Alumnos_CBTis_49.txt", "r") as A:
        print("\n")
        print(A.read())
        accion = input("Presione Enter para seguir")
        if accion:
            return
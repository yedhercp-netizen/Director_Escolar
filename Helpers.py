def Verificacion_Informacion(Nombre):
    with open("Alumnos_CBTis_49.txt", "r") as A:
            Archivo = A.readlines()
            for i in Archivo:
                Caracteristicas = i.split(" / ")
                for x in Caracteristicas:
                    no_importante, importante = x.split(": ")
                    if importante == Nombre:
                         return True
            return False

def Verificacion_Calificaciones(Nombre):
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "r") as AC:
                Archivo = AC.readlines()
                for i in Archivo:
                    if Nombre in i:
                        return True
                return False

def Verificacion_Actualizacion(info_new):
    with open("Alumnos_CBTis_49.txt", "r") as A:
            Archivo = A.readlines()
            for i in Archivo:
                if info_new == i.strip():
                    return True
            return False

def Verificacion_Actualizacion_Calificaciones(info_new):
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "r") as AC:
            Archivo = AC.readlines()
            for i in Archivo:
                if info_new == i.strip():
                    return True
            return False

def Verificacion_Calificaciones_Nombre_Materia(Nombre, materia):
    with open("ARCHIVO_CALIFICACIONES_ALUMNOS.txt", "r") as AC:
                Archivo = AC.readlines()
                for i in Archivo:
                    if Nombre in i and materia in i:
                        return True
                return False

def transicion(lugar):
    def comprovar_fila():
        import sys
        import termios
        import tty
        fd = sys.stdin.fileno()
        configuracion = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            print("\033[6n", end="", flush=True)
            repuesta = ""
            while "R" not in repuesta:
                caracter = sys.stdin.read(1)
                repuesta += caracter
        finally:
            termios.tcsetattr(
                fd,
                termios.TCSADRAIN,
                configuracion
            )
        file, culmanas = repuesta[2:-1].split(";")
        return int(file)
    
    import time
    animacion = 0
    while True:
        fila = comprovar_fila()
        if fila <= 1:
            break
        animacion += 1
        if animacion > 3:
            animacion = 1
        print("\033[1A\033[2K", end="")
        if animacion == 1:
            print("Limpiando la Terminal.")
        elif animacion == 2:
            print("Limpiando la Terminal..")
        elif animacion == 3:
            print("Limpiando la Terminal...")
        time.sleep(0.5)
        print("\033[1A\033[2K", end="")
    for i in range(1, 4):
        if lugar == True:
            print("Yendo al menu inicial" + ("." * i), flush=True)
            time.sleep(1)
            print("\033[1A\033[2K", end="")
        elif lugar == False:
            print("Yendo al menu de calificaciones" + ("." * i), flush=True)
            time.sleep(1)
            print("\033[1A\033[2K", end="")
        else:
            print("Saliendo de la pagina" + ("." * i), flush=True)
            time.sleep(1)
            print("\033[1A\033[2K", end="")

def verificacion_seguimiento(variable: str):
    import string
    import time
    def salir(variable):
        if "BACK" in variable:
            return True
        return False
    
    if not variable.strip():
        print("No se puede dejar el espacio basio")
        time.sleep(1)
        print("\033[1A\033[2K",end="")
        for i in range(1,4):
            print("Regresando" + ("." * i))
            time.sleep(0.5)
            print("\033[1A\033[2K",end="")
        return True

    if any(i in string.punctuation for i in variable):
        print("No se puede agregar simbolos")
        time.sleep(1)
        print("\033[1A\033[2K",end="")
        for i in range(1,4):
            print("Regresando" + ("." * i))
            time.sleep(0.5)
            print("\033[1A\033[2K",end="")
        return True

    if salir(variable):
        print("Saliendo al menu inicial")
        time.sleep(1)
        print("\033[1A\033[2K",end="")
        for i in range(1,4):
            print("Regresando" + ("." * i))
            time.sleep(0.5)
            print("\033[1A\033[2K",end="")
        return True
    return False
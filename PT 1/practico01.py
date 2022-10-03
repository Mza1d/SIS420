def perfil():
    print("SELECCIONE UNA DE LAS OPCIONES")
    print("S -> Para continuar \nN -> Para salir")
    respuesta = input("¿Desea continuar o terminar el programa?: ")
    Apellidos = "Anarata Diaz"
    Nombre = "Mario"
    Nacionalidad = "Bolivia"
    Carrera = "Ing. Sistemas"
    Telefono = "61884698"
    if respuesta == 'S' or respuesta == 's':
        print('---------- MI PRESENTACIÓN ----------')
        print('Apellidos: ',Apellidos)
        print('Nombres: ',Nombre)
        print('Carrera: ',Carrera)
        print('Nacionalidad: ',Nacionalidad)
        print('Telefono: ',Telefono)
        print('------------- SIS - 420 ------------')
    if respuesta == 'N' or respuesta == 'n':
        print("Gracias por su visita")
perfil()
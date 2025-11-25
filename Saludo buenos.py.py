#********************* Zona de funciones *********************************************
# palabra_clave + nombre_funcion(verbo) + parametros(adjectivos)
from datetime import datetime
def capturar_nombre():
    nombre_usuario = input("escriba el nombre del cliente: ")
    return nombre_usuario
def capturar_rol():
    rol_usuario = input("escribe su rol: ")
    return rol_usuario
def capturar_hora():
    hora = int(input("escriba la actual (0-23):"))
    return hora
def obtener_saludo_hora(hora):
    if 6 <= hora < 12:
        return "buenos dias"
    elif 12 <= hora < 18:
        return "buenas tardes"
    else:
        return "buenas noches"
def hacer_saludo (nombre_usuario, rol_usuario, hora):
    saludo_tiempo = obtener_saludo_hora(hora)
    mensaje = saludo_tiempo + " " + nombre_usuario + " rol: " + rol_usuario
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)    
#******************* zona de codigo principal ******************************************
dato_nombre = capturar_nombre()
dato_rol = capturar_rol()
hora_usuario = capturar_hora()
dato_mensaje = hacer_saludo(dato_nombre, dato_rol, hora_usuario)
imprimir_mensaje(dato_mensaje)    
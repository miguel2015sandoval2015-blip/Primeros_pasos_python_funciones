#************* zona de funciones **********************
# palabra_clave + nombre_funcion(verbo) + parametros(adjectivos)

def capturar_datos():
    print("\nmenu principal.")
    print("digite la letra ´A´ para Actualizar Sistema")
    print("digite la letra ´E´ para Eliminar Catalago")
    print("digite la letra ´C´ para crear Producto")
    print("digite la letra ´S´ para salir del Programa")

    letra=input("selecione una opcion:")
    return letra.upper()
def analizar_datos(opcion):
    if opcion=="A":
        return "Elijio actualizar el sistema: "
    elif opcion=="E":
        return "Elijio eliminar el catalogo: "
    elif opcion=="C":
        return "Elijio crear producto: "
    elif opcion=="S":
        return "S"
    else:
        return "infomacion no valida, intente de nuevo: "
    
    def mostrar_datos(resultado):
        print("\n>",resultado,"\n")

#*********************zona de codigo principal ***********************

while True:
    opcion=capturar_datos()
    resultado=analizar_datos(opcion)

    if resultado=="S":
        print("\nFinalizo el programa con exito.\n")
        break

    mostrar_datos(resultado)

    print("el do while a finalizado")



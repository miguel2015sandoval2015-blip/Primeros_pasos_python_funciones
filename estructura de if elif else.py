#******************** zona de funciones ***********************************
def capturar_datos():
    numero = int(input("escriba el nuemro"))
    return numero


def analizar_datos(numero):
    if numero > 0:
        mensaje = "el numero es positivo."
    elif numero == 0:
        mensaje = "el numero es neutro."
    else: 
        mensaje = "el numero es negativo."
    return mensaje

def mostrar_resultados(mensaje):
    print("el numero es: " + numero + str(numero))
    

    #**************zona de codigo principal **********************
    numeroe = capturar_datos()
    mensaje = analizar_datos(nuemro)
    mostrar_resultados(mensaje)
    



















#************************** zona de codigo principal de python *********************

print("digite un numero: ")
numero=int(input())

if numero > 0:
    print("El numero es positivo. ")
elif numero ==0:
    print("El numero es neutro. ")
else:
    print("")
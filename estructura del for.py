"""""  crear un programa que solicite la cantidad de numeros 
        que el usuario va a digitar y calcular el acumulado de la
        lista de numeros entrados por consola  """

# palabra_clave + nombre_funcion(verbo) + parametros(adjectivos)
#**********************zona de funciones ********************************
suma=0 # se crea la variable global
#print("Digite la cantidad de numeros para sumar: ")
#cantidad=int(input()) # estar pendiente de los tipos de variables

def capturar_rango():
    r=int(input("digite el rango ( 0 para salir ): "))
    return r



def procesar_rango(r):
    suma= 0
    for i in range(0,r,2):    
      print("digite el numero" + str(i+1)+": ")
    numero=int(input())
    suma=suma+numero
    
    return suma




def imprimir_resultados(suma):
    print("la suamtoria total es: " + str(suma))

#**************** zona de codigo principal ***************************

rango = capturar_rango()

if rango != 0:
    resultado = procesar_rango(rango)
    imprimir_resultado(resultado)
else:
    print("programa finalizado")    
  




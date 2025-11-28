# realizar un programa que la variable sea diferente a cero
# este pidiendo un valor por consola e indicar si el numero 
# digitado es par o inpar
# palabra_clave + nombre_funcion(verbo) + parametros(adjectivos)

# ******************* zona de funciones **************************
def capturar_numero():
    numero= int(input("digite un numero (0 para salir): "))
    return numero
    
          
def procesar_numero(numero):
        if numero%2==0:
              print("el numero es par")
        else:
              print("el numero es impar")

def imprimir_numero():                    
    print("finalizo el programa")

# ************zona de codigo principal ***************************
numero = 1
while numero != 0:
      numero = capturar_numero()

      if numero != 0:
            procesar_numero(numero)
imprimir_numero()

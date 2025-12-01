# realizazr un programa que por medio del numero del mes
# indique el nombre del mes que le corresponde al numero

#***************zona de funciones **********************
def tomar_datos():
 print("digite un numero del 1 al 12")
 num=int(input())

 return num

def procesar_datos(num):
    match num:
     case 1:
         mes = "enero"
     case 2:
       mes = "febrero"
     case 3:
       mes = "marzo"
     case 4:
       mes = "abril"
     case 5:
       mes = "mayo"
     case 6:
       mes = "junio"
     case 7:
       mes = "julio"
     case 8:
       mes = "agosto"
     case 9:     
       mes = "septiembre"
     case 10:
       mes = "octubre"
     case 11:
       mes = "noviembre"
     case 12:
       mes = "diciembre"  

    return mes 

def imprimir_datos(mes):
   print ("el mes seleccionado es:", mes)
   

#************* Zona de codigo principal*****************************
num = tomar_datos()
mes = procesar_datos(num)
imprimir_datos(mes)
   
 
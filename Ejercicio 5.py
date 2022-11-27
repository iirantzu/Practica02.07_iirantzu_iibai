#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrados():
   lista = []
   lista2 = []
   numero = 1
   while (numero!=0):
       numero=int(input('introduce un numero para meterlo en la lista, para parar de meter números introduce el 0: '))
       lista.append(numero)
   for x in range(len(lista)):
       numero2 = lista[x]
       numero3 = numero2 * numero2
       lista2.append(numero3)
   return lista2
print(cuadrados())
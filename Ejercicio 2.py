#Escribir una función que reciba un número entero positivo y devuelva su factorial. Realiza
#el ejercicio mediante bucles interactivos y mediante una función recursiva.

def factorial(n):
   '''Esta función hace el factorial del numero que introduzcas
      -Parámetros:
       n: númer introducido
       -Salidas: n*factorial(n-1)'''
   if n == 0:
       return 1
   else:
     return n * factorial(n-1)
numero = int(input('introduzca un numero'))
print('el factorial del numero introducido es: ', factorial(numero))

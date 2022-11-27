#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def nums_lista(lista):
    '''Esta función hace la media de una lista de numeros
        -Parámetros:
        lista
        -Salidas:
        media'''
    longitud_lista = len(lista)
    sum_lista = sum(lista)
    media = sum_lista / longitud_lista
    return media


lista = []
usr_input = input('ponga una lista de numeros separados por comas. Se mostrará la media')
lista = usr_input.split(", ")
for elem in range(len(lista)):
    lista[elem] = int(lista[elem])
print('la media de los valores que ha dado es :', nums_lista(lista))
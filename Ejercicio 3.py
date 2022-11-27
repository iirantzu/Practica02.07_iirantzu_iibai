#Escribir una función que calcule el área de un círculo y otra que
#calcule el volumen de un cilindro usando la primera función.

def area_circulo(radio):
    '''Esta funcion calcula el area e un circulode radio<radio>
    -Parámetros:
    radio: radio de la circunferencia dado por el usuario
    -salida:
    area: area de la circunferencia'''
    area = 3.1415 * radio * radio
    return area


def vol_cilindro(radio, altura):
    '''Esta funcion calcula el volumen de un cilindro utilizando el area calculada por la funcion anterior
    -Parametros:
    area_circulo: area del circulo calculado previamente
    altura: altura del cilindro dada por el usuario
    -Salida:
    vol: volumen del cilindro'''
    area = area_circulo(radio)
    vol = area * altura
    return vol


rad = int(input('introduzca el radio del circulo: '))
alt = int(input('introduzca la altura del cilindro'))
print('area del circulo: ', area_circulo(rad))
print('volumen del cilindro de base circulo:', vol_cilindro(rad, alt))
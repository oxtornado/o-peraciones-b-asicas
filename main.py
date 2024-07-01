# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2

# Este programa tiene el fin de usar la importacion de modulos 
# para la generacion de numeros aleatorios y se ejecuten las 
# operaciones de suma, resta, division y multiplicacion


# Importamos de liberia random el modulo randint con el fin de generar numeros enteros aleatorios
from random import randint


# Definimos funcion para retornar suma
def suma(a, b):
    return a + b


# Definimos funcion para retornar resta
def resta(a, b):
    return a - b


# Definimos funcion para retornar division
def division(a, b):
    return a + b

# Definimos funcion para retornar multiplicacion
def multiplicacion(a, b):
    return a + b

# Se establece una funcion que ofrezca la opcion de 
# seguir generando numeros aleatorios y sus operaciones
def continuar_numeros():
    
    # Un bucle hasta que la respuesta que buscamos no sea suministrada 
    while True:

        # variable input para saber la decision del usuario
        mensaje = input('Desea continuar generando numeros aleatorios?: ')

        # Condicionamiento para las respuestas que nosotros configuremos como validas
        if mensaje == 'si':
            
            # Invocamos nuevamente a la funcion principal para volver a ejecutarla
            main()

        # Si el usuario decide no continuar se desplega un mensaje de despedida y se cerrara el programa
        elif mensaje == 'no':
            print('Hasta luego')
            exit()

        # Cualquier entrada que no se encuentre dentro de estas opciones, no sera valida y se le msotraran las opciones validas
        else:
            print('Si/No')


# La funcion principal, que llama las funciones respectivas y printea los resultados
def main():

    # Primer varibale para la generacion de numeros aletaorios
    numeros_aleatorios =  randint(1, 100+1)

    # Segundo varibale para la generacion de numeros aletaorios
    numeros_aleatorios_dos  = randint(1, 100+1)

    # Mostramos en pantalla los resuktados de las operaciones como suma, resta, etc.
    print(f'''
Primer numero: {numeros_aleatorios}
Segundo numero: {numeros_aleatorios_dos} 

La suma entre ambos es: {suma(numeros_aleatorios, numeros_aleatorios_dos)}
La resta entre ambos es: {resta(numeros_aleatorios, numeros_aleatorios_dos)}
La division entre ambos es: {division(numeros_aleatorios, numeros_aleatorios_dos)}
La multiplicacion entre ambos es: {multiplicacion(numeros_aleatorios, numeros_aleatorios_dos)}
''')
    
    #Llamamos a la funcion para identificar si deseamos o no continuar gerendo numeros aletaorios y sus respectivas operaciones
    continuar_numeros()


# Nombramos la condicion donde se ejecutara la funcion invocada
if __name__=='__main__':
    main()
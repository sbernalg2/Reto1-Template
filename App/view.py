"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
#from tabulate import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def newController():
    """
        Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("0- Salir")

def loadData(control):
    """
    Carga los datos
    """
    data = controller.loadData(control, "Ruta")
    pass

def printData(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.getData(control, id)
    print("El dato con el ID",id, "es:", data)

def printReq1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print(controller.req1(control))
    pass

def printReq2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print(controller.req2(control))
    pass

def printReq3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req3(control))
    pass

def printReq4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req4(control))
    pass

def printReq5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print(controller.req5(control))
    pass

def printReq6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req6(control))
    pass

def printReq7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req7(control))
    pass

def printReq8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req8(control))
    pass
# Se crea el controlador asociado a la vista
control = newController()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        try: 
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = loadData(control)
            elif int(inputs) == 2:
                printReq1(control)

            elif int(inputs) == 3:
                printReq2(control)

            elif int(inputs) == 4:
                printReq3(control)

            elif int(inputs) == 5:
                printReq4(control)

            elif int(inputs) == 6:
                printReq5(control)

            elif int(inputs) == 7:
                printReq6(control)

            elif int(inputs) == 8:
                printReq7(control)

            elif int(inputs) == 9:
                printReq8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                printData(control, id)

            elif int(inputs) == 0:
                print("\nGracias por utilizar el programa")
                break

            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
    sys.exit(0)

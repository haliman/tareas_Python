import os
from colorama import Fore, Style

from controllers.tareasController import TareasController

class Menu:
    
    def limpiarPantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def pintarMenu(self):
        print(Fore.GREEN+"****************************")
        print("***** Gestor de tareas *****")
        print("****************************"+ Style.RESET_ALL)
        print('1. Mostrar tareas.')
        print('2. Agregar tarea.')
        print('3. Completar tarea.')
        print('4. Eliminar tarea.')
        print('5. Salir.\n')
        
    def seleccionarOpciones(self):
        opcion = '0'
        tarea = TareasController()
        while opcion != '5':
            self.pintarMenu()
            opcion = input('Seleccione la opción: ')
            if opcion == '1':
                tarea.mostarTareas()
            elif opcion == '2':
                descripcion = input('Introduzca la tarea a realizar: ')
                tarea.agregarTarea(descripcion)
            elif opcion == '3':
                #Excepción en el caso de que el valor introducido no sea correcto nos de un mensaje de error.
                try:
                    posicion = int(input(Fore.BLUE+'Introduzca el número de la tarea que quiere completar: '+Style.RESET_ALL))
                    tarea.completarTarea(posicion)
                except ValueError:
                    print(Fore.RED+'La posición no existe.'+Style.RESET_ALL)
            elif opcion == '4':
                #Excepción en el caso de que el valor introducido no sea correcto nos de un mensaje de error.
                try:
                    posicion = int(input(Fore.BLUE+'Introduzca el número de la tarea que quiere eliminar: '+Style.RESET_ALL))
                    tarea.eliminarTarea(posicion)
                except ValueError:
                    print(Fore.RED+'La posición no existe.'+Style.RESET_ALL)
            elif opcion == '5':
                print('Cerrando programa.')
            else:
                print('Introduzca una opción valida')
            print('\nPresione cualquier tecla para continuar...')
            input()
            self.limpiarPantalla()    
            
            
        
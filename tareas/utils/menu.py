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
        print('4. Mostrar tareas.')
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
                posicion = input(Fore.BLUE+'Introduzca el número de la tarea que quiere completar: '+Style.RESET_ALL)
                tarea.completarTarea(posicion)
            elif opcion == '4':
                posicion = input(Fore.BLUE+'Introduzca el número de la tarea que quiere eliminar: '+Style.RESET_ALL)
                tarea.eliminarTarea(posicion)
            elif opcion == '5':
                print('Cerrando programa.')
            else:
                print('Introduzca una opción valida')
            print('\nPresione cualquier tecla para continuar...')
            input()
            self.limpiarPantalla()    
            
            
        
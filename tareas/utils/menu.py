import os
from colorama import Fore, Style

from controllers.tareasController import TareasController

class Menu:
    #Clase Menu donde vamos a realizar todas la tareas.
    
    #Limpia la pantalla de la consola
    def limpiarPantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    #Pinta las opciones del menú en consola
    def pintarMenu(self):
        print(Fore.GREEN+"****************************")
        print("***** Gestor de tareas *****")
        print("****************************"+ Style.RESET_ALL)
        print('1. Mostrar tareas.')
        print('2. Agregar tarea.')
        print('3. Completar tarea.')
        print('4. Eliminar tarea.')
        print('5. Salir.\n')
        
    #Selecciona una de las opciones del menú 
    def seleccionarOpciones(self):
        #Inicializa la opcion a 0 y Crea una instancia de TareasController para manejar las tareas.
        opcion = '0'
        tarea = TareasController()
        
        #Bucle para escoger la opción deseada y en caso de querer salir presionar la opción correspondiente.
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
            
            
        
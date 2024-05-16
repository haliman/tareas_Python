import os

class Menu:
    
    def limpiarPantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def pintarMenu(self):
        print('1. Mostrar tareas.')
        print('2. Agregar tarea.')
        print('3. Completar tarea.')
        print('4. Mostrar tareas.')
        print('5. Salir.')
        
    def seleccionarOpciones(self):
        opcion = '0'
        while opcion != '5':
            self.pintarMenu()
            opcion = input('Seleccione la opción: ')
            if opcion == '1':
                print('Mostrar tareas')
            elif opcion == '2':
                print('Agregar tarea')
            elif opcion == '3':
                print('Completar tarea')
            elif opcion == '4':
                print('Eliminar tarea')
            elif opcion == '5':
                print('Cerrando programa.')
            else:
                print('Introduzca una opción valida')
            input()
            self.limpiarPantalla()    
            
            
        
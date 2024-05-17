from colorama import Fore, Style

from models.tarea import Tarea

class TareasController:
    '''
        Clase TareasController donde están los módulos para realizar todas las gestiones con las tareas como agregar, mostrar.....
        
        Atributos: 
            tareas(list): Lista de tareas donde se almacena las tareas.
    '''
    def __init__(self):
        #Inicializamos las tareas con una lista vacía.
        self.tareas = []
        
    #Mostramos todas las tareas que hay en la lista.
    def mostarTareas(self):
        for i, tarea in enumerate(self.tareas):
            print(str(i+1)+'.',tarea)
            
    '''
        Agregamos una nueva tarea
        
        Parámetros:
            descripción (str): descripción de la nueva tarea.
    '''
    def agregarTarea(self, descripcion):
        self.tareas.append(Tarea(descripcion))
        print('Se ha creado la tarea con exito!!')
    
    '''
        Eliminar una tarea
        
        Parámetros:
            posición(int): Posición de la tarea que queremos eliminar.
    '''     
    def eliminarTarea(self, posicion):
        #Excepción en el caso de que el valor introducido no sea correcto nos de un mensaje de error.
        try:
            del self.tareas[posicion-1]
            print(Fore.RED+'Se ha eliminado la tarea con exito!!'+Style.RESET_ALL)
        except IndexError:
            print(Fore.RED+'La posición no existe.'+Style.RESET_ALL)
    
    '''
        Cambiamos el estado de tarea a completada(TRUE)
        
        Parámetros:
            posición(int): Posición de la tarea que queremos completar en la lista.  
    '''
    def completarTarea(self, posicion):
        #Excepción en el caso de que el valor introducido no sea correcto nos de un mensaje de error.
        try:
            if self.tareas[posicion-1].completada:
                print('La tarea que intentas completar ya fue completada anteriormente.')
            else:
                self.tareas[posicion-1].tareaCompletada()
                print('Tarea completada con exito!!')
        except IndexError:
           print(Fore.RED+'La posición no existe.'+Style.RESET_ALL)
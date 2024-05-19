from colorama import Fore, Style

from models.tarea import Tarea

class TareasController:
    '''
        Clase TareasController donde están los módulos para realizar todas las gestiones con las tareas como agregar, mostrar.....
        
        Atributos: 
            tareas(list): Lista de tareas donde se almacena las tareas.
    '''
    def __init__(self):
        #Inicializa las tareas con una lista vacía.
        self.tareas = []
        
    #Muestra todas las tareas que hay en la lista en caso de que este vacía muestra un mensaje.
    def mostarTareas(self):
        if  len(self.tareas) == 0:
            print(Fore.LIGHTRED_EX+'No hay tareas en la lista')
        else:
            print(Fore.YELLOW)
            for i, tarea in enumerate(self.tareas):
                print(str(i+1)+'.',tarea)
        print(Style.RESET_ALL)
            
    '''
        Agregamos una nueva tarea
        
        Parámetros:
            descripción (str): descripción de la nueva tarea.
    '''
    def agregarTarea(self, descripcion):
        self.tareas.append(Tarea(descripcion))
        print(Fore.LIGHTGREEN_EX+'Se ha creado la tarea con exito!!'+Style.RESET_ALL)
    
    '''
        Eliminar una tarea
        
        Parámetros:
            posición(int): Posición de la tarea que queremos eliminar.
    '''     
    def eliminarTarea(self, posicion):
        #Excepción en el caso de que el valor introducido no sea correcto nos de un mensaje de error.
        try:
            del self.tareas[posicion-1]
            print(Fore.LIGHTBLUE_EX+'Se ha eliminado la tarea con exito!!'+Style.RESET_ALL)
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
                print(Fore.LIGHTRED_EX+'La tarea que intentas completar ya fue completada anteriormente.'+Style.RESET_ALL)
            else:
                self.tareas[posicion-1].tareaCompletada()
                print(Fore.LIGHTBLUE_EX+'Tarea completada con exito!!'+Style.RESET_ALL)
        except IndexError:
           print(Fore.LIGHTRED_EX+'La posición no existe.'+Style.RESET_ALL)
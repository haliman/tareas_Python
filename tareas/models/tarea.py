class Tarea:
    '''
        Clase Tarea
        
        Atributos:
            descripcion(str): descripción de la tarea.
            completada(booleana): estado de la tarea True completada y False incompleta.
    '''
    
    
    #Inicializa la instancia tarea con una nueva tarea y completada False.
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
        
    #Cambiamos el estado de completada a True.
    def tareaCompletada(self):
        self.completada = True 
               
    #Devuelve una representación de la tarea en string mostrando la descripcion y si esta o no completada.
    def __str__(self):
        return f"{self.descripcion}: {'Completada' if self.completada else 'Incompleta'}"
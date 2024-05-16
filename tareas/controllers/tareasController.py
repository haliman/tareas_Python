from colorama import Fore, Style

from models.tarea import Tarea

class TareasController:
    def __init__(self):
        self.tareas = []
    
    def mostarTareas(self):
        for i, tarea in enumerate(self.tareas):
            print(str(i+1)+'.',tarea)
            
    def agregarTarea(self, descripcion):
        self.tareas.append(Tarea(descripcion))
        
    def eliminarTarea(self, posicion):
        try:
            del self.tareas[posicion]
        except IndexError:
            print(Fore.RED+'La posición no existe.'+Style.RESET_ALL)
    
    def completarTarea(self, posicion):
        try:
            self.tareas[posicion].tareaCompletada()
        except IndexError:
           print(Fore.RED+'La posición no existe.'+Style.RESET_ALL)
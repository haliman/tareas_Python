class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
        
    def tareaCompletada(self):
        self.completada = True 
               
    def __str__(self):
        return f"{self.descripcion}: {'Completada' if self.completada else 'Incompleta'}"
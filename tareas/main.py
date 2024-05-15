from controllers.GestorTareas import GestorTareas

def menu():
    gestor = GestorTareas()
    
    descripcion = input('Introduzca la nueva tarea: ')
    gestor.agregarTarea(descripcion)
    gestor.mostarTareas()
    posicion =int(input('Completar tarea: ')) - 1
    gestor.completarTarea(posicion)
    gestor.mostarTareas()
    posicion =int(input('Eliminar tarea: ')) - 1
    gestor.eliminarTarea(posicion)
    gestor.mostarTareas()
    
if __name__ == "__main__":
    menu()
class Usuario:
    #Clase que representa a un usuario genérico de la tienda

    def __init__(self, identificador, nombre, email):
        # Atributos principales
        self.identificador = identificador  
        self.nombre = nombre              
        self.email = email                  

    def is_admin(self):
    #Indica si el usuario es administrador. 
        return False

    def __str__(self):
      
        return f"ID: {self.identificador}, Nombre: {self.nombre}, Email: {self.email}"
    
class Cliente(Usuario):

    def __init__(self, identificador, nombre, email, direccion):
        # Llamamos al constructor de Usuario
        super().__init__(identificador, nombre, email)
        # Atributo adicional
        self.direccion = direccion

    def __str__(self):
                                                                                                                        #????????????????
        return f"ID: {self.identificador}, Nombre: {self.nombre},Email: {self.email}, Dirección: {self.direccion}, Admin: {self.is_admin()}"

class Administrador(Usuario):
    """Clase que representa a un administrador de la tienda."""

    def __init__(self, identificador, nombre, email):
        # Constructor de Usuario
        super().__init__(identificador, nombre, email)

    def is_admin(self) -> bool:
        return True

    def __str__(self): 
        return f"ID: {self.identificador}, Nombre: {self.nombre}, Email: {self.email}, Admin: {self.is_admin()}"

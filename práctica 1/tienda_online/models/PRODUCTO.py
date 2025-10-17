
#clase producto 
class Producto:
    #Clase que representa un producto genérico en la tienda
   
    def __init__(self, identificador, name, price, stock):
        #constructor de la clase, se ejecuta al crear un objeto y sirve para darle sus valores iniciales.
        self.identificador = identificador
        self.name = name
        self.price = price
        self.stock = stock
        #Es una referencia al propio objeto, permite que cada instancia guarde y acceda a sus propios atributos.
            
    def __str__(self):
        #define el texto que se mostrará cuando imprimas el objeto con print()
        return f"identificador: {self.identificador}, name: {self.name}, price: {self.price}, stock: {self.stock}"
    
class ProductoElectronico(Producto):
    #Clase que representa un producto electrónico con garantía

    def __init__(self, identificador, name, price, stock, garantia_meses):
        #llama al constructor de la clase padre. Permite reutilizar el código ya escrito en la clase de la que hereda.
        super().__init__(identificador, name, price, stock)
        
        # Atributo adicional
        self.garantia_meses = garantia_meses
    
    def __str__(self):
        #Sobrescribimos __str__ para añadir la garantía.
        return f"identificador: {self.identificador}, name: {self.name}, price: {self.price}, stock: {self.stock}, garantía: {self.garantia_meses} meses"
    
class ProductoRopa(Producto):
    #Clase que representa un producto de ropa con talla y color."""

    def __init__(self, identificador, name, price, stock, talla, color):
        # Llamamos al constructor de Producto
        super().__init__(identificador, name, price, stock)
        # Atributos adicionales
        self.talla = talla
        self.color = color

    def __str__(self):
        #Sobrescribimos __str__ para añadir talla y color.
        return f"identificador: {self.identificador}, name: {self.name}, price: {self.price}, stock: {self.stock}, talla: {self.talla}, color: {self.color}"

    

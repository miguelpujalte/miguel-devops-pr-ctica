from tienda_online.models.USUARIO import Cliente, Administrador
from tienda_online.models.PEDIDO import Pedido
from tienda_online.models.PRODUCTO import Producto

class TiendaService:
    def __init__(self):
        self.usuarios = {} 
        self.productos = {}  
        self.pedidos = []    
        
#Registrar un usuario (cliente o administrador)
    def registrar_usuario(self, tipo, identificador, nombre, email, direccion=None):
        if tipo == "cliente":
            usuario = Cliente(identificador, nombre, email, direccion)
        else:
            usuario = Administrador(identificador, nombre, email)
        self.usuarios[identificador] = usuario
        return usuario
    
#Añadir productos de diferentes categorías al inventario
    def añadir_producto(self, producto):
        self.productos[producto.identificador] = producto
        
#Eliminar un producto por su identificador
    def eliminar_producto(self, identificador):
        if identificador in self.productos:
            del self.productos[identificador]
            
#Listar todos los productos disponibles
    def listar_productos(self):
        return list(self.productos.values())
    
#Realizar un pedido verificando que el usuario existe y que hay stock suficiente
    def realizar_pedido(self, cliente_id, lista_productos, fecha=""):
        if cliente_id not in self.usuarios:
            return None
        cliente = self.usuarios[cliente_id]
        if not isinstance(cliente, Cliente):
            return None

        productos_pedido = []
        for prod_id, cantidad in lista_productos:
            if prod_id not in self.productos:
                return None
            producto = self.productos[prod_id]
            if producto.stock < cantidad:
                return None
            producto.stock -= cantidad
            productos_pedido.append((producto, cantidad))
            
#Devolver el pedido creado
        pedido = Pedido("ped" + str(len(self.pedidos) + 1), cliente, productos_pedido, fecha)
        self.pedidos.append(pedido)
        return pedido
    
#Listar todos los pedidos de un usuario por id
    def listar_pedidos_usuario(self, cliente_id):
        pedidos_cliente = [p for p in self.pedidos if p.cliente.identificador == cliente_id]
        return pedidos_cliente


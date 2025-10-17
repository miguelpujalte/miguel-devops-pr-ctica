class Pedido:
    def __init__(self, identificador, cliente, productos, fecha):
        # identificador: string con el id del pedido
        # cliente: objeto Cliente
        # productos: lista de tuplas (producto, cantidad)
        # fecha: string con la fecha
        self.identificador = identificador
        self.cliente = cliente
        self.productos = productos
        self.fecha = fecha

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.price * cantidad
        return total

    def __str__(self):
        return f"Pedido {self.identificador} de {self.cliente.nombre} | Total: {self.calcular_total()}€"



 

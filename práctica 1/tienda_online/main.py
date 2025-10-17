from tienda_online.services.TiendaService import TiendaService
from tienda_online.models.PRODUCTO import Producto, ProductoElectronico, ProductoRopa

def main():
    # Crear la tienda
    tienda = TiendaService()

    # Registrar usuarios (3 clientes y 1 administrador)
    tienda.registrar_usuario("cliente", "c1", "Miguel", "miguel@gmail.com", "Calle Falsa 123")
    tienda.registrar_usuario("cliente", "c2", "Ana", "ana@gmail.com", "Av. Central 45")
    tienda.registrar_usuario("cliente", "c3", "Luis", "luis@gmail.com", "Rúa Nova 10")
    tienda.registrar_usuario("admin", "a1", "Admin", "admin@gmail.com")

    # Crear productos
    p1 = Producto("p1", "Ratón", 20, 10)
    p2 = ProductoElectronico("p2", "Portátil", 800, 5, 24)
    p3 = ProductoRopa("p3", "Camiseta", 15, 20, "M", "Rojo")
    p4 = ProductoRopa("p4", "Pantalón", 30, 15, "L", "Azul")
    p5 = Producto("p5", "Mochila", 40, 8)

    # Añadir productos a la tienda
    tienda.añadir_producto(p1)
    tienda.añadir_producto(p2)
    tienda.añadir_producto(p3)
    tienda.añadir_producto(p4)
    tienda.añadir_producto(p5)

    # Listar productos para comprobar inventario
    print("Inventario inicial:")
    for producto in tienda.listar_productos():
        print(producto)

    # Simular tres pedidos
    pedido1 = tienda.realizar_pedido("c1", [("p1", 2), ("p3", 1)])
    pedido2 = tienda.realizar_pedido("c2", [("p2", 1), ("p5", 1)])
    pedido3 = tienda.realizar_pedido("c3", [("p4", 2)])

    # Mostrar resumen de pedidos
    print("\nPedidos realizados:")
    print(pedido1)
    print(pedido2)
    print(pedido3)

    # Mostrar histórico de pedidos de un cliente
    print("\nHistórico de pedidos de Miguel:")
    for pedido in tienda.listar_pedidos_usuario("c1"):
        print(pedido)

    # Mostrar stock actualizado
    print("\nStock actualizado de productos:")
    for producto in tienda.listar_productos():
        print(producto)

if __name__ == "__main__":
    main()

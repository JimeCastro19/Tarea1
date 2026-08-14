class Producto:
    """Clase que representa un producto del supermercado"""
    def __init__(self, id_producto, nombre, precio, pais_origen, existencias):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.pais_origen = pais_origen
        self.existencias = existencias
    
    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | ${self.precio:.2f} | Origen: {self.pais_origen} | Stock: {self.existencias}"
    
    def __repr__(self):
        return self.__str__()


class Nodo:
    """Clase que representa un nodo en la lista doblemente enlazada"""
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None
        self.anterior = None


class ListaDobleProductos:
    """Clase que implementa una lista doblemente enlazada de productos"""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
    
    def esta_vacia(self):
        """Verifica si la lista está vacía"""
        return self.cabeza is None
    
    def agregar_inicio(self, producto):
        """Agrega un producto al inicio de la lista"""
        nuevo_nodo = Nodo(producto)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1
    
    def agregar_final(self, producto):
        """Agrega un producto al final de la lista"""
        nuevo_nodo = Nodo(producto)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1
    
    def eliminar_por_id(self, id_producto):
        """Elimina un producto por su ID"""
        actual = self.cabeza
        while actual:
            if actual.producto.id == id_producto:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                
                self.tamaño -= 1
                print(f"Producto con ID {id_producto} eliminado")
                return True
            actual = actual.siguiente
        print(f"Producto con ID {id_producto} no encontrado")
        return False
    
    def buscar_por_id(self, id_producto):
        """Busca un producto por su ID"""
        actual = self.cabeza
        while actual:
            if actual.producto.id == id_producto:
                return actual.producto
            actual = actual.siguiente
        return None
    
    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre (búsqueda parcial)"""
        productos_encontrados = []
        actual = self.cabeza
        while actual:
            if nombre.lower() in actual.producto.nombre.lower():
                productos_encontrados.append(actual.producto)
            actual = actual.siguiente
        return productos_encontrados
    
    def obtener_por_pais(self, pais):
        """Obtiene todos los productos de un país específico"""
        productos = []
        actual = self.cabeza
        while actual:
            if actual.producto.pais_origen.lower() == pais.lower():
                productos.append(actual.producto)
            actual = actual.siguiente
        return productos
    
    def actualizar_existencias(self, id_producto, cantidad):
        """Actualiza la cantidad de existencias de un producto"""
        producto = self.buscar_por_id(id_producto)
        if producto:
            producto.existencias = cantidad
            print(f"Existencias de {producto.nombre} actualizadas a {cantidad}")
            return True
        print(f"Producto con ID {id_producto} no encontrado")
        return False
    
    def mostrar_adelante(self):
        """Muestra todos los productos de adelante hacia atrás"""
        if self.esta_vacia():
            print("La lista está vacía")
            return
        
        print("\n=== LISTA DE PRODUCTOS (Adelante) ===")
        actual = self.cabeza
        contador = 1
        while actual:
            print(f"{contador}. {actual.producto}")
            actual = actual.siguiente
            contador += 1
        print(f"Total de productos: {self.tamaño}\n")
    
    def mostrar_atras(self):
        """Muestra todos los productos de atrás hacia adelante"""
        if self.esta_vacia():
            print("La lista está vacía")
            return
        
        print("\n=== LISTA DE PRODUCTOS (Atrás) ===")
        actual = self.cola
        contador = 1
        while actual:
            print(f"{contador}. {actual.producto}")
            actual = actual.anterior
            contador += 1
        print(f"Total de productos: {self.tamaño}\n")
    
    def obtener_tamaño(self):
        """Retorna el tamaño de la lista"""
        return self.tamaño


# Programa principal con ejemplos de uso
def main():
    # Crear la lista de productos
    lista_productos = ListaDobleProductos()
    
    # Agregar productos de ejemplo
    print("Agregando productos...")
    lista_productos.agregar_final(Producto(1, "Manzanas", 2.50, "Costa Rica", 50))
    lista_productos.agregar_final(Producto(2, "Bananas", 1.75, "Costa Rica", 100))
    lista_productos.agregar_final(Producto(3, "Leche", 3.20, "Costa Rica", 30))
    lista_productos.agregar_final(Producto(4, "Pan", 2.00, "Costa Rica", 45))
    lista_productos.agregar_final(Producto(5, "Queso", 5.50, "Argentina", 20))
    lista_productos.agregar_final(Producto(6, "Chocolate", 2.75, "Suiza", 60))
    lista_productos.agregar_final(Producto(7, "Café", 4.50, "Colombia", 25))
    lista_productos.agregar_final(Producto(8, "Huevos", 3.00, "Costa Rica", 80))
    
    # Mostrar la lista completa
    lista_productos.mostrar_adelante()
    
    # Buscar un producto por ID
    print("--- Buscando producto con ID 3 ---")
    producto = lista_productos.buscar_por_id(3)
    if producto:
        print(f"Encontrado: {producto}\n")
    
    # Buscar productos por nombre
    print("--- Buscando productos que contengan 'a' en el nombre ---")
    resultados = lista_productos.buscar_por_nombre("a")
    for p in resultados:
        print(p)
    print()
    
    # Obtener productos por país
    print("--- Productos de Costa Rica ---")
    costa_rica = lista_productos.obtener_por_pais("Costa Rica")
    for p in costa_rica:
        print(p)
    print()
    
    # Actualizar existencias
    print("--- Actualizando existencias ---")
    lista_productos.actualizar_existencias(1, 75)
    print()
    
    # Mostrar en orden inverso
    lista_productos.mostrar_atras()
    
    # Eliminar un producto
    print("--- Eliminando producto con ID 5 ---")
    lista_productos.eliminar_por_id(5)
    lista_productos.mostrar_adelante()
    
    # Agregar producto al inicio
    print("--- Agregando producto al inicio ---")
    lista_productos.agregar_inicio(Producto(9, "Agua", 1.50, "Costa Rica", 200))
    lista_productos.mostrar_adelante()


if __name__ == "__main__":
    main()

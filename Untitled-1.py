
#se asume que los primeros 3 puntos estan hechos

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
        """Busca productos por nombre (busqueda parcial)"""
        productos_encontrados = []
        actual = self.cabeza
        while actual:
            if nombre.lower() in actual.producto.nombre.lower():
                productos_encontrados.append(actual.producto)
            actual = actual.siguiente
        return productos_encontrados
    
    def obtener_por_pais(self, pais):
        """Obtiene todos los productos de un pais especifico"""
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
        """Muestra todos los productos de adelante hacia atras"""
        if self.esta_vacia():
            print("La lista está vacia")
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
        """Muestra todos los productos de atras hacia adelante"""
        if self.esta_vacia():
            print("La lista está vacia")
            return
        
        print("\n=== LISTA DE PRODUCTOS (Atras) ===")
        actual = self.cola
        contador = 1
        while actual:
            print(f"{contador}. {actual.producto}")
            actual = actual.anterior
            contador += 1
        print(f"Total de productos: {self.tamaño}\n")
    
    def obtener_tamaño(self):
        """Retorna el tamannio de la lista"""
        return self.tamaño


       # metodo para verificar si hay productos con existencias en 0 y generar una cola de reposición
    def generar_cola_reposicion(self):
        """Recorre la lista y devuelve una Cola con los productos en existencias 0"""
        cola_reposicion = ColaReposicion()
        actual = self.cabeza
        while actual:
            if actual.producto.existencias == 0:
                cola_reposicion.encolar(actual.producto)
            actual = actual.siguiente
        return cola_reposicion
      # metodo para generar una lista de frecuencia de paises de origen
    def generar_lista_frecuencia_paises(self):
        """Recorre la lista y arma una lista de frecuencia por pais de origen"""
        frecuencia = ListaFrecuenciaPaises()
        actual = self.cabeza
        while actual:
            frecuencia.registrar(actual.producto.pais_origen)
            actual = actual.siguiente
        return frecuencia

    #Metodo para generar reporte de recuperacion en un archivo .txt
    def generar_reporte(self, nombre_archivo="reporte_supermercado.txt"):
        """Genera un archivo .txt con el total a recuperar hoy (precio x existencias)"""
        if self.esta_vacia():
            print("La lista esta vacia, no se puede generar el reporte")
            return 0

        total_general = 0.0
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("REPORTE DE RECUPERACION - SUPERMERCADO\n")
            archivo.write("=" * 70 + "\n\n")

            actual = self.cabeza
            while actual:
                p = actual.producto
                subtotal = p.precio * p.existencias
                total_general += subtotal
                archivo.write(
                    f"ID: {p.id:<6f} Nombre: {p.nombre:<20} "
                    f"Precio: ${p.precio:>10.2f}  Existencias: {p.existencias:>5}  "
                    f"Subtotal: ${subtotal:>12.2f}\n"
                )
                actual = actual.siguiente

            archivo.write("\n" + "=" * 70 + "\n")
            archivo.write(f"TOTAL A RECUPERAR HOY: ${total_general:,.2f}\n")

        print(f"Reporte generado exitosamente en '{nombre_archivo}'")
        print(f"Total a recuperar hoy: ${total_general:,.2f}")
        return total_general

    def mostrar_listaRecursiva(self, nodo=None, contador=1):
        """Muestra la lista de productos de manera recursiva"""
        if nodo is None and contador == 1:
            if self.esta_vacia():
                print("La lista está vacia")
                return
            nodo=self.cabeza
            print("\n=== LISTA DE PRODUCTOS===")

        if nodo is None:
            print(f"Total de productos: {self.tamaño}\n")
            return 

        print(f"{contador}. {nodo.producto}")
        self.mostrar_listaRecursiva(nodo.siguiente, contador + 1)

#----------------------------------------------------------------------------------------------

class NodoCola:
    """Nodo de una cola simple (FIFO)"""
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None


class ColaReposicion:
    """Cola FIFO con los productos que hay que reponer (existencias en 0)"""
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, producto):
        nuevo_nodo = NodoCola(producto)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamaño += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        nodo = self.frente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamaño -= 1
        return nodo.producto

    def mostrar(self):
        if self.esta_vacia():
            print("No hay productos pendientes de reposicion")
            return
        print("\n=== COLA DE REPOSICION (Lista de compras) ===")
        actual = self.frente
        contador = 1
        while actual:
            print(f"{contador}. {actual.producto}")
            actual = actual.siguiente
            contador += 1
        print(f"Total de productos a reponer: {self.tamaño}\n")

#----------------------------------------------------------------------------------------------

class NodoFrecuencia:
    """Nodo que representa un pais y cuantos productos vienen de el"""
    def __init__(self, pais):
        self.pais = pais
        self.contador = 1
        self.siguiente = None


class ListaFrecuenciaPaises:
    """Lista enlazada simple que cuenta productos por pais de origen"""
    def __init__(self):
        self.cabeza = None

    def registrar(self, pais):
        actual = self.cabeza
        while actual:
            if actual.pais.lower() == pais.lower():
                actual.contador += 1
                return
            actual = actual.siguiente
        # el país no existía todavía: se agrega al inicio
        nuevo_nodo = NodoFrecuencia(pais)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def pais_mas_frecuente(self):
        if self.cabeza is None:
            return None, 0
        actual = self.cabeza
        pais_max, max_contador = actual.pais, actual.contador
        while actual:
            if actual.contador > max_contador:
                pais_max, max_contador = actual.pais, actual.contador
            actual = actual.siguiente
        return pais_max, max_contador

    def mostrar(self):
        if self.cabeza is None:
            print("No hay datos de paises registrados")
            return
        print("\n=== FRECUENCIA DE IMPORTACIoN POR PAiS ===")
        actual = self.cabeza
        while actual:
            print(f"{actual.pais}: {actual.contador} producto(s)")
            actual = actual.siguiente
        pais_max, contador_max = self.pais_mas_frecuente()
        print(f"\n Pais del que mas se importa: {pais_max} ({contador_max} producto(s))\n")


#--------------------------------------------------------------------------------------------------




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

   #comprobar desde la lista doble a una cola 
    print("--- Actualizando existencias de algunos productos a 0 para generar la cola de reposición ---")
    lista_productos.actualizar_existencias(1, 0)
    lista_productos.actualizar_existencias(2, 0)
    cola = lista_productos.generar_cola_reposicion()
    cola.mostrar()

    print("--- Frecuencia de paises de origen ---")
    frecuencia = lista_productos.generar_lista_frecuencia_paises()
    frecuencia.mostrar()

    lista_productos.generar_reporte()

    lista_productos.mostrar_listaRecursiva()
    


if __name__ == "__main__":
    main() 



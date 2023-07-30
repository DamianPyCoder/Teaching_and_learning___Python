# EJERCICIO PARA ENSEÑAR POO

class Comida:
    def __init__(self, nombre, precio, calorias):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias

    def info(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Calorías: {self.calorias}"


class Hamburguesa(Comida):
    def __init__(self, nombre, precio, calorias, carne, pan, ingredientes):
        super().__init__(nombre, precio, calorias)
        self.carne = carne
        self.pan = pan
        self.ingredientes = ingredientes

    def info(self):
        return f"{super().info()} - Carne: {self.carne} - Pan: {self.pan} - Ingredientes: {', '.join(self.ingredientes)}"


class Pizza(Comida):
    def __init__(self, nombre, precio, calorias, masa, ingredientes):
        super().__init__(nombre, precio, calorias)
        self.masa = masa
        self.ingredientes = ingredientes

    def info(self):
        return f"{super().info()} - Masa: {self.masa} - Ingredientes: {', '.join(self.ingredientes)}"


class Ensalada(Comida):
    def __init__(self, nombre, precio, calorias, tipo, aderezos):
        super().__init__(nombre, precio, calorias)
        self.tipo = tipo
        self.aderezos = aderezos

    def info(self):
        return f"{super().info()} - Tipo: {self.tipo} - Aderezos: {', '.join(self.aderezos)}"


# Crea instancias de hamburguesas, pizzas y ensaladas
hamburguesa1 = Hamburguesa("Hamburguesa Clásica", 8.99, 600, "Res", "Brioche", ["Lechuga", "Tomate", "Queso", "Cebolla"])
hamburguesa2 = Hamburguesa("Hamburguesa BBQ", 10.49, 750, "Pollo", "Integral", ["Bacon", "Cebolla caramelizada", "Queso cheddar"])
pizza1 = Pizza("Pizza Margarita", 12.99, 800, "Fina", ["Tomate", "Mozzarella", "Albahaca"])
pizza2 = Pizza("Pizza Hawaiana", 11.49, 900, "Gruesa", ["Piña", "Jamón", "Mozzarella"])
ensalada1 = Ensalada("Ensalada César", 6.99, 350, "César", ["Aderezo César", "Pollo a la parrilla", "Crutones"])
ensalada2 = Ensalada("Ensalada Mediterránea", 7.49, 250, "Mediterránea", ["Aceitunas", "Tomate", "Queso feta"])


print(hamburguesa1.info())
print(hamburguesa2.info())
print(pizza1.info())
print(pizza2.info())
print(ensalada1.info())
print(ensalada2.info())

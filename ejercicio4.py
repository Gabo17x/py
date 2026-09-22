class carrito_compras:
    def __init__(self):
        self.producto = []

    def agregar_productos(self, nombre, precio):
        self.producto.append({"nombre": nombre, "precio": precio})

    def total(self):
        return sum(p["precio"] for p in self.producto)

    def total_final(self, ciudad):
        subtotal = self.total()

        if subtotal > 300000:
            descuento = subtotal * 0.15
        else:
            descuento = 0

     
        if ciudad.lower() == "popayan" or ciudad.lower() == "popayán":
            envio = 0
        else:
            envio = 15000

        total = subtotal - descuento + envio

        return total


carrito = carrito_compras()

carrito.agregar_productos("camisa", 50000)
carrito.agregar_productos("pantalon", 110000)

print("Subtotal:", carrito.total())

ciudad = input("Ingrese la ciudad: ")

print("Valor total final:", carrito.total_final(ciudad))
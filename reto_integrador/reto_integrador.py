class Curso:
    def __init__(self):
        self.estudiantes = []

    def inscribir(self, nombre, edad):
        if edad > 15:
            self.estudiantes.append({"nombre": nombre, "edad": edad})
            print(f"{nombre} inscrito correctamente")
        else:
            print(f"{nombre} no puede inscribirse (menor de 16 años)")

    def listar_mayores_edad(self):
        return [e["nombre"] for e in self.estudiantes if e["edad"] > 18]


curso = Curso()
curso.inscribir("Ana", 20)
curso.inscribir("Luis", 15)
curso.inscribir("Carlos", 17)
curso.inscribir("María", 25)
curso.inscribir("Julián", 16)

print("Todos los estudiantes:", [e["nombre"] for e in curso.estudiantes])
print("Mayores de 18:", curso.listar_mayores_edad())

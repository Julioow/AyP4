x = 1
if x == 1:
    print("la variable x es igual a 1")

print("Fin del programa")


for i in range(0,10):
    print("Valor de i:", i)
    print(i)
print("Fin del programa 2")   


class Estudiante:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

estudiante1 = Estudiante("Juan Perez", "12345678")
print("Nombre del estudiante:", estudiante1.nombre)
print("Documento del estudiante:", estudiante1.documento)
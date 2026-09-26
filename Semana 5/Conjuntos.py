elemento = 5
lista = [5, 6, 7, 8, 9]
if elemento in lista:
    print("Está en la lista")

conjunto = {5, 4, 3, 2, 1}

if elemento in conjunto:
    print("Está en el conjunto")

conjunto = set(lista)
print(conjunto)
conjunto.add(8)
conjunto.discard(9)
conjunto.pop()
for num in conjunto:
    print(num)
#---------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
#UNION A Y B
C = A-B
#INTERSECCION A Y B
C= A & B

#DIFERENCIA SIMETRICA
C = A ^ B
print (C)

#SUBCONJUNTOS
if A<=B:
        print("A es subconjunto de B")
#-------------------------
TALLER1 = {"ANA", "CARLOS", "JAVIER", "LUCIA"}
TALLER2 = {"LUCIA", "MARIA", "CARLOS", "MIGUEL"}
TALLER3 = {"ANA", "JAVIER", "JOSE", "MIGUEL"}

REPETIDOS = (TALLER1 & TALLER2) | (TALLER2 & TALLER3) | (TALLER1 &  TALLER3)
print("LOS ALUMNOS QUE SE ENCUENTRAN INSCRITOS EN MAS DE UN TALLER SON:")
print(REPETIDOS)
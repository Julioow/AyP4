# COMPLEJIDAD:
# Tiempo 0(n)- invertir la cadena recorre todos los caracteres 
# Espacio 0(n) - creamos una copia invertido en memoria
texto = "reconocer"
def es_palindromo_invertir(texto):
    limpio = texto.replace(" ","").lower()
    invertido = limpio[::-1]
    return limpio == invertido


# Lo mismo pero con un ciclo for, sin crear una copia invertida
def es_palindromo_ciclo(texto):
    limpio = texto.replace(" ", "").lower()
    n = len(limpio)
    for i in range(n // 2):
        if limpio[i] != limpio[n - 1 - i]:
            return False
    return True   

# Usando recursión
def es_palindromo_recursivo(texto):
    limpio = texto.replace(" ", "").lower()
    def helper(limpio, inicio, fin):
        if inicio >= fin:
            return True
        if limpio[inicio] != limpio[fin]:
            return False
        return helper(limpio, inicio + 1, fin - 1)
    return helper(limpio, 0, len(limpio) - 1)

#otra forma de recursivo sin función helper
def es_palindromo_recursivo_simple(texto):
    limpio = texto.replace(" ", "").lower()
    def rec(limpio, inicio, fin):# Función recursiva que compara caracteres desde los extremos hacia el centro
        if inicio >= fin:
            return True
        if limpio[inicio] != limpio[fin]:
            return False
        return rec(limpio, inicio + 1, fin - 1)
    return rec(limpio, 0, len(limpio) - 1)

print("Usando invertir:", es_palindromo_invertir(texto))
print("Usando ciclo:", es_palindromo_ciclo(texto))    
print("Usando recursivo:", es_palindromo_recursivo(texto))
print("Usando recursivo simple:", es_palindromo_recursivo_simple(texto))

#---------------------------------------------------------------------------
# Complejidad de la función recursiva para sumar los elementos de una lista
listas = [5, 3, 1, 2]
def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return sumar_lista(lista[1:]) + lista[0]

print("Suma de la lista:", sumar_lista(listas))        

       
def suma_digito(n):
        if n==0:
            return 0
        else:
            return (n%10)+suma_digito(n//10)
print(suma_digito(1503))            

def busqueda_binaria_recursiva(lista, objetivo, izquierda=0, derecha=None):
        if derecha is None:
            derecha = len(lista) - 1
        if izquierda > derecha:
            return -1
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
        else:
            return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)
def permutaciones(lista):
    if len(lista)<=1:
        return [lista]  # Caso base: la permutación de una lista vacía o con un solo elemento es la lista misma
    resultado = []
    for i in range(len(lista)):
        elemento = lista[i]  # Selecciona el elemento actual
        resto = lista[:i] + lista[i+1:]  
        for perm in permutaciones(resto):  # Genera permutaciones del resto de la lista
            resultado.append([elemento] + perm)  # Agrega el elemento seleccionado al inicio de cada permutación del resto    
    return resultado      #

#fobonacci mejorado
    def fibonacci_tail(n, actual=0, siguiente=1):
        if n == 0:
            return actual
        return fibonacci_tail(n-1, siguiente, siguiente + actual)

#suma de una lista mejorara 
    def sumar_lista_tail(lista, acumulado=0):    
        if not lista:
            return acumulado
        return sumar_lista_tail(lista[1:], acumulado + lista[0])

# potencia mejorada
    def potencia_tail(base, exponente, resultado=1):
        if exponente == 0:
            return resultado
        return potencia_tail(base, exponente - 1, resultado * base)    

#tener el repositorio actualizado
#estudiar para el examen 
#leer la memorizacion y recusividad
         
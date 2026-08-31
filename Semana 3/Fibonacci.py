#def fibonacci(n):
    #if n <= 1:
        #return n
    #return fibonacci(n-1) + fibonacci(n-2)

#print(f"El resultado es:{fibonacci(5)}")

#No es eficiente con valores grandes

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memo(n, cache={}): #Se define el diccionario
    
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]

print(fibonacci_memo(100))

#Algoritmo recursivo
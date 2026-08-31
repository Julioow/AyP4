def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

#Este es mejor, como solo se llama el método 1 vez es más eficaz
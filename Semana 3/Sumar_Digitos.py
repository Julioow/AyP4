def sumar_digitos(n):
    if n // 10 == 0:
        return n
    return (n%10) + sumar_digitos(n//10)

print("La suma es", sumar_digitos(1541))
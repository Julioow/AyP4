def cambio_monedas(cantidad,monedas):
    if cantidad == 0:
        return 0

    if cantidad < 0:
        return float('inf')

    minimo = float('inf')
    for moneda in monedas:
        resultado = cambio_monedas(cantidad - moneda, monedas)
        if resultado != float('inf'):
            minimo = min(minimo, resultado + 1)
    return minimo

def cambio_monedas(cantidad,monedas, memo={}):
    if cantidad in memo:
        return memo[cantidad]

    if cantidad == 0:
        return 0

    if cantidad < 0:
        return float('inf')

    minimo = float('inf')
    for moneda in monedas:
        resultado = cambio_monedas(cantidad - moneda, monedas, memo)
        if resultado != float('inf'):
            minimo = min(minimo, resultado + 1)

    memo[cantidad] = minimo
    return minimo
                        
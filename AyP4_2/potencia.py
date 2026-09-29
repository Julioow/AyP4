a = 2
b = 3
def potencia(a, b):
    if b == 0:
        return 1
    return a * potencia(a, b-1)
    
# Exponenciación rápida (divide y vencerás)
def potencia_rapida(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = potencia_rapida(a, b // 2)
        return half * half
    else:
        return a * potencia_rapida(a, b - 1)
print("Potencia recursiva simple:", potencia(a, b))
print("Potencia rápida:", potencia_rapida(a, b))


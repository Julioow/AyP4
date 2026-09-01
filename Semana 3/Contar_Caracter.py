def contar_caracter(s, c):
    if len(s) == 0:
        return 0
    if s[0] == c:
        cuenta = 1
    else:
        cuenta = 0
        
    return cuenta + contar_caracter(s[1:], c)

print(contar_caracter("barbara", "f"))
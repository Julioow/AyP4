import re

texto = "gato, geto, gito, goto, guto, g4to, g-to"

# g.to = g + cualquier caracter + to
resultado = re.findall(r'g.to', texto)
print("patron 'g.to':", resultado)



#cuantificadores ?, *, +, {n}, {n,}, {n,m}
texto = "ac abc abbc abbbc abbbbc"
resultado = re.findall(r'ab+c', texto)
print(f"patron 'ab+c'(uno o mas b): {resultado}")

#validador de placas de autos: 3 letras mayusculas seguidas de un guion y 4 numeros
texto = "ABC-1234, AB-1234, ABCD-1234, ABC-123, ABC-12345"
resultado = re.findall(r'^[A-Z]{3}-\s[0-9]{4}$', texto)
print(bool(resultado)) 

# signo de $ 
texto = "El precio es de $100.00 (cien dolares)"
resultado = re.search(r"\$100\.00", texto)
print(bool(resultado))

#otro ejemplo de uso del signo de $ para validar un numero de telefono que termina con 4 digitos
texto = "Mi numero de telefono es 555-1234"
resultado = re.search(r"\d{3}-\d{4}$", texto)
print(bool(resultado))

#validador de telefono celular: 10 digitos, puede tener guiones o espacios
texto = "Mi numero de celular es 555-123-4567"
resultado = re.search(r"^(3[0-9]{2})[-\s]?([0-9]{3})[-\s]?([0-9]{2})[-\s]?([0-9]{2})$", texto)
print(bool(resultado))

#validar correo electronico: formato basico
texto = "Mi correo es john.doe@example.com"
resultado = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)
print(bool(resultado))

# validar fecha en formato dd/mm/yyyy
texto = "La fecha de hoy es 15/08/2024"
resultado = re.search(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$", texto)
print(bool(resultado))


"""menu de ingreso de datos de correo valido y contarseña valida, la contraseña debe tener al menos 8 caracteres, una mayuscula, una minuscula y un caracter especial
def validar_correo(correo):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo) 

def validar_contrasena(contrasena):
    return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$", contrasena) 

while True:
    print("Ingrese su correo electronico:")
    correo = input()
    print("Ingrese su contraseña:")
    contrasena = input()
    if validar_correo(correo):
        print("\nRegistro completado")
        break 
    elif validar_contrasena(contrasena):
        print("\nRegistro completado")
        break
    else:
        print("\nDatos invalidos")
    
        if not validar_correo(correo):
            print("El correo no tiene un formato valido.")
        if not validar_contrasena(contrasena):
            print("La contraseña no cumple los requisitos (8+ caracteres, Mayus, Minus, Num, Especial)")"""



#CONJUNTOS

#ejemplo 1 como eliminar duplicados 
A = [5,6,4,5,3,4,5,6,3,2,5,6,4,6,5]
set(A)
print(set(A))

#ejemplo 2 cuantas personas hay en la red social, cuales son los amigos en comun pero ordenados alfabeticamente
amigos_juan = {"Maria", "Pedro", "Ana", "Carlos", "Laura"}
amigos_maria = {"Pedro", "Laura", "Sofia", "Diego", "Ana", "Juan"}

print(f"cantidad de personas en la red social: {len(amigos_juan.union(amigos_maria))}")
amigos_en_comun = sorted (amigos_juan.intersection(amigos_maria))
print(amigos_en_comun)
print(f"amigos de Juan que no son amigos de Maria: {amigos_juan.difference(amigos_maria)}")
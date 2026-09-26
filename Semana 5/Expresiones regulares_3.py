import re

def validar_cont(password):

    if len(password) < 8:
        return False, "Minimo 8 caracteres"
    if not re.search(r"[A-Z]", password):
        return False, "Falta Mayuscula"
    if not re.search(r"[a-z]"):
        return False, "Falta Minuscula"
    if not re.search(r"[0-9]"):
        return False, "Falta Numero"
    if not re.search(r"[#¿?¡!$%&*-+]"):
        return False, "Falta caracter especial"
    return True, "Contraseña Válida"

patron = r"^[\w.+-]+@[A-Za-z\d-]+(\.[a-zA-Z\d-]+)?\.[A-Za-z]{2,}$"
correo = "juanjoseserna086@gmail.com"
print(correo)


#VALODAR FECHA EN FORMATO DD/MM/AAAA o D-MM-AAAA

patron = r"^(0[1-9]|[12]\d |3[01])(/-)(0[1-9]|1[0-2])[-/](19|20)\d{2}"

Fecha = "31/12/2024"
print(bool(re.match(patron, Fecha)))
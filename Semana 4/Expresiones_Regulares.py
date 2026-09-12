import re

# ==========================================================
# EXPRESIONES REGULARES EN PYTHON
# El módulo "re" permite buscar y trabajar con patrones
# dentro de textos.
# ==========================================================


# ----------------------------------------------------------
# 1. re.match()
# ----------------------------------------------------------
# re.match() busca el patrón ÚNICAMENTE al inicio del texto.
# Si encuentra el patrón, devuelve un objeto Match.
# Si no lo encuentra al inicio, devuelve None.

texto = "python me gusta mucho"

resultado = re.match("python", texto)

print(resultado)


# En este caso:
# El texto comienza con "python", por lo tanto sí encuentra
# la coincidencia.


# ----------------------------------------------------------
# 2. re.search()
# ----------------------------------------------------------
# re.search() busca el patrón en CUALQUIER PARTE del texto.
# No importa si está al principio, en el medio o más adelante.
# Si lo encuentra, devuelve un objeto Match.
# Si no lo encuentra, devuelve None.

texto = "Me gusta python"

resultado = re.search("python", texto)

print(resultado)


# En este caso:
# "python" no está al inicio, pero sí aparece dentro del texto.
# Por eso re.search() encuentra la coincidencia.


# ----------------------------------------------------------
# 3. re.findall()
# ----------------------------------------------------------
# re.findall() busca TODAS las apariciones del patrón
# dentro del texto.
#
# A diferencia de match() y search(), devuelve una lista
# con los textos encontrados.

texto = "python me gusta mucho, python es bueno"

resultado = re.findall("python", texto)

print(resultado)


# En este caso:
# "python" aparece 2 veces.
# Por eso el resultado es:
#
# ['python', 'python']
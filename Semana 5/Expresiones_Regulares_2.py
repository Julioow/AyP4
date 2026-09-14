import re

# . --> Representa cualquier caracter (una vez)
# ^ --> Al inicio del texto
# $ --> Al final del texto
# * --> Un caracter puede estar cero o más veces
# + --> Un caracter puede estar una o más veces
# ? --> Un caracter puede estar cero o una vez
# {} --> Un caracter está un número definido de veces ab{2,5}c (minimo dos hasta 5)
# \w --> Todas las letras (mayúsculas y minúsculas, número y guión bajo)

#Para validar un celular en Colombia

patron = r"^3[0-9]{2}([ -]?)[0-9]{3}\1[0-9]{2}\1[0-9]{2}$" #Ese \1 es como para que revise lo de la primer variable
resultado = bool(re.search(patron, "3192777285"))          #Que si el dato tiene - que lo demás también lo contenga y no se mezcle
print (resultado)

#Para validar una url
#texto = "https://www.google.com/search"

#resultado = re.findall(r"(https?)://(www\.)?([\w\.-]+)(/.)*", texto)
#print(resultado)


#Para validar un correo
#texto = "julianjaramillo82251@elpoli.edu.co"

#resultado = re.findall(r"\w+\w+\.\w{2,}", texto) #Para que entre la a y la c esté cualquiera de esas letras
#print(resultado)

#texto = "ac abc abbc abbbbc"

#resultado = re.findall(r"a[bdef]*c", texto) #Para que entre la a y la c esté cualquiera de esas letras
#print(resultado)                            #o de la A a la Z [a-z] (solo va a ver las minúsculas) (o ambas) [A-Za-z]

#texto = "ac abc abbc abbbbc"

#resultado = re.findall(r"ab?c", texto)
#print(resultado)

#texto = "Python es genial"

#if re.search(r"genial$", texto): #Para validar desde el final
    #print("Termina con genial")
    
#else:
    #print("No termina con genial")

#texto = "Python es genial"

#if re.search(r"^Python", texto): #Para validar desde el inicio
    #print("Empieza con Python")
    
#else:
    #print("No empieza con Python")

#texto = "gato, geto, gito, goto, guto, g4to, g-to"

#resultado = re.findall(r"g.to", texto) #para validar buscando caracteres
#print(resultado)
class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

class Pila:
  def __init__(self):
    self.tope = None
    self.tam = 0

  def esta_vacia(self):
    return self.tope is None

  def push(self,dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = self.tope
    self.tope = nuevo_nodo
    self.tam += 1

  def pop(self):
    if self.esta_vacia():
      raise Exception("Error: No hay elementos en la pila")
    dato = self.tope.dato
    self.tope = self.tope.siguiente
    self.tam -= 1
    return dato

  def peak(self):
    if self.esta_vacia():
      raise Exception("Error: No hay elementos en la pila")
    return self.tope.dato

  def __len__(self):
    return self.tam

  def __str__(self):
    if self.esta_vacia():
      return "Pila vacía"
    elementos = []
    actual = self.tope
    while actual:
      elementos.append(str(actual.dato))
      actual = actual.siguiente
    return "Tope --> " + "--> ".join(elementos) + "--> None"

def evaluar_posfija(expresion):

  tokens = expresion.split()
  pila = Pila()

  operadores = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b,
  }

  for token in tokens:
    if token.lstrip('-').replace('.', '').isdigit():
      valor = float(token) if '.' in token else int(token)
      pila.push(valor)
    elif token in operadores:
      a = pila.pop()
      b = pila.pop()
      resultado = operadores[token](a,b)
      pila.push(resultado)
    return pila.pop()

evaluar_posfija("3 4 5 * +")

#pila = Pila()
#pila.push(10)
#pila.push(20)
#pila.pop()
#print(len(pila))
#print(pila)
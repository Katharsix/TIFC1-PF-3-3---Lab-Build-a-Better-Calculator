def main():
  print("Hello learners!")
  print("¡Bienvenidos!")
  print("Probando suma: 7 + 2 + 8 ->", addmultiplenumbers([7, 2, 8]))
  print("Probando multiplicación: 4 × 6 × 6 ->", multiplymultiplenumbers([4, 6, 6]))
  print("¿El número 238 es par?", isiteven(148))
  print("¿El valor 6.7 es un número entero?", isitaninteger(6.7))

def addmultiplenumbers(lista_numeros):
    """Suma todos los digitos proporcionados en la lista."""
    acumulador = 0
    for valor in lista_numeros:
        acumulador += valor
    return acumulador


def multiplymultiplenumbers(lista_numeros):
    """Multiplica cada elemento de la lista en secuencia."""
    resultado = 1
    for valor in lista_numeros:
        resultado *= valor
    return resultado


def isiteven(numero):
    """Indica si el número entregado es un entero par."""
    return isinstance(numero, int) and numero % 2 == 0


def isitaninteger(numero):
    """Informa si el digito corresponde exactamente a un número entero."""
    return isinstance(numero, int)



if __name__ == "_main_":
    main()
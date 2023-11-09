https://replit.com/join/uhjfuqpdir-elisaramirez4

import random

def pedir_numero():
    try:
        herramienta = int(input())
        boolean = 1
    except ValueError:
        boolean = 0
        herramienta = 1000000
        print("Jaja, eso no es un numero")
    return herramienta, boolean

print("Caja de herramientas de [tu nombre]")
print("Dile adios al Syntax Error!")
print("Que deseas hacer?")
print("0 - Imprimir una variable")
print("1 - Pedirle algo al usuario")
print("2 - Crear un condicional")
print("3 - Crear un ciclo while")
print("4 - Crear un ciclo for")
print("5 - Crear una lista")
print("6 - Divertirme")

boolean = 0
while boolean == 0:
    herramienta, boolean=pedir_numero()

while herramienta not in list(range(7)):
    print("Escribe un numero valido.")
    print(list(range(7)))
    herramienta, boolean=pedir_numero()
    while boolean == 0:
        herramienta, boolean=pedir_numero()

if herramienta == 0:
    print("Usa la función:")
    print("    print()")
    print("Dentro del paréntesis puedes poner ya sea un texto que quieras entre comillas (dobles o simples funciona bien) o una variable, yeii")
    print("Ejemplos:")
    print("    print('Que ondiux')")
    print("    print('Elegiste el número',numero)")
elif herramienta == 1:
    print("Usa la función:")
    print("    input()")
    print("Dentro del paréntesis puedes poner un texto indicando al usuario que debe de escribir, yeii")
    print("OJO: para usar el dato hay que meterlo dentro de una variable, y no olvides convertirlo al tipo de dato adecuado, awesome!")
    print("Los tipos de datos son número entero int(), número decimal float() y texto str()")
    print("Ejemplos:")
    print("    numero_entero = int(input())")
    print("    numero_decimal = float(input())")
    print("    texto = str(input())")
elif herramienta == 2:
  print("Usa la función:")
  print("    if")  
  print("    elif")
  print("    else")
  print("Después de estos se pueden especificar las condiciones, con conectores como and o or también")
  print("Ejemplos:")
  print(" if number < 10:")
  print("    print('tu numero es menor a 10'")
elif herramienta == 3:
  print("Para crear un ciclo while:")
  print("    while condicion:")
  print("    # Código que se ejecutará mientras la condición sea verdadera")
  print("Ejemplo:")
  print("contador = 0")
  print("while contador < 5:")
  print("    print('Iteración número', contador)")
  print("    contador += 1")
elif herramienta == 4:
  print("Para crear un ciclo for:")
  print("    for elemento in lista:")
  print("    # Código que se ejecutará para cada elemento en la lista")
  print("Ejemplo:")
  print(" nombres = ['Ana', 'Juan', 'Luis']")
  print(" for nombre in nombres:")
  print("    print('Hola,', nombre)")
elif herramienta == 5:
  print("Para crear una lista, usa corchetes [] y separa los elementos con comas")
  print("Ejemplo:")
  print("    mi_lista = [1, 2, 3]")
  print("Puedes guardar varios elementos, como números, texto o cualquier otro tipo de datos, dentro de una lista.")
  print("Ejemplo:")
  print("   nombres = ['Ana', 'Juan', 'Luis']")
  print("Ejemplo:")
  print("   numeros = [1, 2, 3, 4, 5]")
  print("   primer_numero = numeros[0]")
elif herramienta == 6:
    aleatorio = random.randint(1,3)
    if aleatorio == 1:
        print("Las variables tipo float se llaman así porque en los decimales el punto flota, ja, que gracioso, no?")
    elif aleatorio == 2:
        print("Sabías que las computadoras no entienden las letras ni las palabras, solo entienden 0 y 1, imaginate hablar así, 000111000 jajaja que gracioso.")
    elif aleatorio == 3:
        print("Python tiene además de las listas, unas cosas llamadas tuplas, la única diferencia es que ocupan menos espacio en la memoria, jaja, que manera tan rara de ahorrar")

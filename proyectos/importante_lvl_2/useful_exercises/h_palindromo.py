"""
==================
    PALINDROMO
==================

Animamos a los usuarios a introducir
cinco palabras. Después comprobamos
cuáles son palabras palíndromas o no.

¿Qué es un palíndromo? Es una palabra
que podemos leer de la misma manera
desde la izquierda a la derecha y viceversa.
"""
from ....base_functions import *

while True:
    frase = wInput("\nIngresa una frase: ")

    wait()

    palindromos = []
    for palabra in frase.split():
        palabra_invertida = palabra[::-1]
        if palabra == palabra_invertida:
            palindromos.append(palabra)

    cantidad_palindromos = len(palindromos)
    if cantidad_palindromos > 0:
        palindromos_str = ", ".join(palindromos)
        write(f"\nDentro de la frase hay {cantidad_palindromos} palíndromos.\nEstos son: {palindromos_str}\n")
    else:
        write("\nNo se encontraron palíndromos en la frase.\n")

    playAgain()
    
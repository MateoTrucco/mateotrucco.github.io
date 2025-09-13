"""
=============================
    ¿CUAL ES MI ACRONIMO?
=============================

Vamos a pedir al usuario que ingrese
el significado completo de una
organización o concepto y con ello
como resultado obtendremos el acrónimo.
"""
from ....base_functions import *

while True:
    frase = wInput("\nFrase para transformar: ")

    acronimo = ""
    for palabra in frase.split():
        acronimo += palabra[0]
        acronimo = acronimo.upper()

    wait()
    write(f"\nLa frase transformada es: | {acronimo} |\n")

    playAgain()

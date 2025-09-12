"""
=========================
    FUNCIONES BASICAS
=========================
"""

import time
import winsound

def wait(taim=0.5):
    time.sleep(taim)

def write(texto, speed=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        wait(speed)

def wInput(texto, speed=0.03):
    write(texto, speed)
    rta = input('\n--- ')
    return rta

def playAgain():
    write("\n--------------------------------------------", 0.01)
    again = wInput("\n¿Quieres jugar de nuevo? (s/n): ")
    wait()
    if again == "s" or again == "S":
        write("\nOk, vuelve a intentarlo!\n")
        write("--------------------------------------------\n", 0.01)
    else: 
        write("\n¡Gracias por jugar!\n")
        write("--------------------------------------------\n", 0.01)
        return exit()

def encuadrar(texto):
    lineas = texto.split('\n')
    max_longitud = max(len(linea) for linea in lineas)
    ancho_recuadro = max_longitud + 2

    texto_encuadrado = ''

    texto_encuadrado += '┌' + '─' * ancho_recuadro + '┐\n'
    for linea in lineas:
        texto_encuadrado += '│ ' + linea.ljust(max_longitud) + ' │\n'
    texto_encuadrado += '└' + '─' * ancho_recuadro + '┘'

    return texto_encuadrado

def alarm(s=0, loop=1):
    for i in range(loop):
        if s == 0:
            winsound.Beep(500, 100)
            winsound.Beep(2000, 100)
            winsound.Beep(500, 100)
            winsound.Beep(1000, 500)
            winsound.Beep(2000, 300)
        elif s == 1:
            winsound.Beep(250, 100)
            winsound.Beep(200, 100)
            winsound.Beep(250, 100)
            winsound.Beep(500, 500)
            winsound.Beep(1000, 300)
        elif s == 2:
            winsound.Beep(200, 300)
            winsound.Beep(500, 300)
            winsound.Beep(1500, 300)
            winsound.Beep(500, 300)
            winsound.Beep(1000, 300)
            winsound.Beep(800, 300)
            winsound.Beep(600, 300)
            winsound.Beep(400, 300)
        elif s == 3:
            winsound.Beep(300, 200)
            winsound.Beep(800, 100)
            winsound.Beep(100, 150)
            winsound.Beep(700, 150)
            winsound.Beep(1200, 150)
            winsound.Beep(300, 100)
            winsound.Beep(500, 200)
            winsound.Beep(1000, 300)
        elif s == 4:
            winsound.Beep(100, 200)
            winsound.Beep(250, 100)
            winsound.Beep(800, 100)
            winsound.Beep(300, 150)
            winsound.Beep(700, 150)
            winsound.Beep(1200, 150)
            winsound.Beep(300, 100)
            winsound.Beep(500, 200)
            winsound.Beep(1000, 300)
        elif s == 5:
            winsound.Beep(900, 200)
            winsound.Beep(200, 100)
            winsound.Beep(800, 100)
            winsound.Beep(400, 150)
            winsound.Beep(1000, 150)
            winsound.Beep(200, 100)
            winsound.Beep(600, 200)
            winsound.Beep(1200, 300)

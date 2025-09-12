"""
==============
    ALARMA
==============
"""
from a_funciones_basicas import *

seg = 0
min = 0
hour = 0
total = 0

tiempo = int(wInput("¿Cuantos segundos dura la alarma?: "))

while total < tiempo:
    wait(1)
    seg += 1
    total += 1
    if seg == 60:
        seg = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1
    print(f"{hour:02}:{min:02}:{seg:02}", end="\r")

print("\n¡ALARMA TERMINADA!")
alarm(5, 3)
